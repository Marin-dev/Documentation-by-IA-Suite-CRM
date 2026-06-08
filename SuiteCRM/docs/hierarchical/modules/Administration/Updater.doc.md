# Updater.php

**Chemin :** `modules/Administration/Updater.php`
**Type :** PHP (view / page parametres)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page de configuration des mises a jour automatiques SuiteCRM. Permet de choisir entre verifications automatiques et manuelles, et de configurer l'envoi de statistiques d'usage ("beat"). Affiche les mises a jour disponibles en comparant la version actuelle avec les versions listees dans la licence.

## Role technique
Script procedral utilisant XTemplate (non Smarty). En POST, sauvegarde le mode de verification via `set_CheckUpdates_config_setting()` et le beat via `set_sugarbeat()`. Compare les versions disponibles via `compareVersions()`.

---

## Dependances cles
| Element | Role |
|---|---|
| `XTemplate` | Moteur de template (format .html) |
| `set_CheckUpdates_config_setting()` | Persistance mode verification |
| `set_sugarbeat()` / `get_sugarbeat()` | Gestion statistiques d'usage |
| `get_CheckUpdates_config_setting()` | Lecture mode actuel |
| `compareVersions()` | Comparaison de versions |
| `$license->settings['license_latest_versions']` | Versions disponibles (serialisees en base64) |

## Symboles principaux
- Aucune classe ni fonction — script procedral

## Interactions
- **Appele par :** `index.php?module=Administration&action=Updater`
- **Template :** `modules/Administration/Updater.html` (XTemplate)

---

## Notes
- Le code de verification immediate (`check_now()`) est commente (lignes 89-93).
- Les versions disponibles sont deserialisees depuis `base64_decode()` avec restriction `['allowed_classes' => false]` (ligne 101) — securite PHP 7.4+.
- `get_sugarbeat()` / `set_sugarbeat()` : INCONNU - fonctions non lues dans ce contexte, probablement dans `include/utils.php`.
