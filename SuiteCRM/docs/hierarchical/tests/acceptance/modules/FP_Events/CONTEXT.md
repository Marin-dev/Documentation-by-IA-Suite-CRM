# FP_Events

## Rôle
Tests d'acceptation du module FP_Events (événements) de SuiteCRM. Vérifie la création et la gestion des événements (conférences, séminaires) avec inscription des participants.

## Contenu
| Fichier | Rôle |
|---|---|
| `FP_EventsCest.php` | Scénarios d'acceptation pour le module FP_Events |

## Points d'entrée
- `FP_EventsCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié au module `FP_Event_Locations` pour la gestion des lieux d'événements.
