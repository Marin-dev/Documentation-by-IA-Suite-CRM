# Targets

## Rôle
Tests d'acceptation du module Targets (cibles/prospects) de SuiteCRM. Vérifie la gestion des destinataires de campagne (prospects sans compte complet dans le CRM).

## Contenu
| Fichier | Rôle |
|---|---|
| `TargetsCest.php` | Scénarios d'acceptation pour le module Targets |

## Points d'entrée
- `TargetsCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié aux modules Campaigns et TargetLists. Différent de Leads — moins de champs, utilisé pour les listes de diffusion.
