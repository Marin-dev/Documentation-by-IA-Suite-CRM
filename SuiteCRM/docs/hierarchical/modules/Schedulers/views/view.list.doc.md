# Fichier : view.list.php

**Chemin :** `modules/Schedulers/views/view.list.php`
**Type :** PHP — vue (ViewList)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Vue liste des planificateurs. Affiche la liste standard des schedulers et ajoute les instructions cron en bas de page (comment configurer le cron job systeme pour faire tourner les schedulers).

## Role technique
Etend `ViewList`. Surcharge `display()` pour appeler `$this->seed->displayCronInstructions()` apres le rendu standard, sauf si l'option `show_all` est false.

---

## Dependances cles
- `ViewList` — classe parente
- `Scheduler::displayCronInstructions()` — affiche les instructions cron systeme

## Exports / Symboles principaux
- `class SchedulersViewList extends ViewList`
- `display()` — surcharge affichant les instructions cron

## Relations cles
- **Appele par :** framework MVC SugarCRM (action index/list du module Schedulers)
- **Appelle :** `parent::display()`, `$this->seed->displayCronInstructions()`

---

## Points d'attention
- RAS — vue simple.
