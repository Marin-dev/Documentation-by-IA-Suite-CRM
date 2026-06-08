# Validators

## Rôle
Ce dossier regroupe les validateurs du sous-système de filtrage JSON:API v1. Chaque classe valide un aspect spécifique d'un filtre de requête : la valeur, le champ, l'opérateur, l'opérateur spécial ou le filtre dans son ensemble. Ils sont utilisés par `FilterParser` pour rejeter les requêtes invalides avant interprétation SQL.

## Contenu
| Fichier | Rôle |
|---|---|
| `FieldValidator.php` | Valide le nom de champ dans la clé de filtre |
| `FilterValidator.php` | Valide la valeur du filtre — retourne toujours `true` (implémentation partielle, dette technique) |
| `OperatorValidator.php` | Valide qu'un opérateur est reconnu dans la liste `FilterOperators` |
| `SpecialOperatorValidator.php` | Valide les opérateurs spéciaux (`[[and]]`, `[[or]]`, etc.) |
| `ValueValidator.php` | Valide la valeur associée à un opérateur |

## Points d'entrée
- `FilterValidator.php` — validateur d'entrée, appelé en premier par `FilterParser`
- `OperatorValidator.php` — validation critique des opérateurs

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Interfaces/ValidatorInterface`
- **Utilisé par :** `lib/API/JsonApi/v1/Filters/Parsers/FilterParser.php`

## Notes
- `FilterValidator.isValid()` retourne toujours `true` — dette technique avérée (logique commentée dans le code).
- La validation effective repose principalement sur `OperatorValidator` et `FieldValidator`.
