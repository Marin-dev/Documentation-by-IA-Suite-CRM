# Fichier : WizardCampaignSave.php

**Chemin :** `modules/Campaigns/WizardCampaignSave.php`
**Type :** PHP - Script d'action (sauvegarde wizard email marketing)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere la sauvegarde du message email marketing depuis le wizard de campagne. Permet de valider et sauvegarder un template `EmailMarketing` associe a une campagne, ou de valider uniquement la configuration du template (mode `getTemplateValidation`).

## Role technique

Script procedural. Selon le parametre `func` dans la requete, soit valide le template (`getTemplateValidation`) soit sauvegarde le bean `EmailMarketing`. Utilise la session `campaignWizard[$campaignId]` pour stocker le `defaultSelectedMarketingId`. Retourne une reponse JSON.

---

## Dependances cles

- `DBManagerFactory::getInstance()` — sanitisation des IDs
- `BeanFactory::newBean('EmailMarketing')` — bean message marketing
- `BeanFactory::newBean('EmailTemplates')` — validation du template

## Exports / Symboles principaux

- `getTemplateValidationMessages($templateId)` — retourne les messages de validation d'un template (l.47)

## Consommateurs identifies

- Wizard de campagne (appel AJAX depuis l'etape "Email Marketing")

## Relations cles

- **Tables DB modifiees :** `email_marketing`
- **Position dans le flux :** Etape 3-4 du wizard de campagne (configuration du message)
- **Retourne :** JSON avec `templateValidationMessages` et `marketingValidationMessages`

---

## Points d'attention

- Utilise `$_SESSION['campaignWizard']` pour persister le `defaultSelectedMarketingId` entre les requetes wizard (l.75, l.115).
- En mode `createEmailMarketing`, ne sauvegarde pas le bean (l.111-113) — permet la preview sans persistence.
- La validation verifie : template selectionne, sujet non vide, corps HTML et texte non vides.
