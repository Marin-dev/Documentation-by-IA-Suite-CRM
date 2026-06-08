# view.backups.php

**Chemin :** `modules/Administration/views/view.backups.php`
**Type :** PHP (view MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de sauvegarde ZIP de l'installation SuiteCRM. Permet a l'administrateur de specifier un repertoire de destination et un nom de fichier ZIP, puis de lancer la compression de toute l'installation.

## Role technique
Etend `SugarView`. `process()` : en POST, sauvegarde si `run=confirm` (validation) puis `run=confirmed` (execution via `zip_dir(".", "$backup_dir/$backup_zip")`). Affiche un formulaire HTML inline si non termine. Deux verifications de securite : `is_admin()` et `$sugar_config['hide_admin_backup']`.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/utils/php_zip_utils.php` | `zip_dir()` pour la compression |

## Symboles principaux
- `ViewBackups extends SugarView` — classe view

## Interactions
- **Appele par :** `index.php?module=Administration&action=Backups`

---

## Notes
- `ini_set("memory_limit", "-1")` et `max_execution_time=0` pendant la compression — peut utiliser beaucoup de ressources.
- Securite : verifie que `backup_dir` ne contient pas `phar://` (ligne 98).
- La sauvegarde est une simple compression du repertoire courant `.` — inclut potentiellement des donnees sensibles.
