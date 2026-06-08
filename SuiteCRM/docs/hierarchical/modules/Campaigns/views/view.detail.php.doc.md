# Fichier : view.detail.php (Campaigns)

**Chemin :** `modules/Campaigns/views/view.detail.php`
**Type :** PHP - Vue (detail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge la vue detail standard pour le module Campaigns. Desactive l'affichage automatique des sous-panels, adapte le titre pour les newsletters, et gere le mode `set_target` qui repopule les cibles de campagne.

## Role technique

Etend `ViewDetail`. Desactive `show_subpanels` dans le constructeur et `preDisplay()`. En mode `set_target`, appelle `track_campaign_prospects()` depuis `utils.php` pour creer les entrees `CampaignLog`. Assigne `APP_LIST` au Smarty pour les vues.

---

## Dependances cles

- `ViewDetail` — classe parente
- `include/json_config.php`
- `modules/Campaigns/utils.php` — `track_campaign_prospects()` (chargement conditionnel)

## Exports / Symboles principaux

- `CampaignsViewDetail` — classe — vue detail du module Campaigns
  - `preDisplay()` — adapte le titre pour les newsletters (l.71)
  - `display()` — gere le mode `set_target`, assigne les listes (l.81)

## Consommateurs identifies

- Framework MVC SuiteCRM (charge pour `action=DetailView` du module Campaigns)

## Relations cles

- **Appelle :** `track_campaign_prospects()` en mode `set_target`
- **Position dans le flux :** Affichage principal d'une campagne

---

## Points d'attention

- Les sous-panels sont desactives dans la vue detail standard (`show_subpanels = false`) — les sous-panels sont probablement charges via AJAX/SubPanelViewer.
- Le mode `set_target` declenche la repopulation des logs de campagne a la demande.
