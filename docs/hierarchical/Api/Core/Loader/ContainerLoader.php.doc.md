# ContainerLoader.php

**Chemin :** `Api/Core/Loader/ContainerLoader.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Responsable de la construction et de la configuration du conteneur d'injection de dependances (DI) Slim. Charge les parametres Slim et enregistre tous les services declares dans les fichiers de configuration.

## Responsabilites

- Charger les parametres Slim via `ConfigResolver::loadFiles()` a partir des chemins declares dans `ApiConfig`
- Instancier le conteneur `Slim\Container` avec ces parametres
- Charger les definitions de services depuis `ApiConfig::getContainers()` et les enregistrer dans le conteneur
- Retourner le conteneur configure pret a etre injecte dans l'application Slim

## Dependances internes

- `Api\Core\Config\ApiConfig` — fournit les listes de fichiers de settings Slim et de conteneurs de services
- `Api\Core\Resolver\ConfigResolver` — charge et fusionne les fichiers de configuration PHP
- `Slim\Container` (dependance externe, framework Slim 3)
- `Psr\Container\ContainerInterface` (interface PSR-11)

## Exports / Points d'entree

- `ContainerLoader::configure()` — methode statique, retourne un `ContainerInterface` (instance de `Slim\Container`) pret a l'emploi
- Consomme par : `Api/Core/app.php` (ligne 23 : `ContainerLoader::configure()`)

## Notes techniques

- Pattern factory statique : la methode `configure()` est statique ; le commentaire interne (ligne 21) note que pour un usage sans DI il faudrait instancier la classe.
- Les services sont enregistres par iteration sur le tableau retourne par `ConfigResolver::loadFiles(ApiConfig::getContainers())` — chaque entree est une closure indexee par nom de service.
- L'attribut `#[\AllowDynamicProperties]` est present mais sans impact fonctionnel apparent sur cette classe.
- Couplage fort avec `Slim\Container` (Slim 3) — une migration vers Slim 4 necessiterait une refonte de ce loader.
