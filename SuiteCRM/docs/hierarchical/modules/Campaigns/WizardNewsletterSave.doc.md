# WizardNewsletterSave.php

**Chemin :** `modules/Campaigns/WizardNewsletterSave.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de sauvegarde des étapes du wizard newsletter/campagne email. Traite les données POST préfixées par `wiz_step1_` et `wiz_step2_` et sauvegarde les informations de campagne (nom, dates, budget, etc.) via le bean `Campaigns`.

**Type :** action (script de sauvegarde wizard)

---

## Dépendances clés

- `include/formbase.php`
- `BeanFactory::newBean('Campaigns')` — création ou mise à jour de la campagne
- `$mod_strings`

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

---

## Interactions

**Appelle :**
- `BeanFactory::newBean('Campaigns')` pour persister les données
- `populateFromPost()` (formbase) pour remplir le bean depuis POST

**Appelée par :** Soumission des formulaires `WizardNewsletter.php` et `WizardEmailSetup.php`.

**Position dans le flux global :** Sauvegarde intermédiaire dans le wizard de création de campagne email/newsletter.

---

## Notes

- Prend en charge les deux modes : création (pas de `record`) et mise à jour (avec `record` ou `campaign_id`).
- Les préfixes `wiz_step1_` et `wiz_step2_` reflètent les deux premières étapes du wizard (informations de base + budget).
