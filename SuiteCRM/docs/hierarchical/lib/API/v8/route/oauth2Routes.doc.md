# Fichier : oauth2Routes.php

**Chemin :** `lib/API/v8/route/oauth2Routes.php`
**Type :** PHP — configuration (routes)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la route OAuth2 de l'API v8 : un unique endpoint `POST /oauth/access_token` routé vers `OAuth2Controller::authenticate()`. C'est le seul endpoint de l'API accessible sans token Bearer valide.

**Type :** configuration

---

## Ce que ce fichier configure

| Route | Verbe | Handler |
|---|---|---|
| `/oauth/access_token` | POST | `OAuth2Controller:authenticate` |

---

## Interactions

- **Consomme :** `OAuth2Controller` (résolu via DI)
- **Inclus par :** INCONNU — bootstrap de l'application API

---

## Notes

- Cette route ne passe PAS par le middleware `ResourceServer` (sinon l'authentification serait impossible).
- Les grants supportés sont `password` et `client_credentials` (configurés dans `lib/API/v8/container/AuthorizationServer.php`).
