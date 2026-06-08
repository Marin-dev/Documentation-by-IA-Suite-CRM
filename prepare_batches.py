"""Prépare les listes de fichiers par agent pour les lots 2+ (include/, modules/, tests/)."""
import json
from pathlib import Path
from collections import defaultdict

with open("docs/hierarchical/doc-plan.json", encoding="utf-8") as f:
    plan = json.load(f)

# Group files by immediate parent
by_folder = defaultdict(list)
for fi in plan["files"]:
    p = fi["path"]
    parent = "/".join(p.split("/")[:-1]) if "/" in p else "."
    by_folder[parent].append(p)

# ── include/ ─────────────────────────────────────────────────────────────────
# On veut un agent par sous-dossier profond de include/ (pas par sous-sous-dossier)
# Regrouper par "include/SubSystem" (depth-2 prefix)
inc_groups = defaultdict(list)
for folder, files in by_folder.items():
    if not folder.startswith("include/"):
        continue
    parts = folder.split("/")
    subsystem = "/".join(parts[:2])  # include/SubSystem
    inc_groups[subsystem].extend(files)

# Ajouter les fichiers directement dans include/ (s'il y en a)
if "include" in by_folder:
    inc_groups["include"].extend(by_folder["include"])

inc_sorted = sorted(inc_groups.keys())
print(f"include/ → {len(inc_sorted)} groupes")
for i, g in enumerate(inc_sorted):
    print(f"  [{i}] {g}: {len(inc_groups[g])} files")

# ── modules/ ──────────────────────────────────────────────────────────────────
# Un agent par module (depth-2, couvre tous les sous-fichiers)
mod_groups = defaultdict(list)
for folder, files in by_folder.items():
    if not folder.startswith("modules/"):
        continue
    parts = folder.split("/")
    module = "/".join(parts[:2])  # modules/ModuleName
    mod_groups[module].extend(files)

mod_sorted = sorted(mod_groups.keys())
print(f"\nmodules/ → {len(mod_sorted)} modules")

# ── tests/ ────────────────────────────────────────────────────────────────────
tests_groups = defaultdict(list)
for folder, files in by_folder.items():
    if not folder.startswith("tests/"):
        continue
    parts = folder.split("/")
    group = "/".join(parts[:2])  # tests/SubArea
    tests_groups[group].extend(files)
if "tests" in by_folder:
    tests_groups["tests"].extend(by_folder["tests"])

tests_sorted = sorted(tests_groups.keys())
print(f"\ntests/ → {len(tests_sorted)} groupes")

# ── Sauvegarder les batches ───────────────────────────────────────────────────
batches = {
    "include": {k: inc_groups[k] for k in inc_sorted},
    "modules": {k: mod_groups[k] for k in mod_sorted},
    "tests":   {k: tests_groups[k] for k in tests_sorted},
}

with open("docs/hierarchical/agent_batches.json", "w", encoding="utf-8") as f:
    json.dump(batches, f, indent=2, ensure_ascii=False)

print("\nSaved agent_batches.json")

# Stats
total_inc = sum(len(v) for v in inc_groups.values())
total_mod = sum(len(v) for v in mod_groups.values())
total_tests = sum(len(v) for v in tests_groups.values())
print(f"include: {total_inc} files | modules: {total_mod} files | tests: {total_tests} files")

# Print module list for batch planning (10 per batch)
print("\nModules batch plan (10/lot):")
for i in range(0, len(mod_sorted), 10):
    batch = mod_sorted[i:i+10]
    print(f"  Lot {i//10 + 1}: {', '.join(m.split('/')[1] for m in batch)}")
