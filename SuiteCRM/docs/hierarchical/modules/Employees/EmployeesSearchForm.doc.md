# EmployeesSearchForm.php

**Chemin :** `modules/Employees/EmployeesSearchForm.php`
**Type :** PHP - Modèle (formulaire de recherche)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Formulaire de recherche spécialisé pour le module Employees. Étend `SearchForm` en adaptant un formulaire de recherche existant pour le module Employees, en préservant les searchdefs et searchFields du formulaire parent.

## Type
model

## Dépendances clés
- `include/SearchForm/SearchForm2.php` — classe parente `SearchForm`

## Exports / Symboles principaux
- `EmployeesSearchForm` (classe, étend `SearchForm`)
  - Constructeur : `__construct(SearchForm $oldSearchForm)` — construit à partir d'un formulaire existant

## Interactions
- **Appelé par :** vues liste du module Employees
- **Appelle :** `SearchForm::setup()`, `SearchForm::__construct()`

## Notes
- Pattern Adapter : transforme un `SearchForm` générique en formulaire Employees.
