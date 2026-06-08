# SugarConfig.php

**Chemin :** `include/SugarObjects/SugarConfig.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Gestionnaire de configuration global de SuiteCRM. Fournit un acces unifie et mis en cache a toutes les valeurs de `$GLOBALS['sugar_config']`, qui est le tableau de configuration central charge depuis `config.php` et `config_override.php` au demarrage.

## Role technique

Singleton avec cache interne (`$_cached_values`). `get(key, default)` utilise `SugarArray::staticGet()` pour supporter les cles avec notation pointee (`'calendar_sync.run_async'`). `clearCache()` invalide tout ou partie du cache.

---

## Dependances cles

- **Imports principaux :**
  - `SugarArray` (`include/utils/array_utils.php`) — acces aux tableaux imbriques par cle pointee
  - `$GLOBALS['sugar_config']` — source de verite de la configuration

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `SugarConfig` | classe singleton | Gestionnaire de config |
| `getInstance(): SugarConfig` | methode statique | Retourne le singleton |
| `get(string, mixed): mixed` | methode | Lit une cle de config avec cache |
| `clearCache(?string): void` | methode | Invalide le cache (global ou par cle) |

- **Consommateurs identifies :** `CalendarSyncConfig`, pratiquement tous les modules SuiteCRM

## Relations cles

- **Appele par :** partout dans SuiteCRM
- **Appelle :** `SugarArray::staticGet()`, `$GLOBALS['sugar_config']`
- **Position dans le flux global :** acces en lecture a toute la configuration systeme

---

## Points d'attention

- `get()` lit `$GLOBALS['sugar_config']` a la premiere demande puis cache — si `sugar_config` est modifie apres le premier appel, le cache est obsolete jusqu'a `clearCache()`.
- Classe singleton sans protection thread-safety (PHP est single-threaded, pas de probleme en pratique).
