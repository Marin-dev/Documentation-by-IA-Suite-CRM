# WizardEmailSetupSave.php

**Chemin :** `modules/Campaigns/WizardEmailSetupSave.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de sauvegarde des paramètres email configurés via le wizard. Traite les données POST des étapes du wizard (`wiz_step_`, `wiz_step1_`, `wiz_step2_`) et les sauvegarde via le bean `Administration`.

**Type :** action (script de sauvegarde)

---

## Dépendances clés

- `include/formbase.php`
- `BeanFactory::newBean('Administration')` — persistance des réglages email
- `$mod_strings`

---

## Exports / Symboles principaux

Aucun — script procédural de sauvegarde.

---

## Interactions

**Appelle :**
- `BeanFactory::newBean('Administration')` pour sauvegarder les réglages

**Appelée par :** Soumission du formulaire `WizardEmailSetup.php`.

**Position dans le flux global :** Traitement POST du wizard de configuration email, après `WizardEmailSetup.php`.

---

## Notes

- Les préfixes `wiz_step_`, `wiz_step1_`, `wiz_step2_` sont utilisés pour regrouper les champs du formulaire par étape avant sauvegarde.
