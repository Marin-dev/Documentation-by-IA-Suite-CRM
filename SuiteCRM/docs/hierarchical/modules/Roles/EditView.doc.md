# EditView.php

**Chemin :** `modules/Roles/EditView.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue d'edition d'un role (legacy). Affiche le formulaire de modification d'un role avec le widget de choix des modules, similaire a DetailView.

## Type
view (legacy PHP)

## Dependances cles
- `XTemplate` — template `EditView.html`
- `TemplateGroupChooser`, `TabController`
- `DetailView` (include)

## Interactions
- **Appele par :** framework SuiteCRM (action=EditView, admin only)
- **Soumet vers :** `Save.php`

## Notes
- Reservee aux administrateurs.
