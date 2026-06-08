# utils.php (Campaigns)

**Chemin :** `modules/Campaigns/utils.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bibliotheque de fonctions utilitaires pour le module Campaigns. Regroupe la logique metier transversale : journalisation des activites de campagne (clics, suppressions, leads), gestion des abonnements/desabonnements aux newsletters, diagnostic de la configuration emailing, et generation des listes cibles.

**Type :** helper

---

## Dependances cles
- `DBManagerFactory::getInstance()` — acces direct base de donnees
- `BeanFactory` — instanciation de Campaigns, CampaignLog, ProspectLists
- `InboundEmail` (require conditionnel) — boites de rebond
- `OutboundEmail` (require conditionnel) — boites d'envoi

## Fonctions principales
| Fonction | Role |
|---|---|
| `log_campaign_activity($identifier, $activity, ...)` | Enregistre ou incremente une entree dans `campaign_log` pour tout clic/suppression/ciblage. Gere les campagnes banniere (md5 IP) et les cas de doublons |
| `subscribe($campaign, $prospect_list, $focus, ...)` | Abonne un lead/contact/prospect a une liste de campagne newsletter ; retire de la liste d'exemption si necessaire |
| `unsubscribe($campaign, $focus)` | Desabonne : ajoute a la liste `exempt`, retire de `default`/`test` |
| `get_subscription_lists($focus)` | Retourne les listes souscrites et non souscrites pour un contact/lead/prospect |
| `get_subscription_lists_keyed($focus)` | Variante avec donnees structurees en tableau associatif |
| `process_subscriptions($arr)` | Parse les chaines de subscription du formulaire (`prospect_list@id@campaign@id`) |
| `diagnose()` | Verifie la sante de la configuration (boite bounce + scheduler) ; retourne un HTML d'alerte si des problemes sont detectes |
| `campaign_log_lead_or_contact_entry(...)` | Cree une entree `CampaignLog` lors de la conversion d'un lead/contact |
| `track_campaign_prospects($focus)` | Repopule `campaign_log` avec toutes les cibles 'targeted' pour la campagne |
| `create_campaign_log_entry(...)` | Cree des entrees `CampaignLog` pour les cibles d'une campagne manuelle (mail-merge) |
| `get_campaign_mailboxes(...)` | Retourne les boites de rebond actives depuis `inbound_email` |
| `filterFieldsFromBeans($beans)` | Filtre les champs d'un bean Person pour la generation de formulaires web-to-lead |
| `getValidWebToPersonModules()` | Retourne les modules etendant la classe `Person` (pour formulaire web) |
| `isValidWebToPersonModule($module)` | Valide qu'un module est eligible au formulaire web-to-person |

## Interactions
- **Appele par :** `Tracker.php`, `RemoveMe.php`, `Subscriptions.php`, `WizardHome.php`, `WebToLeadCreation.php`, `WebToPersonCapture.php`, `DeleteTestCampaigns.php`
- **Tables DB :** `campaign_log`, `prospect_lists`, `prospect_list_campaigns`, `prospect_lists_prospects`, `campaign_trkrs`, `inbound_email`, `schedulers`

## Notes
- `log_campaign_activity()` : pour les campagnes banniere, l'identifiant est derive du MD5 de l'IP cliente ou d'un nouveau GUID selon la config `campaign_banner_id_generation` (ligne 184).
- `campaign_log_lead_entry()` est marquee `@deprecated` depuis version 62_Joneses (ligne 361-364) — utiliser `campaign_log_lead_or_contact_entry()`.
- `diagnose()` verifie specifiquement les schedulers `runMassEmailCampaign` et `pollMonitoredInboxesForBouncedCampaignEmails`.
