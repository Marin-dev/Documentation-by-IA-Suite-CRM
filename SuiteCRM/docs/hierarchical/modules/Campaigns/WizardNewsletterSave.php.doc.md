# Fichier : WizardNewsletterSave.php

**Chemin :** `modules/Campaigns/WizardNewsletterSave.php`
**Type :** PHP - Script d'action (sauvegarde wizard newsletter)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Traite la sauvegarde de l'etape newsletter du wizard. Persiste la configuration specifique aux newsletters (frequence, listes d'abonnement) et redirige vers l'etape suivante.

## Role technique

Script procedural. INCONNU : corps non lu en entier. Par analogie avec les autres `*Save.php` du wizard.

---

## Dependances cles

- INCONNU — probablement `BeanFactory::newBean('Campaigns')`, `modules/Campaigns/utils.php`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Formulaire POST depuis `WizardNewsletter.php`

## Relations cles

- **Tables DB modifiees :** `campaigns`
- **Position dans le flux :** Sauvegarde de l'etape newsletter du wizard

---

## Points d'attention

- INCONNU : comportement exact a verifier dans le corps complet du fichier.
