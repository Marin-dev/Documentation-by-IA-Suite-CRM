# EmailMan

## Rôle
Tests d'acceptation du module EmailMan (gestionnaire d'e-mails) de SuiteCRM. Vérifie la gestion des files de diffusion et l'envoi des campagnes e-mail.

## Contenu
| Fichier | Rôle |
|---|---|
| `EmailManCest.php` | Scénarios d'acceptation pour le module EmailMan |

## Points d'entrée
- `EmailManCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié aux modules Campaigns et EmailTemplates.
