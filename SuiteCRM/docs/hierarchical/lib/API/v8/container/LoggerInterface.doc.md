# Fichier : LoggerInterface.php (container)

**Chemin :** `lib/API/v8/container/LoggerInterface.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\Utility\SuiteLogger` et l'enregistre dans le container DI sous la clé `Psr\Log\LoggerInterface::class`. C'est le logger partagé par tous les contrôleurs et services de l'API v8.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Description |
|---|---|---|
| `Psr\Log\LoggerInterface::class` | `SuiteCRM\Utility\SuiteLogger` | Logger PSR-3 de SuiteCRM |

---

## Interactions

**Consommé par :** tous les containers de contrôleurs (`ApiController`, `ModuleController`, `OAuth2Controller`, `SchemaController`), `JsonApi`, `Links`, `Resource`, `SuiteBeanResource`, `ResourceIdentifier`, `Relationship`
