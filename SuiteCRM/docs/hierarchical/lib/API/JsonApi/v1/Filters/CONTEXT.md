# Filters

## Rôle
Ce dossier constitue le sous-système complet de filtrage de l'API JSON:API v1 de SuiteCRM. Il implémente le pipeline de traitement des filtres de requête HTTP : définition des contrats (Interfaces), parsing de la syntaxe (Parsers), validation (Validators), opérateurs SQL (Operators), et interprétation vers SQL WHERE (Interpreters). Ce pipeline permet aux clients API de filtrer les ressources avec une syntaxe riche et extensible.

## Contenu
| Dossier | Rôle |
|---|---|
| `Interfaces/` | Contrats PHP (interfaces) pour tous les composants de filtrage |
| `Parsers/` | Parseur de la syntaxe filtre HTTP vers structure interne |
| `Validators/` | Validateurs de champs, opérateurs et valeurs |
| `Operators/` | Opérateurs de comparaison et textuels (value objects) |
| `Interpreters/` | Conversion des filtres parsés en clauses SQL WHERE |

## Points d'entrée
- `Parsers/FilterParser.php` — première étape du pipeline, appelée par `FilterRepository`
- `Interpreters/FilterInterpreter.php` — deuxième étape, produit le SQL final

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Interfaces/`, container DI (`FilterOperators`, `FilterFieldOperators`, etc.), `DBManager`, `\BeanFactory`
- **Utilisé par :** `lib/API/JsonApi/v1/Repositories/FilterRepository.php`, contrôleurs `lib/API/v8/`

## Notes
- Pipeline en deux étapes : Parse → Interpret (SQL).
- `FilterValidator.isValid()` retourne toujours `true` — dette technique documentée.
- Import suspect de `Behat\Gherkin` dans `FilterInterpreter` (code de production).
