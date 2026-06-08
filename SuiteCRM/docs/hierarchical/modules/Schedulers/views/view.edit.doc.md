# Fichier : view.edit.php

**Chemin :** `modules/Schedulers/views/view.edit.php`
**Type :** PHP — vue (ViewEdit)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Vue d'edition d'un planificateur (Scheduler). Surcharge la vue generique pour decoder et afficher le champ `job_interval` en format lisible (cron-like), et determiner si l'interface doit etre en mode "basic" (intervalle simple) ou "avance" (expression cron complete).

## Role technique
Etend `ViewEdit`. Decompose `job_interval` (format `min::hr::date::mon::day`) en variables Smarty. Detecte le mode "basic" (*/X sur minutes ou heures) ou avance. Si `time_from`/`time_to` sont definis, force le mode avance. Utilise `$this->ss->assign()` pour passer les variables au template Smarty.

---

## Dependances cles
- `ViewEdit` — classe parente
- `$app_list_strings['scheduler_period_dom']` — options periode (min/heure)
- Smarty (`$this->ss`) — moteur de templates

## Exports / Symboles principaux
- `class SchedulersViewEdit extends ViewEdit`
- `display()` — surcharge principale ; analyse l'intervalle et injecte les variables Smarty

## Relations cles
- **Appele par :** framework MVC SugarCRM (action EditView du module Schedulers)
- **Appelle :** `parent::display()`
- **Position dans le flux :** Vue d'edition des planificateurs ; complement de `Scheduler.php`

---

## Points d'attention
- Le decode des jours de la semaine (lignes 101-126) a des cas edge potentiels si `$exInterval[4]` est un range seul sans virgule.
- `$xtDays` (0=SUN, 1=MON...) : attention a la correspondance avec les valeurs cron standard.
