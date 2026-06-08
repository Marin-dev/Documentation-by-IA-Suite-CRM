# Fichier : Reschedule.php

**Chemin :** `install/suite_install/Reschedule.php`
**Type :** installer (configuration module Calls Reschedule)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure le module de replanification d'appels (Calls_Reschedule) en enregistrant le hook de comptage lors du traitement d'un enregistrement d'appel.

## Role technique
Fonction `install_reschedule()` qui enregistre un hook `process_record` sur le module Calls avec order 1.

---

## Dependances cles
- **Imports principaux :**
  - `ModuleInstall/ModuleInstaller.php`

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_reschedule()` | Enregistre le hook de comptage des replanifications |

**Hook configure :**
- Module : `Calls`, hook : `process_record`, order 1
- Fichier : `modules/Calls_Reschedule/reschedule_count.php`
- Classe : `reschedule_count`, Fonction : `count`

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 46)
- **Appelle :**
  - `check_logic_hook_file()`
  - `modules/Calls_Reschedule/reschedule_count.php`

---

## Notes
- Ce hook compte le nombre de fois qu'un appel a ete replanifie, utilisé pour les rapports.
