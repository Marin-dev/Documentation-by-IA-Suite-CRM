# Campaigns

## Rôle
Tests d'acceptation du module Campaigns (campagnes marketing) de SuiteCRM. Vérifie la création et la gestion des campagnes e-mail, listes cibles et suivi des résultats.

## Contenu
| Fichier | Rôle |
|---|---|
| `CampaignsCest.php` | Scénarios d'acceptation pour le module Campaigns |

## Points d'entrée
- `CampaignsCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/Campaigns.php`
- Utilisé par : pipeline CI/CD

## Notes
Lié aux modules EmailTemplates, TargetLists, Targets.
