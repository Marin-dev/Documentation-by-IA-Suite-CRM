# en_us.lang.php (jjwg_Areas)

**Chemin :** `modules/jjwg_Areas/language/en_us.lang.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Fichier de langue anglaise du module jjwg_Areas. Definit toutes les chaines de texte affichees dans l'interface utilisateur pour le module Zones geographiques.

**Type :** config (langue)

---

## Dependances cles
- Aucune (fichier de donnees pur)

## Exports / Symboles principaux

Tableau `$mod_strings` avec les cles notables :

| Cle | Valeur | Usage |
|---|---|---|
| `LBL_MODULE_NAME` | `'Areas'` | Nom du module |
| `LBL_COORDINATES` | `'Coordinates'` | Libelle du champ coordonnees |
| `LBL_AREA_MAP` | `'Area Map'` | Titre de la page carte |
| `LBL_AREA_EDIT_TITLE` | `'Area Creation Instructions:'` | Titre instructions edition carte |
| `LBL_AREA_EDIT_DESC_1` | Instructions creation polygone | Affiche dans view.area_edit_map |
| `LBL_AREA_EDIT_USE_AREA_COORDINATES` | `'Use Area Coordinates'` | Bouton export coordonnees |
| `LNK_NEW_RECORD` | `'Create Areas'` | Lien menu creation |
| `LNK_LIST` | `'View Areas'` | Lien menu liste |

## Interactions
- **Appele par :** systeme de traduction SuiteCRM (`return_module_language()`), vues du module, Menu.php, dashlet
- **Appelle :** rien

## Notes
- Ce fichier est charge automatiquement par le framework SuiteCRM selon la langue courante.
- Contient aussi les labels des instructions de dessin de polygone affiches dans view.area_edit_map.php.
