# IndexingLockFileTrait.php

**Chemin :** `lib/Search/Index/IndexingLockFileTrait.php`
**Type :** PHP — Trait
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Trait fournissant la gestion des fichiers lock pour l'indexation differentielle. Enregistre l'heure de la derniere indexation dans un fichier de lock et le relit au prochain demarrage.

## Role technique
Fichier lock nomme `cache/{ClassName}.lock`. Contient un timestamp UNIX en entier. Lit et ecrit via `file_get_contents/file_put_contents`. Utilise `Carbon` pour les conversions de timestamp.

---

## Dependances cles
- `Carbon\Carbon`
- `Monolog\Logger` (propriete `$this->logger` attendue)

## Exports / Symboles principaux
- `IndexingLockFileTrait` — trait
  - `readLockFile(): Carbon|false` (private)
  - `writeLockFile(): void` (private)
  - `formatInterval(float $seconds): string` (protected) — human readable (ex: "2h 30m 5s")

- **Consommateurs :** `ElasticSearchIndexer`

---

## Points d'attention
- Chemin lock : `cache/{ClassName}.lock` — le dossier `cache/` doit etre accessible en ecriture.
- Si le fichier lock n'existe pas ou est illisible, `readLockFile()` retourne `false` (indexation complete).
