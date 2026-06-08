# Fichier : ModuleController.php (container)

**Chemin :** `lib/API/v8/container/ModuleController.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory de conteneur Slim qui instancie `ModuleController` et injecte le logger. Enregistre le service sous la clé `'ModuleController'` dans le container DI. Ce service est résolu par Slim à chaque appel de route module.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `ModuleController` | `SuiteCRM\API\v8\Controller\ModuleController` | `$container`, `LoggerInterface` |

---

## Interactions

- **Produit :** `ModuleController` — utilisé par toutes les routes dans `moduleRoutes.php`
- **Consomme :** `Psr\Log\LoggerInterface`
