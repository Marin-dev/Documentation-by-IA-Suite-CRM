# v1

## Rôle
Ce dossier implémente la version 1 de la couche JSON:API de SuiteCRM. Il fournit l'ensemble des composants pour construire, valider et sérialiser des réponses conformes à la spec JSON:API 1.0 : objets `JsonApi` et `Links` racines, modèles de ressources, relations, filtres, repositories et énumérations. C'est la bibliothèque JSON:API centrale utilisée par les contrôleurs de l'API v8.

## Contenu
| Dossier/Fichier | Rôle |
|---|---|
| `JsonApi.php` | Objet racine JSON:API — version 1.0 et schéma de validation |
| `Links.php` | Objet `links` JSON:API — validation et construction des URLs |
| `Enumerator/` | Constantes : types de liens, types de relations, codes de ressources |
| `Filters/` | Pipeline complet de filtrage : interfaces, parseurs, validateurs, opérateurs, interpréteurs SQL |
| `Interfaces/` | Contrats d'identification et de réponse JSON:API |
| `Repositories/` | Façades pour le filtrage et les relations |
| `Resource/` | Modèles de ressources et adaptateur SugarBean ↔ JSON:API |

## Points d'entrée
- `JsonApi.php` — objet racine, injecté dans `ApiController`
- `Resource/SuiteBeanResource.php` — adaptateur central SugarBean ↔ JSON:API
- `Filters/Parsers/FilterParser.php` et `Filters/Interpreters/FilterInterpreter.php` — pipeline de filtrage

## Dépendances clés
- **Dépend de :** `lib/API/v8/Exception/`, container DI Slim, `\BeanFactory`, `DBManager`, `league/uri`
- **Utilisé par :** `lib/API/v8/Controller/ModuleController`, `lib/API/v8/Library/ModulesLib`

## Notes
- `FilterValidator.isValid()` retourne toujours `true` — dette technique documentée.
- Bug potentiel ligne 409 de `SuiteBeanResource` (variable hors portée).
- Le schéma JSON Schema de validation est dans ce dossier (`schema.json` — présence non confirmée).
