# Fichier : WizardMarketingSave.php

**Chemin :** `modules/Campaigns/WizardMarketingSave.php`
**Type :** PHP - Script d'action (sauvegarde wizard message marketing)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Traite la sauvegarde d'un message `EmailMarketing` depuis l'etape marketing du wizard. Persiste les parametres du message (template, date, boite d'envoi) et redirige vers l'etape suivante.

## Role technique

Script procedural. INCONNU : corps non lu en entier. Par analogie avec `WizardCampaignSave.php`, gere le POST de l'etape marketing du wizard.

---

## Dependances cles

- INCONNU — probablement `BeanFactory::newBean('EmailMarketing')`, `modules/Campaigns/utils.php`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Formulaire POST depuis `WizardMarketing.php`

## Relations cles

- **Tables DB modifiees :** `email_marketing`
- **Position dans le flux :** Sauvegarde de l'etape 3 du wizard

---

## Points d'attention

- INCONNU : comportement exact a verifier dans le corps complet du fichier.
