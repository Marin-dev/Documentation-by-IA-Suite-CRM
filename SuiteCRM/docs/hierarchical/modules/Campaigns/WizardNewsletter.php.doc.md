# Fichier : WizardNewsletter.php

**Chemin :** `modules/Campaigns/WizardNewsletter.php`
**Type :** PHP - Script de vue (wizard newsletter)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche l'etape de configuration d'une newsletter dans le wizard de campagne. Specifique aux campagnes de type `NewsLetter`, permet de configurer la frequence, les listes d'abonnement et les parametres specifiques aux newsletters.

## Role technique

Script procedural. Structure identique a `WizardMarketing.php` mais specialisee pour les newsletters. Utilise `modules/Campaigns/utils.php` pour les fonctions communes.

---

## Dependances cles

- `modules/Campaigns/utils.php`
- `BeanFactory` : `Campaigns`
- Globales : `$app_strings`, `$timedate`, `$app_list_strings`, `$mod_strings`, `$current_user`, `$sugar_config`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Action `WizardNewsletter` dans le wizard de campagne de type Newsletter

## Relations cles

- **Soumet vers :** `WizardNewsletterSave.php`
- **Position dans le flux :** Etape newsletter du wizard (frequence, gestion des abonnes)

---

## Points d'attention

- Specifique aux campagnes `NewsLetter` — ne pas utiliser pour les campagnes Email standard.
