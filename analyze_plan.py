import json
from collections import defaultdict

with open("docs/hierarchical/doc-plan.json", encoding="utf-8") as f:
    plan = json.load(f)

# Files par dossier top-level
top_counts = defaultdict(int)
for fi in plan["files"]:
    top = fi["path"].split("/")[0]
    top_counts[top] += 1

print("Files par dossier top-level:")
for k, v in sorted(top_counts.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")

# Depth-2 folders sous modules/
print()
mod_folders = [f for f in plan["folders"] if f["path"].startswith("modules/") and f["depth"] == 2]
print(f"Modules documentés (depth-2): {len(mod_folders)}")
for f in mod_folders:
    prefix = f["path"] + "/"
    cnt = sum(1 for fi in plan["files"] if fi["path"].startswith(prefix) or "/".join(fi["path"].split("/")[:2]) == f["path"])
    print(f"  {f['path']}: ~{cnt} files")

# Depth-2 folders sous include/
print()
inc_folders = [f for f in plan["folders"] if f["path"].startswith("include/") and f["depth"] == 2]
print(f"Include sous-dossiers (depth-2): {len(inc_folders)}")
for f in inc_folders:
    print(f"  {f['path']}")
