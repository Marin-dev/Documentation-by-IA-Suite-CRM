# Parsers

## Rôle
Ce dossier contient le parseur de la syntaxe de filtre JSON:API v1. Il est responsable de transformer les paramètres de requête HTTP bruts (ex : `filter[Accounts.name][[eq]]John`) en structures de données internes consommables par `FilterInterpreter`. C'est la première étape du pipeline de traitement des filtres.

## Contenu
| Fichier | Rôle |
|---|---|
| `FilterParser.php` | Parseur principal — décompose clés et valeurs de filtre en arbres `[module][champ][opérateur+valeur]` |

## Points d'entrée
- `FilterParser.php` — unique fichier, consommé par `FilterRepository::fromRequest()`

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Operators/FieldOperator`, `lib/API/JsonApi/v1/Filters/Validators/FieldValidator`, `lib/API/JsonApi/v1/Filters/Validators/FilterValidator`, container DI (`FilterOperators`, `FilterFieldOperators`, `FilterSpecialOperators`), `lib/API/v8/Exception/BadRequestException`
- **Utilisé par :** `lib/API/JsonApi/v1/Repositories/FilterRepository.php`

## Notes
- Supporte les filtres pré-définis nommés (ex : `filter[Today]` sans clé de champ).
- La méthode `stringDifference()` utilise `array_diff` sur les caractères — comportement potentiellement non standard avec UTF-8.
- Propriétés statiques partagées entre instances : à surveiller dans les environnements multi-instances.
