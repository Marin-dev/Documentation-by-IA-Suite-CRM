# Campaign.php

**Chemin :** `modules/Campaigns/Campaign.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Modèle principal du module Campaigns. Représente une campagne marketing (emailing, newsletter, bannière, etc.). Gère le cycle de vie complet d'une campagne : création, sauvegarde, suppression, export, et requêtes sur les logs d'activité associés.

## Type

`model`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `SugarBean` (extend) | Classe de base ORM SuiteCRM |
| `BeanFactory::newBean('Currencies')` | Conversion montant en USD lors du save |
| `BeanFactory::newBean('EmailMan')` | Construction de la requête emailman pour la file d'envoi |
| `SugarThemeRegistry::current()` | Récupération des URLs d'images pour la liste |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Campaign` | classe | Bean principal de la table `campaigns` |
| `list_view_parse_additional_sections()` | méthode | Injecte le nom de l'utilisateur assigné dans la vue liste |
| `create_export_query()` | méthode | Requête SQL d'export avec JOIN users |
| `clear_campaign_prospect_list_relationship()` | méthode | Supprime la relation campaign ↔ prospect_list |
| `save()` | méthode | Override : conversion devise, nullification de `frequency` si non-Newsletter |
| `mark_deleted()` | méthode | Override : nullifie `campaign_id` dans contacts/accounts, marque logs supprimés |
| `track_log_entries()` | méthode | Construit la requête de lecture des logs de campagne filtrés par type d'activité |
| `get_queue_items()` | méthode | Construit la requête EmailMan pour la file d'envoi |
| `create_list_count_query()` | méthode | Override avec gestion DISTINCT pour éviter les doublons multi-marketing |
| `getDeletedCampaignLogLeadsCount()` | méthode | Compte les leads supprimés créés via formulaire lead |

---

## Interactions

- **Appelé par :** `Save.php`, `QueueCampaign.php`, `WizardCampaignSave.php`, `Charts.php`, `TrackDetailView.php`
- **Appelle :** `campaign_campaignlog` (relation log_entries), `campaign_emailman` (relation queueitems), `EmailMan` (bean)
- **Position dans le flux global :** Entité centrale du module ; tous les sous-processus (envoi, tracking, ROI) lui sont attachés

---

## Points d'attention

- `mark_deleted()` propage la suppression en SQL direct sur `contacts`, `accounts` et `campaign_log` (ligne 275-283) — pas de hooks SugarBean pour ces tables.
- `track_log_entries()` utilise un INNER JOIN pour dédupliquer les cibles lorsque `group_by` et `marketing_id` sont présents (lignes 344-348) : logique complexe.
- Le champ `frequency` est forcé à vide si le type n'est pas NewsLetter (ligne 264) — bug 53301.
- Table de relation `prospect_list_campaigns` gérée manuellement (pas via le framework relation standard).
