# Contacts

## Rôle
Tests d'acceptation du module Contacts de SuiteCRM. Vérifie la création, modification et relations des fiches contact avec les autres modules (Accounts, Meetings, Calls, etc.).

## Contenu
| Fichier | Rôle |
|---|---|
| `ContactsCest.php` | Scénarios d'acceptation pour le module Contacts |

## Points d'entrée
- `ContactsCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/Contacts.php`
- Utilisé par : pipeline CI/CD

## Notes
Module central du CRM — relations avec Accounts, Leads, Meetings, Calls.
