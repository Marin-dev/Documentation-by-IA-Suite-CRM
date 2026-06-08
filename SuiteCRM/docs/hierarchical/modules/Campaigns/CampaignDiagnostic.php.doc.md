# CampaignDiagnostic.php

**Chemin :** `modules/Campaigns/CampaignDiagnostic.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Page de diagnostic de la configuration email des campagnes. Verifie en temps reel : (1) presence de boites de rebond de type `bounce` dans `inbound_email`, (2) configuration de l'adresse `from` (non-defaut), (3) presence et activite des deux schedulers necessaires (`runMassEmailCampaign`, `pollMonitoredInboxesForBouncedCampaignEmails`). Affiche un tableau de synthese avec indicateurs visuels vert/jaune/rouge.

**Type :** view (script d'action)

---

## Dependances cles
- `Sugar_Smarty` — rendu du template `CampaignDiagnostic.html`
- `BeanFactory::newBean('Administration')` — lecture des parametres admin
- `SugarThemeRegistry::current()` — images d'indicateur (red_camp, green_camp, yellow_camp)
- Fonction `define_image()` — definie en bas du fichier

## Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `define_image($num, $total)` | fonction | Retourne le tag img appropriate selon le ratio de sante (rouge/vert/jaune) |

## Interactions
- **Appele par :** Menu Campaigns > Diagnostics, lien dans WizardHome
- **Appelle :** `Administration->retrieveSettings()`, requetes directes sur `inbound_email`, `schedulers`
- **Position dans le flux :** Vue d'audit pre-envoi, accessible avant toute campagne email/newsletter

## Notes
- Ce script est aussi utilisable en mode `inline` (parametre `$_REQUEST['inline']`) depuis les wizards.
- Le lien vers `WizardEmailSetup` n'est affiche qu'aux administrateurs si la sante est degradee.
