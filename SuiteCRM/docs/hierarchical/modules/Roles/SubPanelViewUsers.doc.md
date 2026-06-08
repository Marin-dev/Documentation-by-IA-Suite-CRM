# SubPanelViewUsers.php

**Chemin :** `modules/Roles/SubPanelViewUsers.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue du sous-panneau Utilisateurs affiche dans la vue detail d'un role. Permet de visualiser les utilisateurs assignes au role et d'en ajouter via une popup.

## Type
view (subpanel)

## Dependances cles
- `ListView` — rendu XTemplate
- Template : `modules/Roles/SubPanelViewUsers.html`
- `SugarThemeRegistry` — images inline

## Interactions
- **Appele par :** framework SuiteCRM (vue detail Roles, sous-panneau Users)
- **Soumet vers :** `SaveUserRelationship.php`, `DeleteUserRelationship.php`

## Notes
- Bouton "Select" ouvre une popup `PopupUsers`.
