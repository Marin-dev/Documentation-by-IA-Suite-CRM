# Repositories

## Rôle
Ce dossier contient les repositories de la couche JSON:API v1 — les classes qui orchestrent la récupération et la construction des ressources JSON:API depuis les données SuiteCRM. `FilterRepository` pilote le pipeline de filtrage (parse + interprétation SQL), `RelationshipRepository` gère la lecture des relations entre beans.

## Contenu
| Fichier | Rôle |
|---|---|
| `FilterRepository.php` | Orchestre le pipeline filter : parse la requête HTTP via `FilterParser`, puis interprète en SQL via `FilterInterpreter` |
| `RelationshipRepository.php` | Lit les relations entre beans SuiteCRM et les structure en objets `Relationship` JSON:API |

## Points d'entrée
- `FilterRepository.php` — point d'entrée des filtres, appelé depuis les contrôleurs v8
- `RelationshipRepository.php` — appelé lors de la construction des ressources avec relations

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Parsers/FilterParser`, `lib/API/JsonApi/v1/Filters/Interpreters/FilterInterpreter`, `lib/API/JsonApi/v1/Resource/Relationship`, `\BeanFactory`
- **Utilisé par :** `lib/API/v8/Controller/ModuleController.php`, `lib/API/JsonApi/v1/Resource/SuiteBeanResource.php`

## Notes
- `FilterRepository` est la façade principale du système de filtrage — masque la complexité du pipeline Parse/Interpret.
- `RelationshipRepository` lit les `field_defs` du bean pour déterminer les relations disponibles.
