# Fichier : Campaign.php

**Chemin :** `modules/Campaigns/Campaign.php`
**Type :** PHP - Modele (SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Modele central du module Campaigns. Represente une campagne marketing (emailing, newsletter, banniere, etc.). Gere le cycle de vie d'une campagne : creation, sauvegarde, suppression, et expose les donnees pour les vues liste et detail.

## Role technique

Etend `SugarBean`. Mappe la table `campaigns`. Override plusieurs methodes SugarBean (`save`, `mark_deleted`, `create_export_query`, `get_list_view_data`, `create_list_count_query`). Gere la conversion de devise, le nettoyage des relations lors de la suppression, et le suivi des entrees de log de campagne via les relations ORM.

---

## Dependances cles

- **Extends :** `SugarBean`
- **BeanFactory :** `Currencies`, `EmailMan`, `ProspectLists` (utilises dans `save`)
- **SugarThemeRegistry :** images pour la liste
- **Tables liees :** `campaigns`, `prospect_list_campaigns`, `campaign_log`, `emailman`

## Exports / Symboles principaux

- `Campaign` — classe — modele principal du module Campaigns
  - `save($check_notify)` — sauvegarde avec conversion USD et nettoyage frequence newsletter (l.252)
  - `mark_deleted($id)` — nullifie `campaign_id` dans contacts/accounts, supprime les logs (l.273)
  - `track_log_entries($type, ...)` — construit la requete SQL pour les entrees de log filtrees par type/marketing (l.307)
  - `track_log_leads()` — requete pour les leads generes par la campagne (l.296)
  - `get_queue_items(...)` — requete pour les items en file d'attente EmailMan (l.363)
  - `create_list_count_query($query, $params)` — surcharge pour gerer DISTINCT sur marketing_id (l.438)
  - `getDeletedCampaignLogLeadsCount()` — compte les leads supprimes issus du formulaire web (l.459)
  - `bean_implements('ACL')` — retourne true, ACL actif (l.417)

## Consommateurs identifies

- `modules/Campaigns/Save.php`
- `modules/Campaigns/QueueCampaign.php`
- `modules/Campaigns/WizardHome.php`
- `modules/Campaigns/RoiDetailView.php`

## Relations cles

- **Relations ORM :** `prospectlists`, `emailmarketing`, `queueitems`, `log_entries`, `tracked_urls`, `leads`, `contacts`, `accounts`, `notes`, `survey`
- **Cible par :** contacts.campaign_id, accounts.campaign_id (FK nullifiees a la suppression)

---

## Points d'attention

- Bug53301 (l.264) : le champ `frequency` est force a vide si le type n'est pas `NewsLetter`.
- `mark_deleted` effectue des UPDATE directs en SQL sur contacts et accounts (contournement ORM).
- `track_log_entries` contient une logique complexe de deduplication par INNER JOIN sur `min(id)`.
- `create_list_count_query` detecte `marketing_id` dans la chaine SQL — couplage fragile par analyse de chaine.
