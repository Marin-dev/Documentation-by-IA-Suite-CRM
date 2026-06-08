# includes

## Rôle
Tests unitaires PHPUnit pour les utilitaires de l'espace `include/` de SuiteCRM. Teste les composants transversaux comme la gestion des dates et des fuseaux horaires.

## Contenu
| Fichier | Rôle |
|---|---|
| `TimeDateTest.php` | Tests unitaires de la classe TimeDate (parsing, formatting, fuseaux horaires) |

## Points d'entrée
- `TimeDateTest` — lancé via PHPUnit

## Dépendances clés
- Dépend de : `SuiteCRM/Test/SuitePHPUnitFrameworkTestCase`
- Utilisé par : pipeline CI/CD (suite unit)

## Notes
La gestion des dates est critique dans SuiteCRM (calendriers, activités, rapports).
