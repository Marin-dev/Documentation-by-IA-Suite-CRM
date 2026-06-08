# CustomLoader.php

**Chemin :** `Api/Core/Loader/CustomLoader.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Utilitaire de chargement et de fusion des personnalisations SuiteCRM pour l'API. Permet aux integrateurs de surcharger les tableaux de configuration et d'ajouter des routes personnalisees sans modifier le code core, via le repertoire `custom/application/Ext/Api/V8/`.

## Responsabilites

- Fusionner un tableau de configuration avec un eventuel tableau custom charge depuis le disque (`mergeCustomArray`)
- Charger et executer un fichier de routes personnalisees dans le contexte d'une application Slim (`loadCustomRoutes`)
- Fournir une fusion recursives de tableaux multidimensionnels (`arrayMerge`)
- Gerer et exposer le code d'erreur de la derniere operation (`getLastError`)
- Permettre la reconfiguration du chemin custom (`setCustomPath`, `getCustomPath`)

## Dependances internes

- `LoggerManager` — classe SuiteCRM globale pour la journalisation (debug si fichier custom absent)
- `Slim\App` — utilisee comme type parametre dans `loadCustomRoutes`
- `Exception` (PHP natif)

## Exports / Points d'entree

- `CustomLoader::mergeCustomArray(array $array, string $customFile): array` — fusionne le tableau passe avec le fichier custom correspondant ; retourne le tableau original si le fichier n'existe pas
- `CustomLoader::loadCustomRoutes(App $app, string $customRoutesFile = 'Config/routes.php'): App` — inclut le fichier de routes custom dans le contexte de `$app`
- `CustomLoader::arrayMerge(array $arrays): array` — fusion recursive de tableaux multidimensionnels (gere les cles indexees et associatives)
- `CustomLoader::getLastError(): int` — retourne et remet a zero le dernier code d'erreur
- `CustomLoader::setCustomPath(string)` / `getCustomPath(): string` — lecture/ecriture du chemin de base des customisations

### Codes d'erreur
| Constante | Valeur | Signification |
|---|---|---|
| `ERR_NO_ERROR` | 0 | Pas d'erreur |
| `ERR_FILE_NOT_FOUND` | 1 | Fichier de configuration custom introuvable |
| `ERR_ROUTE_FILE_NOT_FOUND` | 2 | Fichier de routes custom introuvable |
| `ERR_WRONG_CUSTOM_FORMAT` | 3 | Le fichier custom ne retourne pas un tableau |

## Notes techniques

- Chemin custom par defaut : `custom/application/Ext/Api/V8/` (relatif a la racine SuiteCRM).
- L'absence de fichier custom est silencieuse (log debug uniquement) ; seule une mauvaise format (`ERR_WRONG_CUSTOM_FORMAT`) leve une `Exception`.
- Consomme par : `Api/Core/Config/slim.php` et les 11 fichiers sous `Api/V8/Config/` (services, routes, etc.).
- `loadCustomRoutes` utilise `include` (et non `require`) — l'execution continue meme si le fichier est absent.
- Auteur declare dans le docblock : `@author gyula`.
