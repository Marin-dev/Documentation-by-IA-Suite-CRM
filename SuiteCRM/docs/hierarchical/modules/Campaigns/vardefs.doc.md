# vardefs.php

**Chemin :** `modules/Campaigns/vardefs.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Définit le schéma de données (vardefs) de l'entité Campaign : champs de la table `campaigns`, index, et relations ORM avec d'autres modules (Accounts, Contacts, Leads, EmailMarketing, CampaignLog, Surveys, etc.).

## Type

`config`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `VardefManager::createVardef()` | Applique les templates `default`, `assignable`, `security_groups` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `$dictionary['Campaign']` | tableau | Définition complète du bean : table, champs, indices, relations |

### Champs principaux

| Champ | Type DB | Notes |
|---|---|---|
| `name` | varchar(255) | Obligatoire, recherche unifiée boost 3 |
| `start_date` / `end_date` | date | Validation `isbefore` |
| `status` | enum | `campaign_status_dom` |
| `campaign_type` | enum | `campaign_type_dom` |
| `budget` / `actual_cost` / `expected_cost` / `expected_revenue` | double (currency) | Montants financiers |
| `frequency` | enum | `newsletter_frequency_dom` — uniquement pour NewsLetters |
| `survey_id` | id | Lien optionnel vers un Survey |

### Relations déclarées

| Relation | Modules liés | Type |
|---|---|---|
| `campaign_accounts` | Campaigns → Accounts | one-to-many |
| `campaign_contacts` | Campaigns → Contacts | one-to-many |
| `campaign_leads` | Campaigns → Leads | one-to-many |
| `campaign_email_marketing` | Campaigns → EmailMarketing | one-to-many |
| `campaign_emailman` | Campaigns → EmailMan | one-to-many |
| `campaign_campaignlog` | Campaigns → CampaignLog | one-to-many |
| `surveyresponses_campaigns` | Campaigns → SurveyResponses | one-to-many |

---

## Interactions

- **Consommé par :** `Campaign.php` (bean), framework ORM SuiteCRM, Studio
- **Impacte :** Schéma de la table `campaigns` en base de données

---

## Points d'attention

- Les champs `tracker_key`, `tracker_text`, `tracker_count`, `refer_url` sont marqués comme "no longer used as of 4.2" — présents pour compatibilité ascendante.
- Le champ `description` est de type `none` / `source: non-db` (hérité mais non utilisé).
