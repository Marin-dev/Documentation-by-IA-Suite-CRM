# Fichier : view.classic.php (Campaigns)

**Chemin :** `modules/Campaigns/views/view.classic.php`
**Type :** PHP - Vue (classic)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la vue "classique" du module Campaigns qui inclut et execute les anciens scripts PHP de vues (WizardHome, WizardMarketing, etc.) sans passer par le moteur Smarty. Sert de pont de compatibilite pour les scripts proceduraux du module.

## Role technique

Etend `SugarView`. Dans `display()`, determine l'action courante et inclut le fichier PHP correspondant depuis le dossier du module. Requiert `include/MVC/View/SugarView.php` et `include/MVC/Controller/SugarController.php`.

---

## Dependances cles

- `include/MVC/View/SugarView.php`
- `include/MVC/Controller/SugarController.php`

## Exports / Symboles principaux

- `CampaignsViewClassic` — classe — vue classique du module
  - `display()` — inclut le script PHP de l'action courante (l.59)

## Consommateurs identifies

- Framework MVC SuiteCRM (pour les actions ne disposant pas d'une vue Smarty dedie)
- `CampaignsController` (via la propriete `$this->view = 'classic'`)

## Relations cles

- **Inclut :** WizardHome.php, WizardMarketing.php, Schedule.php, etc.
- **Position dans le flux :** Couche de compatibilite pour les scripts legacy

---

## Points d'attention

- Ce pattern "vue classique" est une technique SugarCRM pour inclure des scripts proceduraux dans le nouveau framework MVC sans les recrire en vues Smarty.
