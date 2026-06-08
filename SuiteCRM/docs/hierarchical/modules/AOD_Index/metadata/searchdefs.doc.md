# searchdefs.php

**Chemin :** `modules/AOD_Index/metadata/searchdefs.php`
**Configure :** Formulaires de recherche (basique et avancee) du module AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit `$searchdefs['AOD_Index']` — les champs disponibles dans les formulaires de recherche basique et avancee de la vue liste.

## Parametres cles
| Mode | Champs |
|---|---|
| `basic_search` | `name`, `current_user_only` (filtre utilisateur courant) |
| `advanced_search` | `name`, `assigned_user_id` (liste utilisateurs) |

Layout : 3 colonnes max, 4 en basique.

## Impacte par / impacte
- Charge par le framework SugarCRM pour le rendu des formulaires de recherche de la liste
- Reference dans `metafiles.php`

## Points d'attention
- RAS — configuration standard de recherche.
