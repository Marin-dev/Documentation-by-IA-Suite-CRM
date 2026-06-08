# Meetings

## Rôle
Tests d'acceptation du module Meetings (réunions) de SuiteCRM. Vérifie la création, la planification, les invitations et la synchronisation calendrier des réunions.

## Contenu
| Fichier | Rôle |
|---|---|
| `MeetingsCest.php` | Scénarios d'acceptation pour le module Meetings |

## Points d'entrée
- `MeetingsCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié au module CalendarSync (`include/CalendarSync/`) pour la synchronisation Google/CalDAV.
