# Page

## Rôle
Page Objects Codeception pour les modules SuiteCRM. Encapsule les sélecteurs CSS/XPath et les URL de chaque module dans des classes dédiées, permettant aux tests d'acceptation d'interagir avec l'UI sans dupliquer les localisateurs.

## Contenu
| Fichier | Rôle |
|---|---|
| `AccountsModule.php` | Page Object du module Accounts (comptes) |
| `BasicModule.php` | Page Object générique pour les modules de type Basic |
| `Design.php` | Page Object pour les tests de design responsive |
| `CompanyModule.php` | Page Object pour les modules de type Company |
| `FileModule.php` | Page Object pour les modules de type File |
| `IssueModule.php` | Page Object pour les modules de type Issue |
| `PersonModule.php` | Page Object pour les modules de type Person |
| `SaleModule.php` | Page Object pour les modules de type Sale |

## Points d'entrée
Instanciés dans les `Step/Acceptance/` et directement dans les `Cest` d'acceptation.

## Dépendances clés
- Dépend de : Codeception Page Object pattern
- Utilisé par : `Step/Acceptance/`, `tests/acceptance/`

## Notes
Correspondent aux templates SugarObjects (Basic, Person, Company, Sale, Issue, File) — cohérence avec `include/SugarObjects/templates/`.
