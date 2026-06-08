# VardefManager.php

**Chemin :** `include/SugarObjects/VardefManager.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Gestionnaire des definitions de variables (vardefs) des modules SuiteCRM. Charge, cache, fusionne et rafraichit les definitions de champs, relations et index d'un objet/module. Constitue le mecanisme fondamental de description du schema de donnees dans SuiteCRM.

## Role technique

Classe statique. `createVardef()` charge les templates SugarObject et les vardefs implementes pour construire la definition complete d'un objet. `loadVardef()` utilise un cache deux niveaux : `sugar_cache` (memoire/APC) et fichier cache (`cache/modules/`). `refreshVardefs()` recharge depuis le systeme de fichiers et reconstruit le cache. Integration avec les champs dynamiques (Studio) via `DynamicField::buildCache()`.

---

## Dependances cles

- **Imports principaux :**
  - `LanguageManager` (implicite) — creation de fichiers de langue
  - `BeanFactory` — resolution des noms de modules
  - `DynamicField` (`modules/DynamicFields/DynamicField.php`) — champs personnalises
  - `TableDictionary` (`modules/TableDictionary.php`) — relations globales

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `VardefManager` | classe statique | Gestionnaire des vardefs |
| `createVardef(string, string, array, mixed): void` | methode | Cree et enregistre les vardefs depuis templates |
| `addTemplate(string, string, string, mixed): void` | methode | Fusionne un template dans les vardefs |
| `loadVardef(string, string, bool, array): void` | methode | Charge les vardefs (avec cache) |
| `refreshVardefs(string, string, ?array, bool, array): void` | methode | Recharge depuis le FS et met en cache |
| `saveCache(string, string, array): void` | methode | Persiste le cache fichier + sugar_cache |
| `clearVardef(?string, ?string): void` | methode | Invalide le cache |
| `getLinkFieldsForModule(string, string): array` | methode | Champs de type `link` d'un module |
| `applyGlobalAccountRequirements(array): array` | methode | Force `account_name` requis si config |

- **Consommateurs identifies :** `vardefs.php` de tous les modules, `BeanFactory`, `SugarBean`

## Relations cles

- **Appele par :** toutes les definitions `vardefs.php` de modules SuiteCRM
- **Appelle :** `DynamicField`, `BeanFactory`, `LanguageManager`, systeme de fichiers cache
- **Position dans le flux global :** fondation du schema de donnees — appele au chargement de tout module

---

## Points d'attention

- En mode developpeur (`inDeveloperMode()` ou `$_SESSION['developerMode']`), force un rechargement systematique — impact fort sur les performances. A ne pas activer en production.
- `cleanVardefs()` supprime silencieusement les champs sans `name` ou `type` — des vardefs mal formates disparaissent sans erreur.
- `applyGlobalAccountRequirements()` peut rendre `account_name` requis globalement via `$GLOBALS['sugar_config']['require_accounts']`.
