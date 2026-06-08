# metafiles.php

**Chemin :** `modules/AOD_Index/metadata/metafiles.php`
**Configure :** Registre des fichiers de metadonnees du module AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Declare `$metafiles['AOD_Index']` — le mapping entre les types de vues/definitions et leurs fichiers PHP correspondants. Permet au framework SugarCRM de localiser les metadonnees du module.

## Parametres cles
| Cle | Fichier pointe |
|---|---|
| `detailviewdefs` | `modules/AOD_Index/metadata/detailviewdefs.php` |
| `editviewdefs` | `modules/AOD_Index/metadata/editviewdefs.php` |
| `listviewdefs` | `modules/AOD_Index/metadata/listviewdefs.php` |
| `searchdefs` | `modules/AOD_Index/metadata/searchdefs.php` |
| `popupdefs` | `modules/AOD_Index/metadata/popupdefs.php` |
| `searchfields` | `modules/AOD_Index/metadata/SearchFields.php` |

## Impacte par / impacte
- Consomme par le framework SugarCRM lors du chargement des vues du module

## Points d'attention
- RAS — fichier de registre pur, aucune logique.
