# slim.php

**Chemin :** `Api/Core/Config/slim.php`
**Type :** PHP (fichier de configuration retournant un tableau)
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Fichier de configuration des parametres du framework Slim. Retourne un tableau associatif de settings injecte dans le conteneur Slim lors du bootstrap de l'application.

## Responsabilites

- Activer l'affichage des details d'erreurs (`displayErrorDetails => true`)
- Activer la resolution des routes avant l'execution des middlewares (`determineRouteBeforeAppMiddleware => true`)
- Desactiver l'ajout automatique de l'en-tete `Content-Length` (`addContentLengthHeader => false`)
- Fusionner ces parametres avec d'eventuels overrides provenant du dossier custom (`custom/application/Ext/Api/V8/slim.php`)

## Dependances internes

- `Api\Core\Loader\CustomLoader` — utilise `CustomLoader::mergeCustomArray()` pour fusionner les parametres avec le fichier custom correspondant

## Exports / Points d'entree

- Retourne un tableau PHP (`array`) avec la cle `settings` contenant les parametres Slim
- Consomme par `ContainerLoader::configure()` via `ConfigResolver::loadFiles()` (chemin reference dans `ApiConfig::$slimSettings`)

## Notes techniques

- `displayErrorDetails => true` est active en dur — a desactiver en production pour eviter la fuite d'informations.
- L'appel `CustomLoader::mergeCustomArray($array, basename(__FILE__))` permet aux integrateurs de surcharger ces parametres via `custom/application/Ext/Api/V8/slim.php` sans modifier le core.
- Consomme par les 13 fichiers qui utilisent `CustomLoader` (pattern de customisation SuiteCRM).
