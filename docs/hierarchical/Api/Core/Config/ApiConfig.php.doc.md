# ApiConfig.php

**Chemin :** `Api/Core/Config/ApiConfig.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Registre central de configuration de l'API SuiteCRM. Centralise les chemins vers les fichiers de configuration Slim, les conteneurs de services et les fichiers de routes, ainsi que les chemins des cles OAuth2.

## Responsabilites

- Fournir la liste des fichiers de configuration Slim (`slim.php`)
- Fournir la liste des fichiers de conteneurs de services DI (`Api/V8/Config/services.php`)
- Fournir la liste des fichiers de routes (`Api/V8/Config/routes.php`)
- Exposer les chemins des cles OAuth2 privee et publique
- Controler l'activation du mode debug des exceptions (`$debugExceptions`)

## Dependances internes

- Aucune dependance interne (classe autonome, pas d'import)

## Exports / Points d'entree

- `ApiConfig::getSlimSettings()` — retourne le tableau des fichiers de configuration Slim
- `ApiConfig::getContainers()` — retourne le tableau des fichiers de services DI
- `ApiConfig::getRoutes()` — retourne le tableau des fichiers de routes
- `ApiConfig::getDebugExceptions()` — retourne le flag debug exceptions (toujours `false` en l'etat)
- `ApiConfig::OAUTH2_PRIVATE_KEY` — constante : chemin vers la cle privee OAuth2 (`Api/V8/OAuth2/private.key`)
- `ApiConfig::OAUTH2_PUBLIC_KEY` — constante : chemin vers la cle publique OAuth2 (`Api/V8/OAuth2/public.key`)

## Notes techniques

- Pattern registre statique : tous les membres et methodes sont statiques, pas d'instanciation.
- L'attribut `#[\AllowDynamicProperties]` indique une compatibilite avec PHP 8.2+ tout en gardant la compatibilite descendante (commentaire "we still support 5.5.9" — ligne 7, probablement obsolete).
- Consomme par `ContainerLoader` (`Api/Core/Loader/ContainerLoader.php`) et `RouteLoader` (`Api/Core/Loader/RouteLoader.php`), ainsi que `Api/V8/Config/services/middlewares.php` et `Api/V8/JsonApi/Response/ErrorResponse.php`.
- `$debugExceptions` est toujours `false` — aucun mecanisme d'activation dynamique visible dans ce fichier ; activation eventuellement via surcharge INCONNU.
