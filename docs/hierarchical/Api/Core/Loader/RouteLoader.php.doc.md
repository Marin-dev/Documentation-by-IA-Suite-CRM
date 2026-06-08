# RouteLoader.php

**Chemin :** `Api/Core/Loader/RouteLoader.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Responsable du chargement des fichiers de definition de routes dans l'application Slim. Itere sur la liste des fichiers de routes declares dans `ApiConfig` et les inclut si accessibles.

## Responsabilites

- Recuperer la liste des fichiers de routes depuis `ApiConfig::getRoutes()`
- Verifier l'existence et la lisibilite de chaque fichier via `ConfigResolver::isFileExist()`
- Inclure (`require`) chaque fichier de routes valide dans le contexte de l'application Slim

## Dependances internes

- `Api\Core\Config\ApiConfig` — fournit la liste des fichiers de routes (`Api/V8/Config/routes.php` par defaut)
- `Api\Core\Resolver\ConfigResolver` — verifie l'accessibilite des fichiers avant inclusion
- `Slim\App` (dependance externe, framework Slim 3) — recoit l'instance applicative pour l'enregistrement des routes

## Exports / Points d'entree

- `RouteLoader::configureRoutes(App $app): void` — methode d'instance ; charge tous les fichiers de routes declares
- Consomme par : `Api/Core/app.php` (ligne 25-26 : instanciation puis appel `configureRoutes($app)`)

## Notes techniques

- Contrairement a `ContainerLoader`, `RouteLoader` est instancie (methode non statique) — coherent avec le commentaire dans `ContainerLoader` sur l'usage sans DI.
- `ConfigResolver::isFileExist()` leve une `\RuntimeException` si le fichier est absent ou illisible — une route manquante provoque donc une exception non geree ici.
- L'attribut `#[\AllowDynamicProperties]` est present sans impact fonctionnel apparent.
- Les fichiers de routes inclus ont acces a la variable `$app` via le scope de la methode (pas de passage explicite a `require`) — INCONNU : verifier si les fichiers de routes utilisent `$app` ou une autre convention de declaration.
