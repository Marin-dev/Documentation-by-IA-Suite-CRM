# Fichier : WizardMarketing.php

**Chemin :** `modules/Campaigns/WizardMarketing.php`
**Type :** PHP - Script de vue (wizard etape marketing)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche l'etape "Message marketing" du wizard de campagne. Permet de creer ou editer un message `EmailMarketing` (sujet, template, date d'envoi, boite d'envoi) associe a la campagne.

## Role technique

Script procedural. Charge les beans Campaign et EmailMarketing. Utilise `modules/Campaigns/utils.php` pour les utilitaires de campagne. Affiche le formulaire d'edition du message via les templates HTML.

---

## Dependances cles

- `modules/Campaigns/utils.php`
- `BeanFactory` : `Campaigns`, `EmailMarketing`
- Globales : `$app_strings`, `$timedate`, `$app_list_strings`, `$mod_strings`, `$current_user`, `$sugar_config`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Action `WizardMarketing` dans le wizard de campagne

## Relations cles

- **Soumet vers :** `WizardMarketingSave.php`
- **Position dans le flux :** Etape 3 du wizard (configuration du message email)

---

## Points d'attention

- Partage les globales avec `WizardNewsletter.php` — structure similaire.
