# WizardCampaignSave.php

**Chemin :** `modules/Campaigns/WizardCampaignSave.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Script AJAX de sauvegarde des données du wizard de campagne (marketing / template). Gère deux fonctionnalités : validation du template email (structure, sujet, corps) et sauvegarde/création d'un EmailMarketing. Retourne une réponse JSON.

## Type

`helper` (endpoint AJAX)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('EmailMarketing')` | Récupère/crée le bean EmailMarketing |
| `BeanFactory::newBean('EmailTemplates')` | Validation du template |
| `DBManagerFactory::getInstance()` | Accès DB |
| `$_SESSION['campaignWizard']` | Persistance de l'ID marketing sélectionné entre requêtes |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `getTemplateValidationMessages()` | fonction | Vérifie subject, body_html, body du template |

---

## Interactions

- **Appelé par :** JavaScript du wizard Campaign (appels AJAX)
- **Appelle :** `EmailMarketing::save()`, `EmailMarketing::validate()`
- **Position dans le flux global :** Étape 3 du wizard (configuration email marketing)

---

## Points d'attention

- Utilise la session `$_SESSION['campaignWizard'][$campaignId]['defaultSelectedMarketingId']` pour retenir l'ID marketing entre les requêtes AJAX.
- Si `func=getTemplateValidation`, aucune sauvegarde n'est effectuée — lecture seule.
- Si `func=createEmailMarketing`, le bean est sauvegardé sans mise à jour préalable.
