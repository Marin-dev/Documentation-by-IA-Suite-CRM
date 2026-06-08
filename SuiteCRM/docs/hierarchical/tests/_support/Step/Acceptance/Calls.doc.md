# Calls.php (helper)

**Chemin :** `tests/_support/Step/Acceptance/Calls.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Step Object Codeception fournissant des actions metier pour la creation d'appels (module Calls) dans les tests d'acceptance. Encapsule le remplissage du formulaire de creation d'appel.

## Role technique

Etend `AcceptanceTester`. Propose deux methodes : `createCall($name)` pour creer un appel simple, et `createCallRelateModule($name, $module_name, $module, $params)` pour creer un appel lie a un autre module. Utilise `EditView`, `DetailView`, `SideBar` et `Faker`.

---

## Entrees / Dependances

- **Imports principaux :**
  - `EditView`, `DetailView`, `SideBar` — step objects utilises en interne
  - `Faker` — generation de donnees aleatoires via `getFaker()`

## Sorties / Exports

- `createCall(string $name)` — cree un appel via l'interface
- `createCallRelateModule(string $name, string $module_name, string $module, array $params)` — cree un appel lie a un module
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/modules/Calls/CallsCest.php`

## Relations cles

- **Appele par :** `CallsCest`
- **Appelle :** `EditView`, `DetailView`, `SideBar`
- **Position dans le flux global :** helper de creation pour les tests acceptance du module Calls

---

## Points d'attention

- La date `01/19/2038` est codee en dur (valeur limite Unix timestamp 32 bits).
