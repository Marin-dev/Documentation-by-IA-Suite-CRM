# Resource

## Rôle
Ce dossier contient les classes de modèle de ressource JSON:API v1. Il définit la structure des ressources (Resource, ResourceIdentifier), leurs relations (Relationship), et l'adaptateur clé `SuiteBeanResource` qui fait le pont bidirectionnel entre un SugarBean SuiteCRM et la représentation JSON:API. Ce dossier est au cœur de la sérialisation/désérialisation de l'API.

## Contenu
| Fichier | Rôle |
|---|---|
| `Resource.php` | Classe de base représentant une ressource JSON:API (type, id, attributes, relationships, links) |
| `ResourceIdentifier.php` | Implémente `JsonApiResourceIdentifier` — référence légère à une ressource (type + id uniquement) |
| `Relationship.php` | Représente une relation JSON:API entre deux ressources (to-one ou to-many) |
| `SuiteBeanResource.php` | Adaptateur bidirectionnel SugarBean ↔ JSON:API — lecture ET écriture en BD |

## Points d'entrée
- `SuiteBeanResource.php` — classe la plus importante, point d'entrée pour toute conversion bean ↔ JSON:API
- `Resource.php` — classe de base étendue par `SuiteBeanResource`

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Interfaces/`, `lib/API/JsonApi/v1/Repositories/RelationshipRepository`, `lib/API/JsonApi/v1/Links`, `\BeanFactory`, `\UploadFile`, container DI
- **Utilisé par :** `lib/API/v8/Controller/ModuleController.php`, contrôleurs API v8

## Notes
- `SuiteBeanResource::toSugarBean()` appelle `$sugarBean->save()` — effet de bord direct en BD.
- Bug potentiel ligne 409 de `SuiteBeanResource` : variable `$toManyRelationship` utilisée hors portée.
- Les fichiers binaires sont encodés/décodés en base64 — risque mémoire avec les fichiers volumineux.
