# Search

## Rôle
Tests unitaires PHPUnit pour le moteur de recherche SuiteCRM (`lib/SuiteCRM/Search/`). Vérifie le comportement du `SearchWrapper` et des stratégies de recherche en isolation.

## Contenu
| Fichier | Rôle |
|---|---|
| `SearchWrapperTest.php` | Tests unitaires du SearchWrapper (wrapper unifié des moteurs de recherche) |

## Points d'entrée
- `SearchWrapperTest` — lancé via PHPUnit

## Dépendances clés
- Dépend de : `SuiteCRM/Test/SuitePHPUnitFrameworkTestCase`, `lib/SuiteCRM/Search/SearchWrapper`
- Utilisé par : pipeline CI/CD (suite unit)

## Notes
Correspond au module de recherche avancée de SuiteCRM (ElasticSearch / recherche native).
