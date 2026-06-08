# Fichier : view.list.php

**Chemin :** `modules/Meetings/views/view.list.php`
**Type :** vue (list view)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue liste du module Meetings. Utilise `MeetingsListViewSmarty` pour l'affichage, ce qui ajoute le lien "Carte" en plus de l'export. Filtre les colonnes de la liste pour inclure `recurring_source` (utile pour les controles ACL au niveau ligne).

## Role technique
Etend `ViewList`. Surcharge `preDisplay()` pour instancier `MeetingsListViewSmarty` et `listViewProcess()` pour ajouter le champ `recurring_source` dans `filterFields` avant l'appel a `lv->setup()`.

---

## Dependances cles
- `MeetingsListViewSmarty` (`modules/Meetings/MeetingsListViewSmarty.php`)
- `ViewList` — classe parente

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MeetingsViewList` | classe | vue liste meetings |

---

## Relations cles
- **Appele par :** routeur SuiteCRM (`action=index`)
- **Appelle :** `MeetingsListViewSmarty`

---

## Points d'attention
- `recurring_source` est filtre mais ne s'affiche pas en colonne — utilise uniquement pour le controle ACL ligne.
