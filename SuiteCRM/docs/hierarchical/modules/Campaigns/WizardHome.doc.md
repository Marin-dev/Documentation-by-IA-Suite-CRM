# WizardHome.php

**Chemin :** `modules/Campaigns/WizardHome.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Page de résumé et de navigation du wizard de campagne. Affiche les étapes (informations campagne, cibles, marketing emails, trackers) sous forme de tableaux récapitulatifs avec boutons d'action. Point d'entrée principal pour l'édition et l'envoi d'une campagne.

## Type

`view` (affichage classique wizard)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `modules/Campaigns/utils.php` | `diagnose()` |
| `BeanFactory::newBean('Campaigns')` | Bean de la campagne |
| `Sugar_Smarty` | Rendu du template `WizardHome.html` |
| `BeanFactory::newBean('EmailMarketing')` | Liste des messages marketing |
| `BeanFactory::newBean('ProspectLists')` | Liste des listes cibles |
| `BeanFactory::newBean('CampaignTrackers')` | Liste des trackers |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `create_campaign_summary()` | fonction | HTML du tableau résumé campagne |
| `create_marketing_summary()` | fonction | HTML du tableau des emails marketing avec boutons Test/Send |
| `create_target_summary()` | fonction | HTML du tableau des listes cibles |
| `create_tracker_summary()` | fonction | HTML du tableau des trackers |
| `create_wiz_menu_items()` | fonction | HTML du menu de navigation latéral du wizard |
| `isWizardSummary()` | fonction | Vérifie si on est sur la page résumé |
| `getMarketingId()` | fonction | Récupère l'ID du premier EmailMarketing de la campagne |

---

## Interactions

- **Appelé par :** `CampaignsController::process()` (action WizardHome)
- **Appelle :** `QueueCampaign.php`, `WizardMarketing.php`, `TrackDetailView.php`, `RoiDetailView.php`
- **Position dans le flux global :** Hub central du wizard de campagne

---

## Points d'attention

- Si aucun `record` en paramètre, affiche la page de choix du type de campagne (`WizardHomeStart.tpl`).
- Les boutons Test/Send dans `create_marketing_summary()` soumettent le formulaire vers `QueueCampaign` — pas d'appel AJAX.
- `isWizardSummary()` + `getMarketingId()` déclenchent une redirection vers `WizardMarketing` après un `WizardMarketingSave` (lignes 196-204).
