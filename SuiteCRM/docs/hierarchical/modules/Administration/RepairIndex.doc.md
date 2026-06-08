# RepairIndex.php

**Chemin :** `modules/Administration/RepairIndex.php`
**Type :** PHP (action / maintenance BDD)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Compare les index BDD reels avec ceux definis dans les vardefs. Identifie les index a ajouter, supprimer ou renommer, et permet leur correction en mode execution. Couvre les beans ET les tables de relation (TableDictionary).

## Role technique
Script procedral avec fonction utilitaire `compare()`. Itere sur `$beanFiles` et `TableDictionary`, compare les index via `DBManager::get_indices()`. Construit trois listes : `$add_index`, `$drop_index`, `$change_index`. En mode `execute`, applique les requetes SQL via `$focus->db->query()`.

---

## Symboles principaux

| Fonction | Role |
|---|---|
| `compare($table_name, $db_indexes, $var_indexes)` | Compare index BDD vs vardefs, remplit add/drop/change |

## Interactions
- **Appele par :** `index.php?module=Administration&action=RepairIndex`, `ModuleInstaller::repair_indices()` (via `$_REQUEST['silent']`)
- **Appelle :** `DBManagerFactory::getInstance()->add_drop_constraint()`, `renameIndexDefs()`

---

## Notes
- Ignore les index de type `fulltext` (ligne 159).
- Le mode silencieux (`$_REQUEST['silent']`) est utilise par `ModuleInstaller` — supprimer le HTML.
- `set_time_limit(3600)`.
