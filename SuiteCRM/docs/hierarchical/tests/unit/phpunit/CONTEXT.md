# phpunit

## Rôle
Tests unitaires PHPUnit de SuiteCRM. Organisé en sous-dossiers reflétant la structure du code source (data, includes, include/, lib/). Couvre les composants fondamentaux : BeanFactory, SugarBean, TimeDate, CalendarSync et SearchWrapper.

## Contenu
| Dossier | Rôle |
|---|---|
| `data/` | Tests des classes de données core (BeanFactory, SugarBean) |
| `includes/` | Tests des utilitaires include (TimeDate) |
| `include/` | Tests des modules de `include/` (CalendarSync) |
| `lib/` | Tests des bibliothèques `lib/SuiteCRM/` (Search) |

## Points d'entrée
Lancés via `vendor/bin/phpunit` avec la configuration `phpunit.xml` du projet.

## Dépendances clés
- Dépend de : PHPUnit, `SuiteCRM/Test/SuitePHPUnitFrameworkTestCase`, SuiteCRM core
- Utilisé par : pipeline CI/CD (suite unit)

## Notes
Tests rapides (sans navigateur, sans déploiement complet) — exécutés en priorité dans le pipeline CI.
