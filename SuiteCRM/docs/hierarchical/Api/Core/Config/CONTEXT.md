# 📁 Config

**Chemin :** `Api/Core/Config/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient la configuration centrale du noyau de l'API SuiteCRM. Il déclare les chemins vers tous les fichiers de configuration (Slim settings, services DI, routes), les chemins des clés OAuth2, et les paramètres de l'application Slim (CORS, headers, debug).

## ⚙️ Responsabilité technique
Deux fichiers : `ApiConfig.php` (classe statique pure registre de configuration) et `slim.php` (configuration de l'application Slim). `ApiConfig` est le point d'entrée consulté par `ContainerLoader` et `RouteLoader` au démarrage pour obtenir les listes de fichiers à charger.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ApiConfig.php` | Classe statique : registre des chemins de config (Slim, services DI, routes) et des constantes de clés OAuth2 | [→ fiche](ApiConfig.doc.md) |
| `slim.php` | Configuration des settings Slim (displayErrorDetails, routeBeforeMiddleware, contentLength) avec surcharge custom | [→ fiche](slim.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\Core\Loader\CustomLoader` (pour la surcharge de `slim.php`)
- **Expose :** `ApiConfig::getSlimSettings()`, `getContainers()`, `getRoutes()`, `getDebugExceptions()`, constantes `OAUTH2_PRIVATE_KEY`/`OAUTH2_PUBLIC_KEY` — consommés par `ContainerLoader`, `RouteLoader`, `ErrorResponse`, `middlewares.php`
- **Flux typique :** `ContainerLoader::configure()` appelle `ApiConfig::getSlimSettings()` → obtient le chemin de `slim.php` → `ConfigResolver::loadFiles()` charge les settings → `Slim\Container` instancié.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Trouver les chemins des fichiers de configuration API | [`ApiConfig.php`](ApiConfig.doc.md) |
| Modifier les settings Slim (debug, CORS) | [`slim.php`](slim.doc.md) |

---

## ⚠️ Zones INCONNU
- `ApiConfig::$debugExceptions` codé en dur à `false` — pas de configuration dynamique.
- `slim.php` : `displayErrorDetails: true` en dur — risque en production.
