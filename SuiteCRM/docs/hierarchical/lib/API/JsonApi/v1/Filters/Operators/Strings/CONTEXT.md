# Strings

## Rôle
Ce dossier regroupe les opérateurs de correspondance textuelle pour les filtres JSON:API v1. Il propose les opérateurs LIKE et NOT LIKE permettant les recherches partielles sur des champs texte. Ces opérateurs sont utilisés pour les recherches type "contient" ou "ne contient pas".

## Contenu
| Fichier | Rôle |
|---|---|
| `LikeOperator.php` | Opérateur `[[li]]` → SQL `LIKE` (recherche partielle de texte) |
| `NotLikeOperator.php` | Opérateur `[[nli]]` → SQL `NOT LIKE` (exclusion partielle de texte) |

## Points d'entrée
- `LikeOperator.php` — opérateur de recherche textuelle principale

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Operators/Operator` (classe parente), `lib/API/JsonApi/v1/Filters/Interfaces/OperatorInterface`
- **Utilisé par :** container DI `FilterOperators`, consommé par `FilterParser` et `FilterInterpreter`

## Notes
- Les jokers SQL (`%`, `_`) doivent être fournis par le client dans la valeur de l'opérande — non ajoutés automatiquement.
- Complémentaire aux opérateurs de `Comparators/` pour les champs textuels.
