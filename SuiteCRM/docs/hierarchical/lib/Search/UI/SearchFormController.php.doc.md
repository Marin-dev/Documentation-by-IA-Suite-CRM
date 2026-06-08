# SearchFormController.php

**Chemin :** `lib/Search/UI/SearchFormController.php`
**Type :** PHP — Controller MVC
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Controleur de la barre de recherche et du formulaire de recherche. Assigne les variables Smarty (query, size, from, engine, modules) et delegue le rendu a `SearchFormView`.

## Role technique
Etend `Controller`. Surcharge `display()` pour passer les donnees de la `SearchQuery` et les modules selectionnes par l'utilisateur (`SearchWrapper::getUserSelectedModules()`) au template Smarty.

---

## Dependances cles
- `SuiteCRM\Search\SearchQuery`
- `SuiteCRM\Search\SearchWrapper`
- `SuiteCRM\Search\UI\{SearchFormView, MVC\Controller}`

## Exports / Symboles principaux
- `SearchFormController` — controleur
  - `display(): void`

- **Consommateurs :** `SearchEngine::displayForm()`

---

## Points d'attention
- La chaine de recherche est encodee HTML via `htmlspecialchars()` avant assignation (ligne 74).
