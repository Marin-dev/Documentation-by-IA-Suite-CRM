# view.detail.php

**Chemin :** `modules/Prospects/views/view.detail.php`
**Type :** PHP - Vue (détail)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de détail du module Prospects. Étend `ViewDetail` avec une logique spécifique pour les prospects convertis depuis des leads : si `lead_id` est défini, affiche une bannière ou redirige vers le lead d'origine.

## Type
view

## Dépendances clés
- `ViewDetail` — classe parente
- `$this->bean->lead_id` — identifiant du lead d'origine

## Exports / Symboles principaux
- `ProspectsViewDetail` (classe, étend `ViewDetail`)
  - `display()` — gère le cas prospect converti depuis lead (lead_id non vide)

## Interactions
- **Appelé par :** action DetailView du module Prospects
- **Appelle :** `ViewDetail::display()`

## Notes
- Cas particulier : un prospect peut être converti depuis un lead, dans ce cas `lead_id` est renseigné.
