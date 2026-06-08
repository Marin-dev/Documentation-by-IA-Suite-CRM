# Fichier : view.list.php

**Chemin :** `modules/Emails/views/view.list.php`
**Type :** PHP — Vue (liste emails)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue liste du module Emails. Affiche les emails tries par date d'envoi/reception decroissante, sans message si la liste est vide.

## Role technique

Herite de `ViewList`. Override `preDisplay()` pour forcer le tri par `date_sent_received DESC` et utiliser `ListViewSmartyEmails` a la place du `ListViewSmarty` standard.

---

## Dependances

- **Herite de :** `ViewList`
- **Imports :** `modules/Emails/include/ListView/ListViewSmartyEmails.php`

## Exports / Symboles principaux

- `EmailsViewList` — classe vue
  - `preDisplay()` — configure le tri et la vue liste specifique

## Relations cles

- **Appele par :** `EmailsController::action_index()`
- **Utilise :** `ListViewSmartyEmails`

---

## Points d'attention

- `$this->lv->displayEmptyDataMessages = false` : pas de message "aucun resultat" affiche.
