# editviewdefs.php

**Chemin :** `modules/AOD_Index/metadata/editviewdefs.php`
**Configure :** Mise en page de la vue edition du module AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit `$viewdefs['AOD_Index']['EditView']` — la structure du formulaire d'edition. Panneau unique avec `name`, `assigned_user_name` et `description`. Layout 2 colonnes.

## Parametres cles
| Panneau | Champs |
|---|---|
| `default` | `name`, `assigned_user_name`, `description` |

## Impacte par / impacte
- Charge par le framework MVC SugarCRM pour le rendu de `EditView`
- Reference dans `metafiles.php`

## Points d'attention
- RAS — formulaire d'edition minimal, coherent avec l'usage technique du module.
