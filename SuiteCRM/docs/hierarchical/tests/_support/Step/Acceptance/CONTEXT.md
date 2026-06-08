# Acceptance

## Rôle
Steps Codeception pour les tests d'acceptation SuiteCRM. Implémente les actions réutilisables de haut niveau (navigation, CRUD sur modules, interactions UI) pour les scénarios d'acceptation, en abstrayant les interactions Codeception de bas niveau.

## Contenu
| Fichier | Rôle |
|---|---|
| `NavigationBarTester.php` | Actions sur la barre de navigation principale (menus, recherche globale) |
| `Accounts.php` | Actions métier sur le module Accounts (création, modification, suppression) |
| `Dashboard.php` | Actions sur le tableau de bord SuiteCRM |
| `Calls.php` | Actions métier sur le module Calls (appels) |
| `Campaigns.php` | Actions métier sur le module Campaigns (campagnes) |
| `Cases.php` | Actions métier sur le module Cases (incidents) |
| `Contacts.php` | Actions métier sur le module Contacts |

## Points d'entrée
Injectés dans les `Cest` d'acceptation via l'acteur `AcceptanceTester`.

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Page/`
- Utilisé par : `tests/acceptance/modules/`, `tests/acceptance/Core/`

## Notes
Pattern Steps Codeception — sépare la logique de navigation/interaction de la logique de scénario dans les Cest.
