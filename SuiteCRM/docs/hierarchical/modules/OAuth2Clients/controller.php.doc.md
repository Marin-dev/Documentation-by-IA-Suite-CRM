# 📄 controller.php

**Chemin :** `modules/OAuth2Clients/controller.php`
**Type :** PHP — controller
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Contrôleur du module OAuth2Clients. Restreint l'accès au module aux administrateurs uniquement. Fournit des actions pour les différentes vues d'édition selon le type de grant.

## Rôle technique

Classe `OAuth2ClientsController` héritant de `SugarController`. Surcharge `process()` pour bloquer les non-admins (`$this->hasAccess = false`). Expose 3 actions d'édition redirigeant vers la vue `edit` avec des defs spécifiques.

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuth2ClientsController` | classe | Contrôleur admin-only du module OAuth2Clients |
| `process()` | méthode | Bloque les non-admins |
| `action_EditViewPassword()` | méthode | Vue édition grant Password |
| `action_EditViewCredentials()` | méthode | Vue édition grant Client Credentials |
| `action_EditViewAuthorizationCode()` | méthode | Vue édition grant Authorization Code |

---

## Relations clés

- **Appelé par :** framework MVC SugarCRM
- **Position dans le flux global :** gestion admin des clients OAuth2

---

## Notes

- Accès strictement admin — tout utilisateur non-admin est bloqué dès `process()`.
