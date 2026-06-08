# CalendarSyncJobManager.php

**Chemin :** `include/CalendarSync/application/CalendarSyncJobManager.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service applicatif charge de verifier l'etat actif ou non des jobs de synchronisation calendrier dans la file du scheduler. Permet d'eviter la creation de jobs en double lors d'une synchronisation asynchrone d'un compte ou d'une reunion.

## Role technique

Classe de service sans etat propre, injectee dans `CalendarSyncOrchestrator`. Utilise `JobStatusHelper` pour construire les noms et conditions SQL de recherche. Interroge le bean `SchedulersJobs` via `BeanFactory` et `get_list()` pour detecter les jobs actifs.

---

## Dependances cles

- **Imports principaux :**
  - `JobStatusHelper` (`include/CalendarSync/infrastructure/jobs/JobStatusHelper.php`) — generation des noms de jobs et conditions SQL de statut

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncJobManager` | classe | Gestionnaire de statut des jobs |
| `accountJobIsActive(string): bool` | methode | Verifie si un job de compte est actif |
| `getActiveMeetingJobCount(CalendarSyncOperation): int` | methode | Compte les jobs de reunion actifs |
| `meetingJobIsActive(CalendarSyncOperation): bool` | methode | Raccourci bool sur le compte |

- **Consommateurs identifies :** `CalendarSyncOrchestrator` (injection dans le constructeur)

## Relations cles

- **Appele par :** `CalendarSyncOrchestrator` (avant creation de job async)
- **Appelle :** `JobStatusHelper`, `BeanFactory::newBean('SchedulersJobs')`
- **Position dans le flux global :** garde-fou anti-doublon avant soumission d'un job au scheduler

---

## Points d'attention

- En cas d'exception lors de la requete BDD, retourne `false` / `0` (failsafe : autorise la creation de job plutot que de bloquer). Surveiller les erreurs BDD en production.
- `get_list()` avec `LIMIT 1` pour les jobs de compte : efficace. Pas de limite pour les jobs de reunion, peut etre couteux si la file est longue.
