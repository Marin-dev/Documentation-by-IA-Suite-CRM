# SearchResultsView.php

**Chemin :** `lib/Search/UI/SearchResultsView.php`
**Type :** PHP — View MVC
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Vue de rendu des resultats de recherche. Simple wrapper pointant vers le template Smarty des resultats.

## Role technique
Etend `View`. Constructeur fixe le template a `lib/Search/UI/templates/search.results.tpl`. Pas de logique supplementaire.

---

## Dependances cles
- `SuiteCRM\Search\UI\MVC\View`

## Exports / Symboles principaux
- `SearchResultsView` — vue

- **Consommateurs :** `SearchResultsController`

---

## Points d'attention
- Toute la logique de preparation de donnees est dans `SearchResultsController`.
