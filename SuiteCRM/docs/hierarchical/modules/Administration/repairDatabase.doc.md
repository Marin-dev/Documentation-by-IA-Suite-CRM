# repairDatabase.php

**Chemin :** `modules/Administration/repairDatabase.php`
**Type :** PHP (action / maintenance BDD)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Repare la structure de la base de donnees en comparant les schemas attendus (vardefs) avec la BDD reelle. Peut etre execute en mode apercu (affiche le SQL) ou en mode execution directe. Supporte aussi l'export SQL.

## Role technique
Script procedral. Itere sur tous les `$beanFiles`, instancie chaque bean, appelle `$db->repairTable()` pour generer le SQL de correction. Traite aussi `TableDictionary.php` (tables de relations). En mode POST avec `raction=execute`, execute les requetes SQL. En mode `raction=export`, envoie le SQL en fichier telechargeable. Affiche via template `templates/RepairDatabase.tpl` si des differences sont trouvees.

---

## Dependances cles
| Element | Role |
|---|---|
| `DBManagerFactory` | Instance BDD |
| `VardefManager::clearVardef()` | Reinitialisation des vardefs |
| `include/modules.php` | $beanFiles |
| `modules/TableDictionary.php` | Tables de relation N-N |
| `DynamicField` | Reparation champs personnalises |
| `Sugar_Smarty` | Template affichage SQL |

## Symboles principaux
- Aucune classe ni fonction — script d'action

## Interactions
- **Inclus par :** `QuickRepairAndRebuild::repairDatabase()` (ligne 140), et `index.php?module=Administration&action=repairDatabase` direct
- **Template :** `modules/Administration/templates/RepairDatabase.tpl`

---

## Notes
- `$execute = false` par defaut — le script genere uniquement le SQL sans l'executer sauf si `$_REQUEST['execute']` est vrai.
- La variable `$from_sync_client` peut bypass le check `is_admin()` (ligne 53) — usage legacy.
- `$reload_vardefs = true` force le rechargement des vardefs pour chaque bean.
- `set_time_limit(3600)` — peut prendre longtemps sur de grosses instances.
