# Fichier : SchemaController.php (container)

**Chemin :** `lib/API/v8/container/SchemaController.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory de conteneur Slim qui instancie `SchemaController` et injecte le logger. Enregistre le service sous la clé `'SchemaController'`.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `SchemaController` | `SuiteCRM\API\v8\Controller\SchemaController` | `$container`, `LoggerInterface` |

---

## Interactions

- **Produit :** `SchemaController` — utilisé par les routes `GET /v8/schema` et `GET /v8/swagger.json`
- **Consomme :** `Psr\Log\LoggerInterface`
