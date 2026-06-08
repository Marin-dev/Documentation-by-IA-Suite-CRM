# 📄 view.edit.php

**Chemin :** `modules/Bugs/views/view.edit.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Vue d'édition d'un bug. Affiche le formulaire de création/modification d'un enregistrement Bug. Injecte l'information sur l'activation du portail client.

## Rôle technique

Classe `BugsViewEdit` héritant de `ViewEdit`. Surcharge uniquement `display()` pour vérifier `portal_on` dans les settings d'administration et l'assigner au template via `$this->ev->ss` (EditView Smarty).

---

## Dépendances clés

- `ViewEdit` (framework SuiteCRM) — classe parente
- `BeanFactory::newBean('Administration')` — lecture de `portal_on`
- `$this->ev->ss` — Sugar_Smarty de la vue édition

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `BugsViewEdit` | classe | Vue édition du module Bugs |
| `display()` | méthode | Ajoute le flag portail puis affiche la vue |

---

## Relations clés

- **Appelé par :** framework MVC SugarCRM (action EditView)
- **Appelle :** `BeanFactory::newBean('Administration')`, `ViewEdit::display()`
- **Position dans le flux global :** formulaire de création/modification d'un bug

---

## Notes

- Différence avec `view.detail.php` : l'assignation se fait sur `$this->ev->ss` (et non `$this->ss`) car la vue édition utilise un objet `EditView` intermédiaire.
