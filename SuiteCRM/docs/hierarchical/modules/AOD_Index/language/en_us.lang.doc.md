# en_us.lang.php

**Chemin :** `modules/AOD_Index/language/en_us.lang.php`
**Configure :** Chaines de traduction anglaises du module AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Declare le tableau `$mod_strings` contenant toutes les chaines de traduction anglaises (en-US) du module AOD_Index. Couvre les labels generiques (champs ORM), les labels specifiques aux stats d'index et les labels de l'interface de recherche AOD.

## Parametres cles
| Cle | Valeur | Usage |
|---|---|---|
| `LBL_LAST_OPTIMISED` | `'Last Optimised'` | Affichage date optimisation |
| `LBL_LOCATION` | `'Location'` | Champ chemin de l'index |
| `LBL_INDEX_STATS` | `'Index stats'` | Titre section stats |
| `LBL_OPTIMISE_NOW` | `'Optimise now'` | Bouton optimisation manuelle |
| `LBL_TOTAL_RECORDS` | `'Total records'` | Stat total |
| `LBL_INDEXED_RECORDS` | `'Indexed records'` | Stat indexes |
| `LBL_FAILED_RECORDS` | `'Failed records'` | Stat echecs |
| `LBL_INDEX_FILES` | `'Index file count'` | Stat fichiers .cfs |
| `LBL_SEARCH_QUERY_PLACEHOLDER` | `'Enter search...'` | Placeholder champ recherche |
| `LBL_USE_AOD_SEARCH` | `'Use Advanced Search'` | Toggle recherche AOD |

## Impacte par / impacte
- Charge par le framework SugarCRM au rendu de tout ecran du module `AOD_Index`
- Consomme par `view.indexdata.php` (via `$GLOBALS['mod_strings']`) et les templates Smarty

## Points d'attention
- Aucune traduction FR incluse dans le module — la localisation francaise serait dans un fichier `fr_FR.lang.php` absent du perimetre analyse.
