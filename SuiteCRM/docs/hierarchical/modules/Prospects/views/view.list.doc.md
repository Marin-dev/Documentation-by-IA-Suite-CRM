# view.list.php

**Chemin :** `modules/Prospects/views/view.list.php`
**Type :** PHP - Vue (liste)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue liste du module Prospects. Utilise `ProspectsListViewSmarty` pour afficher la liste avec le lien de cartographie JJW Google Maps intégré. Hérite de `ViewList`.

## Type
view

## Dépendances clés
- `ViewList` — classe parente
- `modules/Prospects/ProspectsListViewSmarty.php`

## Exports / Symboles principaux
- `ProspectsViewList` (classe, étend `ViewList`)

## Interactions
- **Appelé par :** action ListView du module Prospects
- **Appelle :** `ProspectsListViewSmarty`, `ViewList`

## Notes
- La méthode `LeadsViewList()` visible en ligne 50 semble être un ancien nom de méthode non nettoyé.
