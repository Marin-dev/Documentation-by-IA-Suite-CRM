# DetailView.php

**Chemin :** `modules/Roles/DetailView.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de detail d'un role (legacy). Affiche les proprietes du role et le widget de choix des modules autorises/refuses via `TemplateGroupChooser`. Inclut le sous-panneau Utilisateurs.

## Type
view (legacy PHP)

## Dependances cles
- `DetailView` (include) — traitement du bean
- `XTemplate` — rendu HTML via `DetailView.html`
- `TemplateGroupChooser` — widget de selection de modules
- `TabController` — liste des modules systeme
- `SubPanelTiles` — affichage des sous-panneaux

## Interactions
- **Appelle :** `$focus->query_modules(0/1)`, `TemplateGroupChooser->display()`, `SubPanelTiles->display()`
- **Appele par :** framework SuiteCRM (action=DetailView, admin only)

## Notes
- Reservee aux administrateurs (verifie `is_admin`).
- Si pas de record, redirige vers Accounts (vestige SugarCRM).
