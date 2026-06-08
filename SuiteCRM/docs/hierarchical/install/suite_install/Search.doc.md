# Fichier : Search.php

**Chemin :** `install/suite_install/Search.php`
**Type :** installer (configuration moteur de recherche)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure le moteur de recherche de SuiteCRM lors de l'installation : parametres du SearchWrapper (pagination, moteur par defaut) et configuration ElasticSearch.

## Role technique
Expose deux fonctions : `install_search()` configure `$sugar_config['search']` avec UnifiedSearch et BasicSearchEngine par defaut. `install_es()` configure ElasticSearch (INCONNU : detail de la configuration ES).

---

## Dependances cles
- **Imports principaux :**
  - `modules/Administration/Administration.php`
  - `$sugar_config` (global)
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_search()` | Configure SearchWrapper avec UnifiedSearch/BasicSearchEngine |
| `install_es()` | Configure ElasticSearch (INCONNU : detail) |

**Parametres configures par `install_search()` :**
- `search.controller = 'UnifiedSearch'`
- `search.defaultEngine = 'BasicSearchEngine'`
- `search.pagination = {min:10, max:50, step:10}`

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (lignes 38-39)
- **Appelle :** `write_array_to_file()` (INCONNU : verifier)

---

## Notes
- SuiteCRM supporte deux moteurs : BasicSearchEngine (SQL) et ElasticSearch. BasicSearch est le defaut.
- La pagination par defaut est 10/50/10 (min/max/step).
