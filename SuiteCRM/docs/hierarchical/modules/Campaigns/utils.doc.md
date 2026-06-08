# utils.php

**Chemin :** `modules/Campaigns/utils.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Bibliothèque de fonctions utilitaires partagées par l'ensemble du module Campaigns. Couvre : logging des activités de campagne, gestion des abonnements/désabonnements, récupération des boîtes mail bounce, diagnostic de configuration, création d'entrées de log, et filtrage des champs pour formulaires Web-to-Lead.

## Type

`helper` (bibliothèque)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `DBManagerFactory::getInstance()` | Accès DB direct |
| `BeanFactory::newBean('CampaignLog')` | Création entrées log |
| `BeanFactory::newBean('ProspectLists')` | Gestion listes abonnement |
| `modules/InboundEmail/InboundEmail.php` | Récupération boîtes bounce |
| `modules/OutboundEmail/OutboundEmail.php` | Récupération boîtes outbound |
| `TimeDate::getInstance()` | Dates DB |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `log_campaign_activity()` | fonction | Enregistre ou met à jour une activité dans `campaign_log` (link, removed, bannière) |
| `get_message_scope_dom()` | fonction | Retourne la liste des prospect lists d'une campagne (hors exempt) |
| `get_campaign_mailboxes()` | fonction | Retourne les boîtes bounce actives |
| `get_campaign_mailboxes_with_stored_options()` | fonction | Retourne les options complètes des boîtes bounce |
| `get_campaign_mailboxes_with_stored_options_outbound()` | fonction | Retourne les boîtes outbound |
| `get_subscription_lists()` | fonction | Retourne les listes subscribed/unsubscribed d'une cible pour les newsletters |
| `get_subscription_lists_keyed()` | fonction | Variante avec données structurées (description, frequency) |
| `process_subscriptions()` | fonction | Parse les chaînes `prospect_list@id@campaign@id` en tableau |
| `subscribe()` | fonction | Abonne une cible à une prospect list newsletter |
| `unsubscribe()` | fonction | Désabonne une cible (ajoute à la liste exempt) |
| `diagnose()` | fonction | Vérifie la config email (boîte bounce, adresse from) et les schedulers nécessaires |
| `track_campaign_prospects()` | fonction | Re-génère toutes les entrées `targeted` dans `campaign_log` |
| `campaign_log_lead_or_contact_entry()` | fonction | Crée une entrée log pour un lead/contact |
| `campaign_log_mail_merge()` | fonction | Crée les entrées log pour mail-merge |
| `create_campaign_log_entry()` | fonction | Crée des entrées log pour toutes les cibles d'une relation |
| `filterFieldsFromBeans()` | fonction | Filtre les champs d'un bean pour le formulaire WebToLead |
| `getValidWebToPersonModules()` | fonction | Retourne les modules héritant de `Person` |
| `isValidWebToPersonModule()` | fonction | Vérifie si un module est valide pour WebToPerson |

---

## Interactions

- **Consommé par :** `Tracker.php`, `RemoveMe.php`, `Subscriptions.php`, `WizardHome.php`, `QueueCampaign.php`, `WebToLeadCapture.php`, `WebToLeadFormBuilder.php`
- **Appelle :** Tables `campaign_log`, `campaign_trkrs`, `prospect_lists`, `prospect_list_campaigns`, `inbound_email`, `schedulers`

---

## Points d'attention

- `log_campaign_activity()` gère deux flux distincts : bannières (identifiant basé sur IP/md5) vs emails (basé sur tracker_key) — logique longue et complexe (lignes 163-353).
- `diagnose()` vérifie deux schedulers critiques : `runMassEmailCampaign` et `pollMonitoredInboxesForBouncedCampaignEmails` — si absents, les campagnes ne fonctionnent pas.
- `subscribe()` / `unsubscribe()` manipulent directement les relations prospect_list_prospects — cohérence dépendante de l'intégrité référentielle.
- `campaign_log_lead_entry()` est dépréciée depuis juin 2011 (ligne 361).
