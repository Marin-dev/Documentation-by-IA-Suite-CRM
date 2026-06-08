# listviewdefs.php

**Chemin :** `modules/AOD_Index/metadata/listviewdefs.php`
**Configure :** Colonnes de la vue liste du module AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit `$listViewDefs['AOD_Index']` — les colonnes affichees dans la vue liste du module. Seules deux colonnes sont configurees : le nom (avec lien) et l'utilisateur assigne.

## Parametres cles
| Colonne | Label | Lien | Defaut |
|---|---|---|---|
| `NAME` | `LBL_NAME` | oui | oui |
| `ASSIGNED_USER_NAME` | `LBL_ASSIGNED_TO_NAME` | non | oui |

## Impacte par / impacte
- Charge par le framework SugarCRM pour le rendu de la liste du module
- Surcharge possible via `custom/modules/AOD_Index/metadata/listviewdefs.php`
- Declare dans `metafiles.php`

## Points d'attention
- Vue liste tres minimaliste (2 colonnes) — coherent avec le fait que le module est essentiellement un singleton technique.
