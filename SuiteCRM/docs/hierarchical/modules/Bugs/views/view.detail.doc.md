# view.detail.php

**Chemin :** `modules/Bugs/views/view.detail.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de detail d'un bug. Surcharge la vue detail generique pour injecter l'information portal (activation du portail) dans le template Smarty.

## Type
view

## Dependances cles
- `ViewDetail` (heritage implicite — autoload SuiteCRM)
- `BeanFactory::newBean('Administration')` — lecture des parametres portal

## Exports / Symboles principaux
- `class BugsViewDetail extends ViewDetail`
- Methode `display()` — injecte `PORTAL_ENABLED` si le portail est actif

## Interactions
- **Appelle :** `BeanFactory::newBean('Administration')`, `$admin->retrieveSettings()`, `parent::display()`
- **Appele par :** framework SuiteCRM (routing action=DetailView)

## Notes
- Si `portal_on` est actif, la vue peut afficher des elements specifiques au portail client.
