# Fichier : oauth2.php

**Chemin :** `lib/API/v8/callable/oauth2.php`
**Type :** PHP — configuration / middleware callable
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Fichier de configuration Slim qui enregistre le middleware `ResourceServer` sur l'application. Une seule instruction : `$app->add('ResourceServer')`. Cela signifie que toutes les routes de l'application passent par le middleware de validation du token OAuth2 avant d'être traitées.

**Type :** configuration

---

## Ce que ce fichier configure

Enregistre le middleware `ResourceServer` (résolu depuis le container DI sous la clé `'ResourceServer'`) sur l'instance Slim `$app`. Ce middleware valide le JWT Bearer token sur chaque requête entrante et rejette les requêtes non authentifiées.

---

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `$app->add('ResourceServer')` | clé container `ResourceServer` | Toutes les routes nécessitent un token valide |

---

## Interactions

- **Consomme :** `lib/API/v8/container/ResourceServer.php` (factory du middleware)
- **Inclus par :** INCONNU — probablement par le bootstrap de l'application API (point d'entrée non identifié dans `lib/API/v8/`)

---

## Notes

- Ce fichier opère sur la variable `$app` (Slim App) qui doit être définie dans le contexte d'inclusion.
- Sans ce middleware, toutes les routes seraient accessibles sans authentification.
