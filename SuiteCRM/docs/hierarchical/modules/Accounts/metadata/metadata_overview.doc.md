# metadata/ — Vue d'ensemble des fichiers de configuration Accounts

**Chemin :** `modules/Accounts/metadata/`
**Type :** Configuration (metadonnees du module)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Ce repertoire contient toutes les definitions de vues, de recherche, de sous-panneaux et de droits ACL pour le module Accounts. Ces fichiers sont consommes par le framework SuiteCRM pour afficher et controler les formulaires, listes et popups.

## Fichiers et leur role

| Fichier | Variable exportee | Role |
|---|---|---|
| `detailviewdefs.php` | `$viewdefs['Accounts']['DetailView']` | Structure de la vue de detail (panneaux, champs) |
| `editviewdefs.php` | `$viewdefs['Accounts']['EditView']` | Structure du formulaire d'edition |
| `listviewdefs.php` | `$listViewDefs['Accounts']` | Colonnes affichees en vue liste |
| `searchdefs.php` | `$searchdefs['Accounts']` | Champs de recherche basique et avancee |
| `SearchFields.php` | `$searchFields['Accounts']` | Operateurs et types de champs de recherche |
| `popupdefs.php` | `$popupMeta['Accounts']` | Configuration de la popup de selection de compte |
| `quickcreatedefs.php` | `$viewdefs['Accounts']['QuickCreate']` | Vue Quick Create (creation rapide) |
| `subpaneldefs.php` | `$layout_defs['Accounts']` | Definition des sous-panneaux (contacts, oppties, cases...) |
| `additionalDetails.php` | N/A | Details supplementaires pour le survol (hover) |
| `fieldGroups.php` | N/A | Groupes de champs pour l'interface |
| `acldefs.php` | `$acldefs['Accounts']` | Definition des controles ACL sur les formulaires |
| `studio.php` | `$GLOBALS['studioDefs']['Accounts']` | Declarations pour l'outil Studio (vues editables) |
| `metafiles.php` | `$metafiles['Accounts']` | Registre des chemins vers les metafichiers |
| `subpanels/default.php` | N/A | Sous-panneau par defaut pour les relations |
| `subpanels/ForEmails.php` | N/A | Configuration sous-panneau Emails |
| `subpanels/ForProspectLists.php` | N/A | Configuration sous-panneau Prospect Lists |

## Points d'attention
- Tous ces fichiers peuvent etre surcharges dans `custom/modules/Accounts/metadata/` sans modifier le core.
- `studio.php` reference encore des fichiers legacy (DetailView.html, EditView.html) qui peuvent ne plus exister dans les versions recentes de SuiteCRM utilisant le framework MVC.
- `acldefs.php` definit un bouton `btn1` avec `display_option: disabled` qui redirige vers la liste si l'action EditView est tentee sans droits suffisants.
