# listviewdefs.php (configuration)

**Chemin :** `modules/Bugs/metadata/listviewdefs.php`
**Configure :** Vue liste du module Bugs
**Derniere mise a jour doc :** 2026-05-31

## Ce que ce fichier configure
Definit les colonnes affichees dans la vue liste du module Bugs : ordre, largeur, label, tri et liens.

## Parametres cles
| Parametre | Effet |
|---|---|
| `$listViewDefs['Bugs']` | Tableau des colonnes de la liste Bugs |
| Colonnes typiques | bug_number, name, status, priority, assigned_user_name, date_modified |

## Impacte par / impacte
- Consomme par le framework SuiteCRM lors du rendu `action=index`
- Peut etre surcharge par `custom/modules/Bugs/metadata/listviewdefs.php`

## Notes
- Fichier purement declaratif.
