# Fichier : schemaRoutes.php

**Chemin :** `lib/API/v8/route/schemaRoutes.php`
**Type :** PHP — configuration (routes)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit les deux routes d'exposition des schémas de l'API v8, routées vers `SchemaController`.

**Type :** configuration

---

## Ce que ce fichier configure

| Route | Verbe | Handler |
|---|---|---|
| `/v8/schema` | GET | `SchemaController:getJsonApiSchema` |
| `/v8/swagger.json` | GET | `SchemaController:getSwaggerSchema` |

---

## Interactions

- **Consomme :** `SchemaController` (résolu via DI)
- **Inclus par :** INCONNU — bootstrap de l'application API

---

## Notes

Ces routes permettent aux clients de découvrir la structure JSON:API (`/v8/schema`) et la documentation Swagger (`/v8/swagger.json`) de l'API.
