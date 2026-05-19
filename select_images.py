import os
import csv
import glob

base_dir = "/home/robot/gitrepos/2026_RH_SUMMIT/SUMMIT_SUMMARY"
folders = [
    "20260512_1030_experimenting-with-vllm-on-kubernetes-microshift-podman-kserve",
    "20260512_1145_red-hat-lightspeed-roadmap",
    "20260512_1300_beyond-mlops-establishing-agentops-for-enterprise-ai-on-red-hat-ai",
    "20260512_1530_chain-of-trust-validated-and-benchmarked-ai-models",
    "20260512_1530_deploy-agentic-ai-devops-assistant-incident-response-with-rhoai",
    "20260513_1030_agentops-in-production-agentic-e2e-observability-with-red-hat-ai",
    "20260513_1330_agent-skills-with-quarkus-and-langchain4j",
    "20260513_1420_aiops-meets-agentic-automation-servicenow-and-red-hat",
    "20260513_1530_protecting-genai-apps-with-gaas",
    "20260514_0945_automated-rag-pattern-discovery-with-red-hat-ai",
    "20260514_1100_building-production-ready-ai-agents-for-enterprise-it-automation",
    "20260514_1300_container-hardening-zero-to-hero-with-red-hat-hardened-images"
]

mapping = {}

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    img_dir = os.path.join(folder_path, "img")
    
    # Heuristic 1: Look for PXL_*.jpg
    pxl_images = sorted(glob.glob(os.path.join(img_dir, "PXL_*.jpg")))
    if pxl_images:
        selected = [os.path.basename(p) for p in pxl_images[:4]]
        mapping[folder] = selected
        continue
    
    # Heuristic 2: Use img_manifest.csv
    manifest_path = os.path.join(folder_path, "img_manifest.csv")
    if os.path.exists(manifest_path):
        images = []
        with open(manifest_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    area = int(row['width']) * int(row['height'])
                    images.append({
                        'file': row['image_file'],
                        'page': row['page_number'],
                        'area': area
                    })
                except (ValueError, KeyError):
                    continue
        
        # Sort by area descending
        images.sort(key=lambda x: x['area'], reverse=True)
        
        selected = []
        selected_pages = set()
        
        # Prefer spread across pages
        # First pass: one largest image per page, up to 4 pages
        for img in images:
            if img['page'] not in selected_pages:
                selected.append(img['file'])
                selected_pages.add(img['page'])
            if len(selected) == 4:
                break
        
        # Second pass: if we still need more, take the largest remaining ones
        if len(selected) < 4:
            for img in images:
                if img['file'] not in selected:
                    selected.append(img['file'])
                if len(selected) == 4:
                    break
        
        mapping[folder] = selected
    else:
        mapping[folder] = []

for folder, files in mapping.items():
    print(f"{folder}: {', '.join(files)}")
