# ConfigResolver.php

**Chemin :** `Api/Core/Resolver/ConfigResolver.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Utilitaire de chargement et de fusion des fichiers de configuration PHP. Charge une liste de fichiers retournant des tableaux, les fusionne en un seul tableau plat, et verifie leur accessibilite.

## Responsabilites

- Construire le chemin absolu de chaque fichier en prefixant avec `$GLOBALS['BASE_DIR']`
- Verifier l'existence et la lisibilite de chaque fichier (`isFileExist`)
- Inclure chaque fichier via `require` et valider qu'il retourne bien un tableau
- Fusionner tous les tableaux charges en un seul via `array_reduce` + `array_merge`
- Lever des exceptions typees en cas de fichier invalide ou illisible

## Dependances internes

- `$GLOBALS['BASE_DIR']` — variable globale definie dans `include/entryPoint.php` (initialise dans `app.php`)
- Aucune autre dependance interne

## Exports / Points d'entree

- `ConfigResolver::loadFiles(array $files): array` — charge et fusionne les fichiers de configuration ; leve `\InvalidArgumentException` si un fichier ne retourne pas un tableau
- `ConfigResolver::isFileExist(string $file): bool` — verifie existence + lisibilite ; leve `\RuntimeException` si le fichier est absent ou illisible

### Consommateurs identifies
| Fichier | Usage |
|---|---|
| `Api/Core/Loader/ContainerLoader.php` | Charge slim settings et services |
| `Api/Core/Loader/RouteLoader.php` | Verifie les fichiers de routes avant inclusion |

## Notes techniques

- Le commentaire ligne 35 ("since we support 5.5.9, we can't use splat op here") indique une compatibilite historique avec PHP 5.5.9 — `array_reduce` est utilise a la place de `array_merge(...$configs)`.
- Bogue potentiel (ligne 27) : si `$file` n'existe pas, `$config` n'est pas assignee dans l'iteration courante mais la valeur precedente de `$config` persiste — la verification `!is_array($config)` pourrait passer meme si le `require` a ete saute. INCONNU : comportement reel en cas de fichier manquant non-leve par `isFileExist`.
- `isFileExist` leve systematiquement une `\RuntimeException` si le fichier est absent — il n'y a pas de retour `false` silencieux.
- L'attribut `#[\AllowDynamicProperties]` est present sans impact fonctionnel apparent.
