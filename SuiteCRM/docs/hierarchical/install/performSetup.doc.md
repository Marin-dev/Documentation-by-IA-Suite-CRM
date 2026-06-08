# Fichier : performSetup.php

**Chemin :** `install/performSetup.php`
**Type :** installer (execution de l'installation)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Orchestre l'execution effective de l'installation de SuiteCRM : creation des tables, ecriture de la configuration, initialisation des modules, etc. C'est l'etape finale du wizard qui applique toutes les configurations collectees. Ecrit les statuts de progression dans `install/status.json`.

## Role technique
Script include par `install.php` avec `$GLOBALS['installing'] = true`. Desactive la mise en tampon de sortie pour affichage en temps reel. Definit `installStatus()` pour ecrire la progression JSON. Charge `TableDictionary.php` et met en pause le `TrackerManager`. Limite d'execution fixee a 3600 secondes.

---

## Dependances cles
- **Imports principaux :**
  - `install/install_utils.php` — toutes les fonctions utilitaires
  - `modules/TableDictionary.php` — dictionnaire des tables
  - `TrackerManager` (global) — gestion traceurs (mis en pause)
- **Variables de contexte :** `$mod_strings`, `$install_script`
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `installStatus($msg, $cmd, $overwrite, $before)` | Ecrit/accumule les messages de statut dans `install/status.json` |

## Interactions
- **Appele par :** `install.php` (include, etape finale)
- **Appelle :**
  - `install/install_utils.php` (toutes fonctions)
  - `modules/TableDictionary.php`
  - `install/suite_install/suite_install.php` (INCONNU : verifier si appele ici ou dans install.php)

---

## Notes
- `ob_implicit_flush()` (ligne 69) force le flush apres chaque echo pour affichage temps reel.
- `set_time_limit(3600)` (ligne 68) — l'installation peut prendre jusqu'a 1 heure.
- Le fichier `install/status.json` est utilise par `installConfig.php::startStatusReader()` pour la progression AJAX.
- Le detail des operations effectuees (creation tables, insert config...) est dans la suite du fichier non lue ici — INCONNU complet de toutes les etapes.
