# Enumerator

## Rôle
Ce dossier regroupe les classes d'énumération (constantes) de la couche JSON:API v1. Ces classes centralisent les valeurs constantes utilisées dans le système JSON:API : types de liens, types de relations, codes de ressources, types de relations SugarBean. Elles facilitent la maintenance et évitent les chaînes magiques dans le code.

## Contenu
| Fichier | Rôle |
|---|---|
| `LinksMessage.php` | Messages d'erreur pour la validation des URLs dans l'objet `Links` |
| `RelationshipType.php` | Constantes des types de relation JSON:API (to-one, to-many) |
| `ResourceEnum.php` | Constantes de types de ressources JSON:API (`data`, `included`, etc.) |
| `SugarBeanRelationshipType.php` | Constantes des types de relations SugarCRM (`one_to_one`, `one_to_many`, `many_to_many`) |

## Points d'entrée
- `RelationshipType.php` — utilisé dans `SuiteBeanResource` pour déterminer le type de relation
- `SugarBeanRelationshipType.php` — utilisé dans `RelationshipRepository`

## Dépendances clés
- **Dépend de :** rien (classes statiques de constantes)
- **Utilisé par :** `lib/API/JsonApi/v1/Resource/SuiteBeanResource`, `lib/API/JsonApi/v1/Repositories/RelationshipRepository`, `lib/API/JsonApi/v1/Links`

## Notes
- Toutes ces classes sont des conteneurs de constantes statiques — aucune logique.
- `SugarBeanRelationshipType` fait le pont entre les concepts SuiteCRM et JSON:API.
