# 📄 RouteLoader.php

**Chemin :** `Api/Core/Loader/RouteLoader.php`
**Type :** `PHP`
**Catégorie :** loader
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel

Enregistre toutes les routes de l'API dans l'instance Slim. Il itère sur la liste des fichiers de routes déclarés dans `ApiConfig` et les inclut séquentiellement dans le contexte de l'application, ce qui a pour effet d'enregistrer les routes via les appels `$app->get()`, `$app->post()`, etc. présents dans ces fichiers.

## ⚙️ Rôle technique

Classe non-statique (contrairement à `ContainerLoader`) avec une seule méthode publique `configureRoutes(App $app)`. Pour chaque chemin de route retourné par `ApiConfig::getRoutes()`, elle vérifie l'existence du fichier via `ConfigResolver::isFileExist()` (lève une `RuntimeException` si absent ou illisible), puis l'inclut avec `require`. Les fichiers de routes reçoivent `$app` en scope via le `require`.

---

## 📥 Entrées / Dépendances

- **Imports principaux :**
  - `Api\Core\Config\ApiConfig` — fournit la liste des fichiers de routes
  - `Api\Core\Resolver\ConfigResolver` — vérifie l'existence/lisibilité des fichiers
  - `Slim\App` — instance passée en paramètre, utilisée comme scope pour les fichiers de routes

## 📤 Sorties / Exports

| Symbole | Type | Rôle |
|---|---|---|
| `configureRoutes(App $app)` | méthode publique | Charge tous les fichiers de routes dans l'instance Slim |

**Consommateurs identifiés dans le repo :**
- `Api/Core/app.php` — instancie `RouteLoader` et appelle `configureRoutes($app)`

## 🔗 Relations clés

- **Appelé par :** `Api/Core/app.php` (lignes 25-26)
- **Appelle :** `ApiConfig::getRoutes()`, `ConfigResolver::isFileExist()`, `require $route`
- **Position dans le flux global :** exécuté après l'initialisation du conteneur DI, enregistre les routes avant que Slim commence à traiter les requêtes

---

## 💡 Points d'attention

- Contrairement à `ContainerLoader`, cette classe est instanciée (non statique) — le commentaire dans `ContainerLoader` explique pourquoi ce choix a été fait ("closure shouldn't be created in static context under PHP7").
- `ConfigResolver::isFileExist()` lève une `RuntimeException` si le fichier est absent — une route manquante fait planter le démarrage entier de l'API.
- Les fichiers de routes inclus doivent avoir `$app` disponible dans leur scope pour fonctionner.
