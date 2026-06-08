# Interfaces

## Rôle
Ce dossier définit les contrats (interfaces PHP) du sous-système de filtrage JSON:API v1. Il expose six interfaces couvrant les interpréteurs de filtres (par ID, par filtre pré-défini), les opérateurs, les parseurs et les validateurs. Ces interfaces garantissent l'extensibilité du moteur de filtrage sans couplage aux implémentations.

## Contenu
| Fichier | Rôle |
|---|---|
| `ByIdFilterInterpreter.php` | Contrat pour les interpréteurs de filtre par liste d'IDs (`WHERE id IN (...)`) |
| `ByPreMadeFilterInterpreter.php` | Contrat pour les filtres pré-définis nommés (ex : "Today") |
| `HasParserInterface.php` | Contrat pour les classes disposant d'un parseur de filtres |
| `OperatorInterface.php` | Contrat pour les opérateurs de comparaison (méthodes `toFilterOperator()`, `toSqlOperator()`) |
| `ParserInterface.php` | Contrat pour les parseurs de syntaxe filtre JSON:API |
| `ValidatorInterface.php` | Contrat pour les validateurs de filtres |

## Points d'entrée
- `OperatorInterface.php` — interface centrale implémentée par tous les opérateurs
- `ByIdFilterInterpreter.php` — contrat le plus utilisé par `FilterInterpreter`

## Dépendances clés
- **Dépend de :** rien (interfaces pures PHP)
- **Utilisé par :** `lib/API/JsonApi/v1/Filters/Interpreters/`, `lib/API/JsonApi/v1/Filters/Operators/`, `lib/API/JsonApi/v1/Filters/Validators/`

## Notes
- Ce dossier ne contient que des interfaces : aucune logique métier.
- Toute implémentation doit se trouver dans les sous-dossiers frères (Interpreters, Operators, Validators).
