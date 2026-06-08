# ByIdFilters

## Rôle
Ce dossier contient l'implémentation du filtre par identifiants pour l'API JSON:API v1. Il transforme une liste d'IDs fournie dans le paramètre de filtre `[id]` en clause SQL `id IN (...)`. C'est le mécanisme permettant de récupérer un ensemble précis d'enregistrements par leurs identifiants.

## Contenu
| Fichier | Rôle |
|---|---|
| `ByIdFilter.php` | Implémente `ByIdFilterInterpreter` — génère `id IN ("id1","id2",...)` via `DBManager::quote()` |

## Points d'entrée
- `ByIdFilter.php` — unique fichier, instancié par `FilterInterpreter` via le container DI

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Interfaces/ByIdFilterInterpreter`, `DatabaseManager` (container), `SuiteCRM\Exception\Exception`
- **Utilisé par :** `lib/API/JsonApi/v1/Filters/Interpreters/FilterInterpreter.php`

## Notes
- Les IDs vides dans la liste sont silencieusement ignorés.
- Lève `Exception` si la structure de filtre est vide.
- L'injection du `DBManager` via le container garantit l'échappement SQL sécurisé.
