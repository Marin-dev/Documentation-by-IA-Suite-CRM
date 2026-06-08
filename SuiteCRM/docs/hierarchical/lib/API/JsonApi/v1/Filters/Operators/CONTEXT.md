# Operators

## Rôle
Ce dossier regroupe tous les opérateurs de filtre JSON:API v1. Chaque opérateur mappe un token de filtre API (syntaxe `[[op]]`) vers son équivalent SQL. Il distingue les opérateurs de comparaison numérique (`Comparators/`), les opérateurs textuels (`Strings/`), et les classes de base pour les opérateurs de champs et spéciaux.

## Contenu
| Fichier/Dossier | Rôle |
|---|---|
| `Operator.php` | Classe abstraite de base pour tous les opérateurs |
| `FieldOperator.php` | Opérateur sur champ de bean — encapsule le nom du champ cible |
| `SpecialOperator.php` | Opérateurs logiques spéciaux (`[[and]]`, `[[or]]`) |
| `Comparators/` | Opérateurs de comparaison : `[[eq]]`, `[[ne]]`, `[[gt]]`, `[[gte]]`, `[[lt]]`, `[[lte]]`, `[[in]]`, `[[nin]]` |
| `Strings/` | Opérateurs de correspondance textuelle : `[[li]]` (LIKE), `[[nli]]` (NOT LIKE) |

## Points d'entrée
- `FieldOperator.php` — utilisé dans `FilterInterpreter` pour les filtres par attribut
- `Comparators/EqualsOperator.php` — opérateur le plus courant

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Interfaces/OperatorInterface`
- **Utilisé par :** container DI (`FilterOperators`, `FilterFieldOperators`, `FilterSpecialOperators`), `FilterParser`, `FilterInterpreter`

## Notes
- Toutes les classes d'opérateurs sont des value objects — aucune logique SQL générée directement.
- La liste des opérateurs enregistrés dans le container détermine les filtres acceptés par l'API.
