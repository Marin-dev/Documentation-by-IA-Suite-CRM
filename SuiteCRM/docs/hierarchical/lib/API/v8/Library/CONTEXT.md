# Library

## Rôle
Ce dossier contient les bibliothèques utilitaires de l'API v8 de SuiteCRM. `ModulesLib` fournit la logique de pagination, tri et filtrage pour les listes de modules ; `UtilityLib` regroupe des utilitaires partagés entre contrôleurs. Ces classes évitent la duplication de logique dans les contrôleurs.

## Contenu
| Fichier | Rôle |
|---|---|
| `ModulesLib.php` | Gestion des listes paginées de beans : pagination, tri SQL, filtrage JSON:API, construction des liens de navigation |
| `UtilityLib.php` | Utilitaires généraux pour les contrôleurs API v8 |

## Points d'entrée
- `ModulesLib.php` — injecté dans `ModuleController` via le container DI

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/`, `lib/API/JsonApi/v1/Resource/SuiteBeanResource`, `lib/API/JsonApi/v1/Links`, `League\Uri`, `SugarBean::get_list()`, container DI
- **Utilisé par :** `lib/API/v8/Controller/ModuleController.php`

## Notes
- Bug potentiel ligne 352 de `ModulesLib` : `$pagination['page']['limit'] = $offset` au lieu de `$limit`.
- `getCurrentUser()` lit `oauth_user_id` depuis les attributs de la requête (injecté par le middleware OAuth2).
- Trois stratégies de filtre supportées : ByPreMadeName, ById, ByAttributes.
