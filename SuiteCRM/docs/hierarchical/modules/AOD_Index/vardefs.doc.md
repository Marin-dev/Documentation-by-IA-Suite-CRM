# vardefs.php

**Chemin :** `modules/AOD_Index/vardefs.php`
**Type :** PHP — Configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit le schema de la table `aod_index` et les metadonnees ORM du module AOD_Index. Declare deux champs specifiques (`last_optimised`, `location`) en plus des champs standards injectes par `VardefManager::createVardef` avec les templates `basic` et `assignable`.

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `table` | `aod_index` | Nom de la table SQL |
| `audited` | `true` | Les modifications sont auditees |
| `unified_search` | `false` | Le module n'est pas inclus dans la recherche unifiee |
| `optimistic_locking` | `true` | Verrouillage optimiste active |
| `last_optimised` | `datetimecombo` | Date de la derniere optimisation de l'index |
| `location` | `varchar(255)` | Chemin physique du repertoire de l'index Lucene |
| `disable_row_level_security` | (via `AOD_Index_sugar`) | Securite par lignes desactivee |

## Impacte par / impacte
- Consomme par `VardefManager` au chargement du module
- Templates appliques : `basic` (id, name, dates, description, deleted, etc.) + `assignable` (assigned_user_id)
- Lu par `AOD_Index_sugar` via le systeme ORM SugarCRM

## Points d'attention
- Le champ `location` stocke le chemin de l'index sur le filesystem — sensible en termes de securite si expose.
- `unified_search: false` confirme que AOD_Index lui-meme n'est pas indexable.
