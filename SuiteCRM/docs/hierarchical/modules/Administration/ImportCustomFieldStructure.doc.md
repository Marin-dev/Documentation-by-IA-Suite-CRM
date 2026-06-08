# ImportCustomFieldStructure.php

**Chemin :** `modules/Administration/ImportCustomFieldStructure.php`
**Type :** PHP (action / import)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Importe la structure des champs personnalises depuis un fichier `.sugar`. Supprime l'enregistrement existant s'il existe et reinsere le champ via le bean `EditCustomFields`. Appelle ensuite `UpgradeFields.php` pour mettre a jour les tables BDD.

## Role technique
En GET : affiche un formulaire d'upload. En POST (avec fichier) : lit le fichier ligne par ligne, reconstruit chaque enregistrement jusqu'au separateur `DONE`, supprime l'existant et sauvegarde. Compte le total des champs apres import. Inclut `UpgradeFields.php` pour propager les changements.

---

## Dependances cles
| Element | Role |
|---|---|
| `BeanFactory::getBean('EditCustomFields')` | Bean de gestion champs personnalises |
| `modules/Administration/UpgradeFields.php` | Migration des tables apres import |
| `fields_meta_data` | Table cible |

## Symboles principaux
- Aucune classe ni fonction — script d'import

## Interactions
- **Appele par :** `index.php?module=Administration&action=ImportCustomFieldStructure` (lien depuis `Development.php`)
- **Complement :** `ExportCustomFieldStructure.php`
- **Inclut :** `UpgradeFields.php` apres import

---

## Notes
- `$fmd->new_with_id = true` force la creation avec l'ID original du fichier (ligne 68).
- La colonne `table_name` est ignoree a l'import (ligne 78) — elle est recalculee par le bean.
- Le fichier tmp est lu directement via `$_FILES['sugfile']['tmp_name']` — pas de validation du contenu.
