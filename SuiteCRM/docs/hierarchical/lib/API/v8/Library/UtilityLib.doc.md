# Fichier : UtilityLib.php

**Chemin :** `lib/API/v8/Library/UtilityLib.php`
**Type :** PHP — service / helper
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Bibliothèque utilitaire offrant des méthodes de connexion (`login`), déconnexion (`logout`) et d'informations serveur (`getServerInfo`) pour l'API v8. Encapsule les appels à `AuthenticationController` de SuiteCRM pour authentifier un utilisateur par username/password.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `SuiteCRM\Utility\Paths` | Résolution du chemin projet |
| `AuthenticationController` (require_once) | Contrôleur d'authentification SuiteCRM |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `UtilityLib` | classe | Helper utilitaire API v8 |
| `login($postData)` | méthode publique | Authentifie un utilisateur, retourne `['loginApproved' => bool, 'userId' => string\|null]` |
| `logout()` | méthode publique | Déconnecte l'utilisateur courant, retourne `[]` |
| `getServerInfo()` | méthode publique | Retourne des infos serveur (actuellement vide `[]`) |

---

## Interactions

**Appelé par :** INCONNU — aucun consommateur identifié dans `lib/API/v8/`. Peut être utilisé depuis d'autres parties du code ou des tests.

**Appelle :**
- `AuthenticationController::login()` avec `['passwordEncrypted' => false]`
- `AuthenticationController::logout()`
- `\User::retrieve_user_id()` pour récupérer l'ID utilisateur

---

## Notes

- `getServerInfo()` retourne un tableau vide — fonctionnalité non implémentée (ligne 88).
- Le password est passé en clair (`passwordEncrypted => false`) — la sécurité du transport dépend de HTTPS.
- Cette classe semble préfigurer une implémentation d'authentification alternative à OAuth2, mais son usage actuel est INCONNU.
