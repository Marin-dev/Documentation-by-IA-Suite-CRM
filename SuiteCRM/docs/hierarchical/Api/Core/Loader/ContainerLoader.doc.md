# 📄 ContainerLoader.php

**Chemin :** `Api/Core/Loader/ContainerLoader.php`
**Type :** `PHP`
**Catégorie :** service / loader
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel

Initialise et retourne le conteneur d'injection de dépendances (DI) de l'application API. Il charge les paramètres Slim et les services applicatifs, puis les injecte dans une instance `Slim\Container`. C'est la pièce centrale du bootstrap de l'IoC container.

## ⚙️ Rôle technique

La méthode statique `configure()` :
1. Charge les settings Slim depuis les fichiers déclarés dans `ApiConfig::getSlimSettings()` via `ConfigResolver::loadFiles()`.
2. Instancie un `Slim\Container` avec ces settings.
3. Charge les définitions de services depuis `ApiConfig::getContainers()` et les enregistre dans le conteneur via la syntaxe tableau (`$container[$service] = $closure`).
4. Retourne le conteneur prêt à l'emploi.

---

## 📥 Entrées / Dépendances

- **Imports principaux :**
  - `Api\Core\Config\ApiConfig` — fournit les listes de fichiers de config
  - `Api\Core\Resolver\ConfigResolver` — charge et fusionne les fichiers de config
  - `Psr\Container\ContainerInterface` — interface de typage retour
  - `Slim\Container` — implémentation concrète du conteneur DI Slim 3

## 📤 Sorties / Exports

| Symbole | Type | Rôle |
|---|---|---|
| `configure()` | méthode statique | Construit et retourne le `ContainerInterface` configuré |

**Consommateurs identifiés dans le repo :**
- `Api/Core/app.php` — appelle `ContainerLoader::configure()` pour instancier `\Slim\App`

## 🔗 Relations clés

- **Appelé par :** `Api/Core/app.php` (ligne 23)
- **Appelle :** `ConfigResolver::loadFiles()`, `ApiConfig::getSlimSettings()`, `ApiConfig::getContainers()`, `new Slim\Container()`
- **Position dans le flux global :** exécuté en premier lors du bootstrap, avant l'enregistrement des routes

---

## 💡 Points d'attention

- Le commentaire `// if we want to use this without DI, should create an instance for it` (ligne 21) suggère que le design pourrait évoluer vers une version non-statique.
- Si `ConfigResolver::loadFiles()` lève une exception (fichier manquant ou non-tableau), le bootstrap échoue entièrement.
