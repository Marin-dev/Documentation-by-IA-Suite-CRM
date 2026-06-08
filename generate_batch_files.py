"""Génère des fichiers texte avec les listes de fichiers pour chaque batch d'agents."""
import json
from pathlib import Path

with open("docs/hierarchical/agent_batches.json", encoding="utf-8") as f:
    batches = json.load(f)

out = Path("docs/hierarchical/batch_lists")
out.mkdir(parents=True, exist_ok=True)

# include/ : 5 lots de ~9 groupes
inc_groups = list(batches["include"].items())
BATCH_SIZE = 10
for i in range(0, len(inc_groups), BATCH_SIZE):
    chunk = inc_groups[i:i + BATCH_SIZE]
    lot_num = i // BATCH_SIZE + 1
    lines = []
    for group, files in chunk:
        lines.append(f"# {group}")
        lines.extend(files)
    fname = out / f"include_lot{lot_num}.txt"
    fname.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for _, v in chunk)
    print(f"include lot{lot_num}: {len(chunk)} groups, {total} files -> {fname.name}")

# modules/ : 12 lots de 10
mod_groups = list(batches["modules"].items())
for i in range(0, len(mod_groups), BATCH_SIZE):
    chunk = mod_groups[i:i + BATCH_SIZE]
    lot_num = i // BATCH_SIZE + 1
    lines = []
    for group, files in chunk:
        lines.append(f"# {group}")
        lines.extend(files)
    fname = out / f"modules_lot{lot_num}.txt"
    fname.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for _, v in chunk)
    print(f"modules lot{lot_num}: {len(chunk)} modules, {total} files -> {fname.name}")

# tests/ : 2 lots de 4
tests_groups = list(batches["tests"].items())
for i in range(0, len(tests_groups), 4):
    chunk = tests_groups[i:i + 4]
    lot_num = i // 4 + 1
    lines = []
    for group, files in chunk:
        lines.append(f"# {group}")
        lines.extend(files)
    fname = out / f"tests_lot{lot_num}.txt"
    fname.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for _, v in chunk)
    print(f"tests lot{lot_num}: {len(chunk)} groups, {total} files -> {fname.name}")

print("\nDone.")
