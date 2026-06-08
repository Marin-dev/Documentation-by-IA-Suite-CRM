# 📄 globals.php

**Chemin :** `Api/V8/Config/services/globals.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Expose les ressources globales PHP de SuiteCRM comme services du conteneur DI : la configuration applicative (`$sugar_config`) et l'instance de base de données (`DBManager`).

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\Core\Loader\CustomLoader` | Fusion avec services globaux personnalisés |
| `$sugar_config` (global PHP) | Configuration applicative SuiteCRM |
| `DBManagerFactory::getInstance()` | Singleton de connexion à la base de données |

---

## Services enregistrés

| Clé DI | Source | Description |
|---|---|---|
| `'suiteConfig'` | `global $sugar_config` | Configuration PHP de SuiteCRM (array) |
| `DBManager::class` | `DBManagerFactory::getInstance()` | Instance singleton de connexion à la DB |

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **`suiteConfig`** : consommé par `middlewares.php` (via `$GLOBALS['sugar_config']`) — INCONNU si d'autres services le consomment via le conteneur
- **`DBManager::class`** : consommé par `services.php` dans la factory de `BeanManager`

---

## Notes

- Ces deux services "pontent" les globales PHP vers le système DI propre.
- L'accès à `DBManagerFactory` (classe SuiteCRM native) est fait sans import PHP — disponible globalement dans l'environnement SuiteCRM.
- `suiteConfig` bridge `$sugar_config` global, mais `middlewares.php` accède directement à `$GLOBALS['sugar_config']` — légère incohérence d'usage.
