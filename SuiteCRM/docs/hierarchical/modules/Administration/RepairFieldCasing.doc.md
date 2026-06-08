# RepairFieldCasing.php

**Chemin :** `modules/Administration/RepairFieldCasing.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Repare la casse des noms de champs personnalises. Detecte les champs dans `fields_meta_data` dont le nom n'est pas en minuscules, corrige en BDD (UPDATE fields_meta_data + renommage colonne dans la table `_cstm`), et met a jour les layouts de vues (editview, detailview, etc.) via `ParserFactory`.

## Role technique
Requete `SELECT * FROM fields_meta_data`, filtre les lignes ou `name != strtolower(name)`. Pour chaque module affecte : UPDATE BDD + `renameColumnSQL()`, puis iteration sur les vues `basic_search`, `advanced_search`, `detailview`, `editview`, `quickcreate` via `ParserFactory::getParser()`. Vide le cache vardefs via `RepairAndClear::clearVardefs()`.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/TemplateHandler/TemplateHandler.php` | Nettoyage cache templates |
| `modules/ModuleBuilder/parsers/ParserFactory.php` | Parseurs de vues layout |
| `QuickRepairAndRebuild.php` | Nettoyage vardefs cache |

## Notes
- Script destructif sur les colonnes BDD — renomme les colonnes des tables `*_cstm`.
- Capture les exceptions `ParserFactory::getParser()` et loggue en fatal sans arreter le processus.
