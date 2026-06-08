# Fichier : view.edit.php

**Chemin :** `modules/FP_events/views/view.edit.php`
**Type :** PHP — vue (ViewEdit)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Vue d'edition d'un evenement FP_events. Surcharge la vue generique pour charger les templates d'email de type 'event' dans la liste deroulante du formulaire avant l'affichage.

## Role technique
Etend `ViewEdit`. Surcharge `display()` pour appeler `$this->bean->email_templates()` (qui peuple `$app_list_strings['emailTemplates_type_list']`) avant le rendu Smarty standard.

---

## Dependances cles
- `ViewEdit` — classe parente
- `FP_events::email_templates()` — charge les templates email de type 'event'

## Exports / Symboles principaux
- `class FP_eventsViewEdit extends ViewEdit`
- `display()` — appelle email_templates() puis parent::display()

## Relations cles
- **Appele par :** framework MVC SugarCRM (action EditView du module FP_events)
- **Appelle :** `$this->bean->email_templates()`, `parent::display()`

---

## Points d'attention
- RAS — vue minimaliste ; la logique metier est dans `FP_events::email_templates()`.
