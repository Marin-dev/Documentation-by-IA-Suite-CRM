# vardefs.php (Campaigns)

**Chemin :** `modules/Campaigns/vardefs.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Definition du schema de la table `campaigns` et des relations ORM du module Campaigns. Declare les champs, les index, et les relations avec les autres modules (Accounts, Contacts, Leads, Opportunities, EmailMarketing, CampaignLog, Surveys, etc.).

**Type :** config (vardefs)

---

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `table` | `campaigns` | Table SQL principale |
| `audited` | `true` | Journalisation des modifications |
| `unified_search` | `true` | Inclus dans la recherche globale |
| `full_text_search` | `true` | Indexe pour la recherche plein texte |
| Champ `campaign_type` | enum `campaign_type_dom` | Determine le comportement (Email, NewsLetter, etc.) |
| Champ `status` | enum `campaign_status_dom`, required | Statut de la campagne |
| Champ `frequency` | enum `newsletter_frequency_dom` | Frequence, pertinent uniquement pour les newsletters |
| Champ `survey_id` | id | Liaison optionnelle a un questionnaire (Surveys) |

## Relations definies
| Nom | Type | Modules |
|---|---|---|
| `campaign_accounts` | one-to-many | Campaigns -> Accounts (via `campaign_id`) |
| `campaign_contacts` | one-to-many | Campaigns -> Contacts (via `campaign_id`) |
| `campaign_leads` | one-to-many | Campaigns -> Leads |
| `campaign_opportunities` | one-to-many | Campaigns -> Opportunities |
| `campaign_email_marketing` | one-to-many | Campaigns -> EmailMarketing |
| `campaign_emailman` | one-to-many | Campaigns -> EmailMan (file d'envoi) |
| `campaign_campaignlog` | one-to-many | Campaigns -> CampaignLog |
| `prospect_list_campaigns` | many-to-many (via table) | Campaigns <-> ProspectLists |
| `surveys_campaigns` | one-to-many | Campaigns -> SurveyResponses |

## Notes
- Les champs `tracker_key`, `tracker_count`, `refer_url`, `tracker_text` sont depreciés depuis la version 4.2 (remplacés par `campaign_trkrs`).
- Le lien `leads` et `contacts` utilise la classe `ProspectLink` (`link_class`) pour effectuer des jointures via les listes cibles (prospect_list_campaigns + prospect_lists_prospects).
