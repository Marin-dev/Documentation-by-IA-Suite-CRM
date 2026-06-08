# Fichier : controller.php

**Chemin :** `modules/Users/controller.php`
**Type :** PHP — Controleur (SugarController)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Controleur MVC du module Users. Intercepte et traite les actions HTTP specifiques au module : suppression d'utilisateur, reset des preferences, assistant de configuration initiale (wizard), sauvegarde des modules de recherche plein texte, et acces aux vues edition/detail avec controle d'acces.

## Role technique

Classe `UsersController` qui etend `SugarController`. Chaque methode `action_*` correspond a une action URL (`?module=Users&action=...`). Le controleur delegue la logique metier au bean `User` via `BeanFactory`, et redirige via `SugarApplication::redirect()`. La methode `action_saveuserwizard` gere specialement le premier passage de l'assistant en ecrivant preferences et donnees utilisateur en une seule requete POST.

---

## Dependances principales

| Import | Role |
|---|---|
| `OutboundEmail` | Gestion email sortant (charge dans le require) |
| `UserPreference` | Preferences utilisateur |
| `BeanFactory` | Creation des beans Users, EAPM |
| `SugarThemeRegistry` | Theme par defaut pour le wizard |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `UsersController` | classe | Controleur du module Users |
| `action_resetPreferences()` | methode | Remet a zero les preferences de l'utilisateur cible |
| `action_delete()` | methode | Suppression logique (status=Inactive) + suppression comptes externes |
| `action_wizard()` | methode | Affiche la vue wizard |
| `action_saveuserwizard()` | methode | Sauvegarde les donnees du wizard de premier demarrage |
| `action_saveftsmodules()` | methode | Sauvegarde les modules desactives pour la recherche FTS |
| `action_editview()` | methode | Acces a la vue edition avec controle admin/self |
| `action_detailview()` | methode | Acces a la vue detail avec controle admin/self |

---

## Relations cles

- **Etend :** `SugarController`
- **Appelle :** `User` (via BeanFactory), `EAPM::delete_user_accounts()`, `SugarApplication::redirect()`
- **Appele par :** le routeur MVC SugarCRM via `index.php?module=Users&action=...`

---

## Points d'attention

- `action_delete()` ne supprime pas physiquement : met le statut a `Inactive` / `Terminated`, appelle `mark_deleted()`, puis supprime les comptes externes EAPM. Un utilisateur ne peut pas se supprimer lui-meme (ligne 78-100).
- `action_saveuserwizard()` fixe des valeurs POST par defaut (`reminder_checked`, `email_reminder_checked`, etc.) — toute modification du wizard doit tenir compte de ces valeurs forcees (lignes 113-123).
- `action_editview()` et `action_detailview()` redirigent vers Home si l'utilisateur n'est ni admin ni le proprietaire du record (lignes 232-243).
