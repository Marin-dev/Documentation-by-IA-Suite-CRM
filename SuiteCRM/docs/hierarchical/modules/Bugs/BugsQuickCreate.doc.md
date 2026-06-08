# BugsQuickCreate.php

**Chemin :** `modules/Bugs/BugsQuickCreate.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Gere le formulaire de creation rapide (Quick Create) d'un bug depuis un sous-panneau ou une popup. Permet de creer un bug sans naviguer vers la vue d'edition complete.

## Type
controller / helper vue

## Dependances cles
- `include/EditView/QuickCreate.php` — classe parente `QuickCreate`
- `BeanFactory::newBean('Bugs')` — instanciation du bean pour la validation JS
- `javascript` (classe SuiteCRM) — generation des scripts de validation cote client
- `$app_list_strings` — listes de valeurs (bug_priority_dom, bug_status_dom, bug_type_dom)

## Exports / Symboles principaux
- `class BugsQuickCreate extends QuickCreate`
- Methode `process()` — prepare les options de formulaire et les scripts JS

## Interactions
- **Appelle :** `parent::process()`, `BeanFactory::newBean('Bugs')`, `get_select_options_with_id()`, `javascript->setFormName/setSugarBean/addAllFields/getScript`
- **Appele par :** framework SuiteCRM lors du rendu d'un sous-panneau Bugs avec action QuickCreate
- **Mode AJAX :** surcharge les attributs `saveOnclick`/`cancelOnclick` si `$this->viaAJAX`

## Notes
- Form name fixe : `bugsQuickCreate`.
- Sous-panneau cible : `subpanel_bugs`.
- Pas de logique metier ; uniquement preparation de la vue.
