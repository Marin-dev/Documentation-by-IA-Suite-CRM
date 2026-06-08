# view.edit.php

**Chemin :** `modules/Bugs/views/view.edit.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue d'edition d'un bug. Surcharge la vue edit generique pour injecter l'information portal dans le template Smarty du formulaire d'edition.

## Type
view

## Dependances cles
- `ViewEdit` (heritage implicite — autoload SuiteCRM)
- `BeanFactory::newBean('Administration')` — lecture des parametres portal

## Exports / Symboles principaux
- `class BugsViewEdit extends ViewEdit`
- Methode `display()` — injecte `PORTAL_ENABLED` via `$this->ev->ss`

## Interactions
- **Appelle :** `BeanFactory::newBean('Administration')`, `$admin->retrieveSettings()`, `parent::display()`
- **Appele par :** framework SuiteCRM (routing action=EditView)

## Notes
- Meme logique que `view.detail.php` mais appliquee a la vue d'edition.
