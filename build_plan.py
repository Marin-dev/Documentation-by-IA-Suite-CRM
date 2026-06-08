import os, json
from pathlib import Path
from datetime import datetime
from collections import Counter

REPO = Path(r"c:\Github\Documentation by IA Suite CRM\SuiteCRM")

EXCLUDE_DIRS = {
    ".git", "build", "upload", "jssource", "themes",
    "Zend", "Pear", "Smarty", "tcpdf", "nusoap",
    "HTTP_WebDAV_Server", "fonts", "images", "javascript",
    "vendor", "__pycache__", "node_modules", ".next", ".nuxt",
    "coverage", "dist", "out", "target", "bin", "obj",
    "venv", ".venv", "metadata", "language",
}

INCLUDE_EXT = {".php", ".js", ".json", ".yml", ".yaml", ".xml", ".md", ".env", ".ini", ".conf"}
IGNORE_FILES = {"composer.lock", "files.md5", "package-lock.json", "yarn.lock"}
SKIP_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
    ".woff", ".woff2", ".ttf", ".eot", ".otf",
    ".pdf", ".zip", ".tar", ".gz", ".bz2", ".7z",
    ".mp4", ".mp3", ".wav", ".avi", ".mov",
    ".map", ".lock", ".log", ".css", ".less", ".scss", ".sass",
    ".tpl", ".html", ".htm", ".txt", ".iml", ".bat", ".sh",
}

def is_documentable(fname):
    if fname in IGNORE_FILES:
        return False
    ext = Path(fname).suffix.lower()
    if ext in SKIP_EXT:
        return False
    name = fname.lower()
    if ".min." in name:
        return False
    return ext in INCLUDE_EXT

LANG_MAP = {
    ".php": "PHP", ".js": "JavaScript", ".json": "JSON",
    ".yml": "YAML", ".yaml": "YAML", ".xml": "XML",
    ".md": "Markdown", ".env": "ENV", ".ini": "INI", ".conf": "Conf",
}

files = []
folders = set()

for root, dirs, filenames in os.walk(REPO):
    root_path = Path(root)
    rel_root = root_path.relative_to(REPO)

    # Prune excluded dirs
    dirs[:] = [d for d in sorted(dirs) if d not in EXCLUDE_DIRS]

    # Skip if any ancestor part is excluded
    if any(part in EXCLUDE_DIRS for part in rel_root.parts):
        dirs[:] = []
        continue

    for fname in sorted(filenames):
        if not is_documentable(fname):
            continue
        rel = (root_path / fname).relative_to(REPO)
        ext = Path(fname).suffix.lower()
        files.append({
            "path": rel.as_posix(),
            "type": "source",
            "language": LANG_MAP.get(ext, "Text"),
            "depth": len(rel.parts) - 1
        })
        parent = rel.parent.as_posix()
        if parent != ".":
            folders.add(parent)

folder_list = [{"path": f, "depth": len(Path(f).parts)} for f in sorted(folders)]
folder_list.sort(key=lambda x: (x["depth"], x["path"]))

plan = {
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "repo_root": str(REPO).replace("\\", "/"),
    "files": files,
    "folders": folder_list,
    "excluded_patterns": sorted(EXCLUDE_DIRS),
    "stats": {
        "total_files": len(files),
        "to_document": len(files),
        "folders": len(folder_list),
    },
}

out_dir = Path(r"c:\Github\Documentation by IA Suite CRM\docs\hierarchical")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "doc-plan.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)

print(f"OK  files={len(files)}  folders={len(folder_list)}")
print("Distribution par profondeur :")
for d, c in sorted(Counter(f["depth"] for f in folder_list).items()):
    print(f"  depth {d}: {c} dossiers")
print("\nDossiers level-1 :")
for f in folder_list:
    if f["depth"] == 1:
        print(f"  {f['path']}")
