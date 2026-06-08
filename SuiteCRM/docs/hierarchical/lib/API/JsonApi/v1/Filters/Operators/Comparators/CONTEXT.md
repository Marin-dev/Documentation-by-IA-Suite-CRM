# Comparators

## Rôle
Ce dossier regroupe les opérateurs de comparaison numérique et d'égalité pour les filtres JSON:API v1. Chaque classe mappe un token de filtre API (syntaxe `[[op]]`) vers son équivalent SQL. Ils couvrent l'égalité, l'inégalité, les comparaisons supérieur/inférieur et les opérateurs d'appartenance à un ensemble.

## Contenu
| Fichier | Rôle |
|---|---|
| `EqualsOperator.php` | Opérateur `[[eq]]` → SQL `=` |
| `NotEqualsOperator.php` | Opérateur `[[ne]]` → SQL `!=` |
| `GreaterThanOperator.php` | Opérateur `[[gt]]` → SQL `>` |
| `GreaterThanOrEqualsOperator.php` | Opérateur `[[gte]]` → SQL `>=` |
| `LessThanOperator.php` | Opérateur `[[lt]]` → SQL `<` |
| `LessThanOrEqualsOperator.php` | Opérateur `[[lte]]` → SQL `<=` |
| `InOperator.php` | Opérateur `[[in]]` → SQL `IN (...)` |
| `NotInOperator.php` | Opérateur `[[nin]]` → SQL `NOT IN (...)` |

## Points d'entrée
- `EqualsOperator.php` — opérateur le plus courant
- `InOperator.php` / `NotInOperator.php` — opérateurs pour les listes de valeurs

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Operators/Operator` (classe parente), `lib/API/JsonApi/v1/Filters/Interfaces/OperatorInterface`
- **Utilisé par :** container DI `FilterOperators`, consommé par `FilterParser` et `FilterInterpreter`

## Notes
- Toutes les classes suivent le même pattern : étendent `Operator`, implémentent `OperatorInterface`, et exposent `toFilterOperator()` et `toSqlOperator()`.
- Aucune logique SQL générée directement ici : ces classes sont des value objects retournant uniquement les tokens.
