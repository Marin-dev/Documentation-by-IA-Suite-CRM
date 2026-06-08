# controller.php

**Chemin :** `modules/Users/controller.php`
**Type :** PHP (Controller)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Contrôleur HTTP du module Users. Gère les actions spécifiques au module (suppression, réinitialisation des préférences, assistant de création, sauvegarde FTS, vues edit/detail) en étendant `SugarController`.

## Type
controller

## Dépendances clés
- `SugarController` — classe parente du framework
- `include/OutboundEmail/OutboundEmail.php` — chargé en tête de fichier
- `modules/UserPreferences/UserPreference.php` — chargé en tête de fichier
- `BeanFactory`, `SugarApplication`, `SugarThemeRegistry` — framework SuiteCRM

## Exports / Symboles principaux
- `class UsersController extends SugarController`
- `action_resetPreferences()` — réinitialise les préférences d'un utilisateur (ligne 56)
- `action_delete()` — supprime un utilisateur (passage en Inactive + mark_deleted) (ligne 74)
- `action_wizard()` — affiche la vue wizard (ligne 104)
- `action_saveuserwizard()` — sauvegarde les données de l'assistant de premier démarrage (ligne 109)
- `action_saveftsmodules()` — sauvegarde la liste des modules FTS désactivés (ligne 222)
- `action_editview()` — accès contrôlé à la vue d'édition (ligne 229)
- `action_detailview()` — accès contrôlé à la vue de détail (ligne 237)

## Interactions
- **Appelé par :** dispatcher HTTP SuiteCRM (index.php via SugarApplication)
- **Appelle :** `User::resetPreferences()`, `User::save()`, `User::mark_deleted()`, `loadBean('EAPM')`, `SugarApplication::redirect()`
- **Position dans le flux global :** Point d'entrée HTTP pour toutes les actions CRUD et de configuration du module Users

## Notes
- `action_delete()` vérifie que l'utilisateur courant ne se supprime pas lui-même (ligne 78).
- `action_editview()` et `action_detailview()` redirigent vers Home si l'utilisateur n'est ni admin ni le propriétaire du compte (lignes 232-243).
- `action_saveuserwizard()` accepte un paramètre `whatnext` (POST) pour router vers différentes pages après l'assistant (ligne 204).
