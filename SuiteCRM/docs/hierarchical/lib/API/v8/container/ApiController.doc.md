# Fichier : ApiController.php (container)

**Chemin :** `lib/API/v8/container/ApiController.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory de conteneur Slim qui instancie `ApiController` (classe de base) et injecte le logger. Enregistre le service sous la clé `'ApiController'` dans le container DI.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `ApiController` | `SuiteCRM\API\v8\Controller\ApiController` | `$container`, `LoggerInterface` |

---

## Interactions

- **Produit :** `ApiController` (classe de base, rarement utilisée directement)
- **Consomme :** `Psr\Log\LoggerInterface` (via `LoggerInterface.php`)
