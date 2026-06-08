# Accounts

## Rôle
Tests d'acceptation du module Accounts (comptes) de SuiteCRM. Vérifie les scénarios CRUD et les fonctionnalités spécifiques au module Accounts via l'interface utilisateur.

## Contenu
| Fichier | Rôle |
|---|---|
| `AccountsCest.php` | Scénarios d'acceptation complets pour le module Accounts |

## Points d'entrée
- `AccountsCest` — suite de tests pour le module Accounts

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Page/AccountsModule.php`, `_support/Step/Acceptance/Accounts.php`
- Utilisé par : pipeline CI/CD

## Notes
Module Accounts est central dans SuiteCRM — les tests couvrent les interactions avec Contacts, Opportunities, etc.
