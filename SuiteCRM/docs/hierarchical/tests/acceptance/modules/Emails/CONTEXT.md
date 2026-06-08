# Emails

## Rôle
Tests d'acceptation du module Emails de SuiteCRM. Vérifie la création, l'envoi, la réception et l'archivage des e-mails ainsi que les relations avec les contacts et comptes.

## Contenu
| Fichier | Rôle |
|---|---|
| `EmailsCest.php` | Scénarios d'acceptation pour le module Emails |

## Points d'entrée
- `EmailsCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Module central de communication — lié aux modules Contacts, Accounts, Cases.
