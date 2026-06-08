# data

## Rôle
Tests unitaires PHPUnit pour la couche données de SuiteCRM. Teste les classes core de manipulation des beans (`SugarBean`) et de la factory de beans (`BeanFactory`).

## Contenu
| Fichier | Rôle |
|---|---|
| `BeanFactoryTest.php` | Tests unitaires de BeanFactory (instanciation, cache, gestion des beans) |
| `SugarBeanTest.php` | Tests unitaires de SugarBean (méthodes CRUD, vardefs, relations) |

## Points d'entrée
- `BeanFactoryTest` et `SugarBeanTest` — lancés via PHPUnit

## Dépendances clés
- Dépend de : `SuiteCRM/Test/BeanFactoryTestCase`, `SuiteCRM/Test/SuitePHPUnitFrameworkTestCase`
- Utilisé par : pipeline CI/CD (suite unit)

## Notes
Tests des composants fondamentaux du framework SuiteCRM — haute valeur critique.
