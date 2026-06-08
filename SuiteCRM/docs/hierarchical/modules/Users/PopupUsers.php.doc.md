# Fichier : PopupUsers.php

**Chemin :** `modules/Users/PopupUsers.php`
**Type :** PHP — Vue (popup selection utilisateur)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche une fenetre popup permettant de rechercher et selectionner un ou plusieurs utilisateurs pour les assigner a un role ou a un enregistrement. Utilisee par le module Roles (`SaveUserRelationship`).

## Role technique

Script procedural. Construit une requete WHERE a partir des champs de recherche (`first_name`, `last_name`, `user_name`). Utilise `ListView` avec `XTemplate` (`Popup_Users_picker.html`) pour afficher la liste paginee. La selection soumet vers `module=Roles&action=SaveUserRelationship`.

---

## Dependances principales

| Import | Role |
|---|---|
| `BeanFactory::newBean('Users')` | Bean seed pour la liste |
| `XTemplate` | Template popup |
| `ListView` | Affichage liste paginee |
| `append_where_clause()` / `generate_where_statement()` | Construction requete |

## Exports / Symboles principaux

Aucun. Produit HTML popup.

---

## Relations cles

- **Appele par :** INCONNU — probablement depuis la gestion des roles utilisateurs
- **Soumet vers :** `module=Roles&action=SaveUserRelationship`
