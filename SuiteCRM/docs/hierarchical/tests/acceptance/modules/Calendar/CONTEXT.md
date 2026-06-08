# Calendar

## Rôle
Tests d'acceptation du module Calendar (calendrier) de SuiteCRM. Vérifie l'affichage, la navigation et la gestion des événements dans la vue calendrier de SuiteCRM.

## Contenu
| Fichier | Rôle |
|---|---|
| `CalendarCest.php` | Scénarios d'acceptation pour le module Calendrier |

## Points d'entrée
- `CalendarCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié au module CalendarSync (`include/CalendarSync/`) pour la synchronisation externe.
