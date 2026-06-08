# modules

## Rôle
Tests d'acceptation organisés par module SuiteCRM. Chaque sous-dossier contient un fichier `*Cest.php` avec les scénarios UI pour le module correspondant. Couvre l'ensemble des modules fonctionnels de SuiteCRM : CRM core (Accounts, Contacts, Leads, Opportunities), activités (Calls, Meetings, Tasks), marketing (Campaigns, EmailMan), projets, documents, et modules AO/AM/FP/AOW.

## Contenu
| Dossier | Module SuiteCRM |
|---|---|
| `Accounts/` | Comptes |
| `AM_Project_Templates/` | Modèles de projets |
| `AOK_KnowledgeBase/` | Base de connaissances |
| `AOK_Knowledge_Base_Categories/` | Catégories base de connaissances |
| `AOR_Reports/` | Rapports |
| `AOS_PDF_Templates/` | Modèles PDF |
| `AOS_Product_Categories/` | Catégories produits |
| `AOS_Products/` | Produits |
| `AOW_Workflow/` | Workflows |
| `Activities/` | Activités (vue agrégée) |
| `Calendar/` | Calendrier |
| `Calls/` | Appels |
| `Campaigns/` | Campagnes marketing |
| `Cases/` | Incidents support |
| `Contacts/` | Contacts |
| `Contracts/` | Contrats |
| `Documents/` | Documents |
| `EmailMan/` | Gestionnaire e-mails |
| `EmailTemplates/` | Modèles e-mails |
| `Emails/` | E-mails |
| `FP_Events/` | Événements |
| `FP_Event_Locations/` | Lieux d'événements |
| `History/` | Historique activités |
| `Invoices/` | Factures |
| `Leads/` | Prospects |
| `Meetings/` | Réunions |
| `Notes/` | Notes |
| `Opportunities/` | Opportunités |
| `Projects/` | Projets |
| `Quotes/` | Devis |
| `Spots/` | Spots (INCONNU) |
| `Surveys/` | Enquêtes |
| `TargetLists/` | Listes cibles |
| `Targets/` | Cibles campagne |
| `Tasks/` | Tâches |

## Points d'entrée
Chaque `*Cest.php` est une suite autonome lancée par Codeception.

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/`, SuiteCRM déployé (BDD réelle)
- Utilisé par : pipeline CI/CD, tests de régression

## Notes
Tests end-to-end — nécessitent un SuiteCRM opérationnel. Couvrent 35 modules métier.
