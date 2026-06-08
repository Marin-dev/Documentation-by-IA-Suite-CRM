# ⚙️ slim.php (configuration)

**Chemin :** `Api/Core/Config/slim.php`
**Configure :** `Slim Framework (instance App)`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Ce que ce fichier configure

Fichier de configuration des paramètres de base du framework Slim. Il retourne un tableau de settings qui sera passé au constructeur `\Slim\App` via le `ContainerLoader`. Il supporte également un mécanisme de surcharge via `CustomLoader::mergeCustomArray`, permettant à des configurations personnalisées situées dans `custom/application/Ext/Api/V8/slim.php` d'écraser ou compléter ces valeurs.

## 🔑 Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `settings.displayErrorDetails` | `true` | Affiche les détails d'exception dans les réponses d'erreur Slim |
| `settings.determineRouteBeforeAppMiddleware` | `true` | La route est résolue avant l'exécution des middlewares globaux |
| `settings.addContentLengthHeader` | `false` | Désactive l'ajout automatique du header `Content-Length` |

## 🔗 Impacté par / impacte

- **Consommé par :** `Api/Core/Loader/ContainerLoader.php` via `ConfigResolver::loadFiles(ApiConfig::getSlimSettings())`
- **Surcharge possible :** `custom/application/Ext/Api/V8/slim.php` (lu par `CustomLoader::mergeCustomArray`)
- **Import utilisé :** `Api\Core\Loader\CustomLoader` (ligne 3)

## 💡 Points d'attention

- `displayErrorDetails` est à `true` — potentiellement problématique en production car expose les traces d'erreur dans les réponses HTTP.
- La surcharge custom est silencieuse si le fichier n'existe pas (`ERR_FILE_NOT_FOUND` logué en debug uniquement).
