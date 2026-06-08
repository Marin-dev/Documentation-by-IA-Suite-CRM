# SearchFields.php

**Chemin :** `modules/AOD_Index/metadata/SearchFields.php`
**Configure :** Champs de recherche SQL du module AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit `$searchFields['AOD_Index']` — le mapping entre les champs du formulaire de recherche et leur comportement SQL. Inclut le support des plages de dates pour `date_entered` et `date_modified`.

## Parametres cles
| Champ | Type requete | Particularite |
|---|---|---|
| `name` | `default` | Recherche par nom |
| `current_user_only` | `default` | Filtre sur `assigned_user_id` de l'utilisateur courant |
| `assigned_user_id` | `default` | Filtre par utilisateur assigne |
| `range_date_entered` | `default` | Plage de dates de creation |
| `range_date_modified` | `default` | Plage de dates de modification |

## Impacte par / impacte
- Consomme par le moteur de recherche SugarCRM (`SearchForm`) pour construire les requetes SQL
- Reference dans `metafiles.php`

## Points d'attention
- RAS — configuration standard avec support range search.
