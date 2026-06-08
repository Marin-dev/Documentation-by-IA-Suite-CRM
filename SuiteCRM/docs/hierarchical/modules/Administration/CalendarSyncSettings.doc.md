# CalendarSyncSettings.php

**Chemin :** `modules/Administration/CalendarSyncSettings.php`
**Type :** PHP (view / page parametres)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page d'administration de la synchronisation des calendriers. Permet de configurer les options de synchronisation (resolution des conflits, planificateur) et de declencher manuellement une synchronisation de tous les comptes calendrier.

## Role technique
Script procedral. Gere deux actions POST : `manual_trigger` (appelle `CalendarSync::syncAllCalendarAccounts(true)`) et `save` (appelle `CalendarSync::saveConfig($_POST)`). Construit les options de resolution de conflits a partir des valeurs de l'enum `ConflictResolutionCase`. Affiche les dates de derniere execution (planifiee et manuelle) converties au fuseau horaire utilisateur via `$timedate`.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/CalendarSync/CalendarSync.php` | Service de synchronisation calendrier (singleton) |
| `Sugar_Smarty` | Template |
| `$timedate` (global) | Conversion dates en TZ utilisateur |
| `CalendarSync::getScheduler()` | Lecture du planificateur associe |
| `CalendarSync::getConflictResolutionCases()` | Enum des cas de conflit |

## Symboles principaux
- Aucune classe ni fonction — script procedral de vue

## Interactions
- **Appele par :** `index.php?module=Administration&action=CalendarSyncSettings`
- **Appelle :** `CalendarSync::getInstance()`, `syncAllCalendarAccounts()`, `saveConfig()`
- **Template :** `modules/Administration/templates/CalendarSyncSettings.tpl`

---

## Notes
- Acces restreint : `is_admin($current_user)`.
- Fichier recent (copyright 2025) — fonctionnalite ajoutee par SalesAgility.
- `$scheduler?->status === 'Active'` : utilise l'operateur nullsafe de PHP 8.
- `last_manual_run_time` est stocke dans la config de CalendarSync, pas dans le scheduler.
