# 📁 Loader

**Chemin :** `Api/Core/Loader/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les loaders du bootstrap de l'API SuiteCRM. Ils initialisent le conteneur DI Slim, enregistrent les routes, et permettent aux intégrateurs d'étendre la configuration via des fichiers custom sans modifier le core.

## ⚙️ Responsabilité technique
Trois classes : `ContainerLoader` (initialise le conteneur Slim), `RouteLoader` (enregistre les routes), `CustomLoader` (fusion de configuration custom via tableaux ou inclusion de fichiers). Tous utilisent `ConfigResolver` et `ApiConfig` pour résoudre les chemins. Le pattern custom permet l'extension sans modification du core.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ContainerLoader.php` | Initialise et retourne le conteneur DI Slim avec les settings et services configurés | [→ fiche](ContainerLoader.doc.md) |
| `RouteLoader.php` | Enregistre toutes les routes API dans l'instance Slim depuis les fichiers déclarés dans `ApiConfig` | [→ fiche](RouteLoader.doc.md) |
| `CustomLoader.php` | Mécanisme de surcharge : fusionne la config avec des fichiers custom dans `custom/application/Ext/Api/V8/` | [→ fiche](CustomLoader.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\Core\Config\ApiConfig`, `Api\Core\Resolver\ConfigResolver`, `Slim\App`, `Slim\Container`, `LoggerManager`
- **Expose :** `ContainerLoader::configure()` et `RouteLoader::configureRoutes()` appelés depuis `Api/Core/app.php` ; `CustomLoader::mergeCustomArray()` et `loadCustomRoutes()` appelés dans tous les fichiers de config V8
- **Flux typique :** `app.php` appelle `ContainerLoader::configure()` → conteneur créé ; puis `RouteLoader::configureRoutes($app)` → routes enregistrées.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'initialisation du conteneur DI | [`ContainerLoader.php`](ContainerLoader.doc.md) |
| Comprendre l'enregistrement des routes | [`RouteLoader.php`](RouteLoader.doc.md) |
| Ajouter une configuration custom sans modifier le core | [`CustomLoader.php`](CustomLoader.doc.md) |

---

## ⚠️ Zones INCONNU
- `CustomLoader::arrayMerge` : comportement spécial des clés entières (toujours appendées, jamais écrasées).
- `CustomLoader::$lastError` : réinitialisé à chaque appel à `getLastError()` — effet de bord documenté.
