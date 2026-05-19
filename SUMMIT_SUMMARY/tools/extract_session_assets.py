#!/usr/bin/env python3
"""Extract and merge session artifacts from transcript/PDF sources.

This script does extraction only:
- Reads transcript text files from a talk directory
- Reads all PDF files from the same directory
- Extracts text from all PDFs
- Extracts embedded images only from transcript-like PDFs
- Copies standalone image files from the source talk directory
- Applies transcript cleanup rules (e.g., bomb -> BOM)
- Writes source_bundle.txt, img/ assets, and img_manifest.csv
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except Exception as exc:  # pragma: no cover
    fitz = None
    FITZ_IMPORT_ERROR = exc
else:
    FITZ_IMPORT_ERROR = None


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
TRANSCRIPT_MARKERS = ("summary keywords", "speakers")


def normalize_bom_terms(text: str) -> str:
    """Normalize common transcription mistake: bomb -> BOM."""
    text = re.sub(r"\bbombs\b", "BOMs", text, flags=re.IGNORECASE)
    text = re.sub(r"\bbomb\b", "BOM", text, flags=re.IGNORECASE)
    return text


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def normalize_for_matching(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def source_archive_ref(talk_dir: Path) -> str:
    parts = list(talk_dir.parts)

    if "otter_summaries" in parts:
        anchor = parts.index("otter_summaries") + 1
        relative_parts = parts[anchor:]
        if relative_parts:
            return "/".join(relative_parts)

    return talk_dir.name


def is_transcript_like_pdf(pdf_path: Path, talk_dir: Path) -> bool:
    normalized_stem = normalize_for_matching(pdf_path.stem)
    normalized_talk_name = normalize_for_matching(talk_dir.name)

    if "transcript" in normalized_stem:
        return True

    if normalized_stem == normalized_talk_name:
        return True

    if fitz is None:
        return False

    doc = fitz.open(pdf_path)
    try:
        sampled_text = []
        for page_index in range(min(2, len(doc))):
            sampled_text.append(doc.load_page(page_index).get_text("text"))
    finally:
        doc.close()

    normalized_text = "\n".join(sampled_text).lower()
    return all(marker in normalized_text for marker in TRANSCRIPT_MARKERS)


def reset_image_dir(img_dir: Path) -> None:
    if img_dir.exists():
        for child in img_dir.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    else:
        img_dir.mkdir(parents=True, exist_ok=True)


def copy_loose_images(talk_dir: Path, img_dir: Path) -> list[dict[str, str]]:
    manifest_rows: list[dict[str, str]] = []

    for image_path in sorted(p for p in talk_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS):
        destination_path = img_dir / image_path.name
        shutil.copy2(image_path, destination_path)
        manifest_rows.append(
            {
                "image_file": image_path.name,
                "source_pdf": image_path.name,
                "page_number": "",
                "image_index": "",
                "width": "",
                "height": "",
            }
        )

    return manifest_rows


def extract_pdf_text_and_images(
    pdf_path: Path,
    img_dir: Path,
    *,
    extract_images: bool,
) -> tuple[str, list[dict[str, str]]]:
    if fitz is None:
        raise RuntimeError(
            "PyMuPDF is required for PDF text/image extraction. "
            f"Import error: {FITZ_IMPORT_ERROR}"
        )

    doc = fitz.open(pdf_path)
    text_chunks: list[str] = []
    manifest_rows: list[dict[str, str]] = []

    safe_stem = re.sub(r"[^A-Za-z0-9._-]+", "_", pdf_path.stem)

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        page_no = page_index + 1
        page_text = page.get_text("text")

        text_chunks.append(
            "\n".join(
                [
                    f"--- PDF: {pdf_path.name} | Page: {page_no} ---",
                    page_text.strip(),
                    "",
                ]
            )
        )

        if not extract_images:
            continue

        images = page.get_images(full=True)
        for image_idx, image_info in enumerate(images, start=1):
            xref = image_info[0]
            base_image = doc.extract_image(xref)
            ext = base_image.get("ext", "bin")
            image_bytes = base_image["image"]
            width = str(base_image.get("width", ""))
            height = str(base_image.get("height", ""))

            image_name = f"{safe_stem}_p{page_no:03d}_img{image_idx:02d}.{ext}"
            image_path = img_dir / image_name
            image_path.write_bytes(image_bytes)

            manifest_rows.append(
                {
                    "image_file": image_name,
                    "source_pdf": pdf_path.name,
                    "page_number": str(page_no),
                    "image_index": str(image_idx),
                    "width": width,
                    "height": height,
                }
            )

    doc.close()
    return "\n".join(text_chunks).strip() + "\n", manifest_rows


def build_bundle(talk_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    img_dir = output_dir / "img"
    reset_image_dir(img_dir)

    txt_files = sorted(talk_dir.glob("*.txt"))
    pdf_files = sorted(talk_dir.glob("*.pdf"))
    datetime_file = talk_dir / "datetime.txt"
    note_file = talk_dir / "note.txt"

    bundle_parts: list[str] = []

    bundle_parts.append("# Session Source Bundle")
    bundle_parts.append(f"Source archive ref: {source_archive_ref(talk_dir)}")
    bundle_parts.append("")

    if datetime_file.exists():
        dt_text = normalize_bom_terms(read_text_file(datetime_file).strip())
        bundle_parts.extend(
            [
                "## Session Datetime",
                dt_text,
                "",
            ]
        )

    if note_file.exists():
        note_text = normalize_bom_terms(read_text_file(note_file).strip())
        bundle_parts.extend(
            [
                "## Session Notes",
                note_text,
                "",
            ]
        )

    transcript_files = [
        p for p in txt_files if p.name.lower() not in {"datetime.txt", "note.txt"}
    ]

    for txt_path in transcript_files:
        text = normalize_bom_terms(read_text_file(txt_path))
        bundle_parts.extend(
            [
                f"## Transcript: {txt_path.name}",
                text.strip(),
                "",
            ]
        )

    all_manifest_rows: list[dict[str, str]] = []

    if pdf_files:
        for pdf_path in pdf_files:
            pdf_text, rows = extract_pdf_text_and_images(
                pdf_path,
                img_dir,
                extract_images=is_transcript_like_pdf(pdf_path, talk_dir),
            )
            pdf_text = normalize_bom_terms(pdf_text)
            bundle_parts.extend(
                [
                    f"## PDF Text: {pdf_path.name}",
                    pdf_text.strip(),
                    "",
                ]
            )
            all_manifest_rows.extend(rows)
    else:
        bundle_parts.extend(["## PDF Text", "No PDF files found in this talk folder.", ""])

    all_manifest_rows.extend(copy_loose_images(talk_dir, img_dir))

    source_bundle = output_dir / "source_bundle.txt"
    source_bundle.write_text("\n".join(bundle_parts).strip() + "\n", encoding="utf-8")

    manifest_path = output_dir / "img_manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as csvfile:
        fieldnames = ["image_file", "source_pdf", "page_number", "image_index", "width", "height"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_manifest_rows:
            writer.writerow(row)

    print(f"Wrote: {source_bundle}")
    print(f"Wrote: {manifest_path}")
    print(f"Images extracted: {len(all_manifest_rows)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract session assets from talk folder.")
    parser.add_argument("--talk-dir", required=True, help="Path to source talk folder under otter_summaries.")
    parser.add_argument("--output-dir", required=True, help="Path to destination session folder in SUMMIT_SUMMARY.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    talk_dir = Path(args.talk_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if not talk_dir.exists() or not talk_dir.is_dir():
        print(f"Error: talk-dir does not exist or is not a directory: {talk_dir}", file=sys.stderr)
        return 1

    try:
        build_bundle(talk_dir, output_dir)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
