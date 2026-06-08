# AOW_Workflow

## Rôle
Tests d'acceptation du module AOW_Workflow (workflows) de SuiteCRM. Vérifie la création, configuration et exécution des workflows automatisés (règles, conditions, actions).

## Contenu
| Fichier | Rôle |
|---|---|
| `AOW_WorkflowCest.php` | Scénarios d'acceptation pour le module Workflow |

## Points d'entrée
- `AOW_WorkflowCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Module d'automatisation business process SuiteCRM — très central pour la configuration des règles métier.
