# Fichier : WizardEmailSetupSave.php

**Chemin :** `modules/Campaigns/WizardEmailSetupSave.php`
**Type :** PHP - Script d'action (sauvegarde configuration email wizard)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Traite la sauvegarde de la configuration email du wizard de campagne. Persiste les parametres de boite d'envoi (OutboundEmail) et de boite de rebond (InboundEmail) configures a l'etape `WizardEmailSetup`.

## Role technique

Script procedural. INCONNU : corps non lu en entier. Probablement similaire a `WizardEmailSetup.php` mais cote traitement POST.

---

## Dependances cles

- INCONNU (corps non lu) — probablement `BeanFactory::newBean('Administration')`, `InboundEmail`, `OutboundEmail`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Formulaire POST depuis `WizardEmailSetup.php`

## Relations cles

- **Position dans le flux :** Sauvegarde de la configuration email avant les etapes d'envoi du wizard

---

## Points d'attention

- INCONNU : comportement exact a verifier dans le corps complet du fichier.
