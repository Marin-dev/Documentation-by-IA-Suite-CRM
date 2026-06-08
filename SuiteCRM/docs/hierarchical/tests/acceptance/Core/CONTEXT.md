# Core

## Rôle
Tests d'acceptation des templates de modules SuiteCRM Core. Vérifie le comportement CRUD générique pour chaque type de template SugarObject (Basic, Company, File, Issue, Person, Sale) ainsi que les fonctionnalités du Module Builder (champs personnalisés).

## Contenu
| Fichier | Rôle |
|---|---|
| `BasicModuleCest.php` | Tests d'acceptation pour les modules de type Basic |
| `CompanyModuleCest.php` | Tests d'acceptation pour les modules de type Company |
| `FileModuleCest.php` | Tests d'acceptation pour les modules de type File |
| `IssueModuleCest.php` | Tests d'acceptation pour les modules de type Issue |
| `PersonModuleCest.php` | Tests d'acceptation pour les modules de type Person |
| `SaleModuleCest.php` | Tests d'acceptation pour les modules de type Sale |
| `ModuleBuilderFieldsCest.php` | Tests d'acceptation pour la création de champs personnalisés via Module Builder |

## Points d'entrée
Lancés par Codeception suite `acceptance` — correspondent aux templates `include/SugarObjects/templates/`.

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Page/*Module.php`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD pour validation des templates de modules

## Notes
Un Cest par template SugarObject — cohérence avec la hiérarchie `include/SugarObjects/templates/`.
