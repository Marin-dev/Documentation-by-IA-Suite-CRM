# controller.php

**Chemin :** `modules/MergeRecords/controller.php`
**Type :** PHP - Controller
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Contrôleur du module MergeRecords. Surcharge `loadBean()` pour ne pas charger automatiquement un bean (le module ne correspond pas à un bean standard).

## Type
controller

## Dépendances clés
- `include/MVC/Controller/SugarController.php`

## Exports / Symboles principaux
- `MergeRecordsController` (classe, étend `SugarController`)
  - `loadBean()` — méthode vide (override intentionnel)

## Interactions
- **Appelé par :** framework SugarCRM (dispatcher d'actions)
- **Appelle :** `SugarController` (héritage)

## Notes
- Override de `loadBean()` pour éviter le chargement automatique d'un bean inexistant.
