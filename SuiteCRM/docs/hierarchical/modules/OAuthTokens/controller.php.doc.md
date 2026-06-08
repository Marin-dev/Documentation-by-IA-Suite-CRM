# 📄 controller.php

**Chemin :** `modules/OAuthTokens/controller.php`
**Type :** PHP — controller
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Contrôleur du module OAuthTokens (OAuth 1.0). Gère la suppression d'un token avec vérification que l'utilisateur est admin ou propriétaire du token.

## Rôle technique

Classe `OAuthTokensController` héritant de `SugarController`. Surcharge `action_delete()` pour vérifier les droits avant la suppression. Surcharge `post_delete()` pour supporter une URL de redirection custom.

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuthTokensController` | classe | Contrôleur des tokens OAuth 1.0 |
| `action_delete()` | méthode | Supprime un token avec vérification admin/propriétaire |
| `post_delete()` | méthode | Redirection post-suppression (URL custom ou défaut) |

---

## Relations clés

- **Appelé par :** framework MVC SugarCRM (action Delete)
- **Appelle :** `ACLController::displayNoAccess()`, `SugarBean::mark_deleted()`
- **Position dans le flux global :** gestion des tokens OAuth 1.0

---

## Notes

- Un utilisateur non-admin ne peut supprimer que ses propres tokens (vérification `assigned_user_id`).
