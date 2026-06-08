"""Group files by immediate parent folder for agent batching."""
import json
from pathlib import Path
from collections import defaultdict

with open("docs/hierarchical/doc-plan.json", encoding="utf-8") as f:
    plan = json.load(f)

# Group files by immediate parent folder
by_folder = defaultdict(list)
for fi in plan["files"]:
    p = fi["path"]
    parent = "/".join(p.split("/")[:-1]) if "/" in p else "."
    by_folder[parent].append(fi["path"])

# Sort folders by depth then name
sorted_folders = sorted(by_folder.keys(), key=lambda x: (len(x.split("/")), x))

print(f"Total folders with files: {len(sorted_folders)}")
print()

# Group by top-level section for batch planning
sections = defaultdict(list)
for folder in sorted_folders:
    top = folder.split("/")[0] if "/" in folder else folder
    sections[top].append(folder)

for section, folders in sorted(sections.items(), key=lambda x: -sum(len(by_folder[f]) for f in x[1])):
    total_files = sum(len(by_folder[f]) for f in folders)
    print(f"{section}/: {len(folders)} folders, {total_files} files")

# Save grouped structure for use in agents
grouped = {folder: by_folder[folder] for folder in sorted_folders}
with open("docs/hierarchical/grouped_files.json", "w", encoding="utf-8") as f:
    json.dump(grouped, f, indent=2, ensure_ascii=False)
print("\nSaved grouped_files.json")
