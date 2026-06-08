# LanguageManager.php

**Chemin :** `include/SugarObjects/LanguageManager.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Gestionnaire des fichiers de langue des modules SuiteCRM. Cree et met en cache les fichiers de traduction par module en fusionnant les chaines des templates SugarObject utilises. Appele depuis `VardefManager::createVardef()`.

## Role technique

Classe statique. `createLanguageFile()` verifie si le cache existe et, si non (ou en mode developpeur), charge les chaines des templates via `loadTemplateLanguage()` puis persiste via `refreshLanguage()`. Utilise un cache statique `$createdModules` pour eviter les reconstructions multiples dans la meme requete.

---

## Dependances cles

- **Imports principaux :**
  - `translated_prefix.php` (meme repertoire) — prefixes de traduction
  - `$GLOBALS['sugar_config']['default_language']` — langue par defaut
  - Systeme de cache fichier Sugar (`sugar_cached()`)

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `LanguageManager` | classe statique | Gestionnaire de langue des modules |
| `createLanguageFile(string, array, bool): void` | methode | Cree le cache de langue d'un module |

- **Consommateurs identifies :** `VardefManager::createVardef()`

## Relations cles

- **Appele par :** `VardefManager`
- **Appelle :** `loadTemplateLanguage()`, `refreshLanguage()`, systeme de cache
- **Position dans le flux global :** generation des fichiers de langue caches lors du chargement des vardefs

---

## Points d'attention

- En mode developpeur, force la reconstruction. Le corps complet de la classe n'a pas ete entierement lu — methodes internes (`loadTemplateLanguage`, `refreshLanguage`) sont INCONNU au-dela de la signature visible.
