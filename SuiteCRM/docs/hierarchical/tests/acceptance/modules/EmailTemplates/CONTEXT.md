# EmailTemplates

## Rôle
Tests d'acceptation du module EmailTemplates (modèles d'e-mails) de SuiteCRM. Vérifie la création et la gestion des templates d'e-mails utilisés dans les campagnes et workflows.

## Contenu
| Fichier | Rôle |
|---|---|
| `EmailTemplatesCest.php` | Scénarios d'acceptation pour le module EmailTemplates |

## Points d'entrée
- `EmailTemplatesCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié aux modules Campaigns, AOW_Workflow et EmailMan.
