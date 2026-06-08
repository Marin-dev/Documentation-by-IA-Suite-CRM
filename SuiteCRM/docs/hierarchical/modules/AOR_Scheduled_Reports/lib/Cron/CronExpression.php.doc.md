# Fichier CronExpression.php

**Chemin :** `modules/AOR_Scheduled_Reports/lib/Cron/CronExpression.php`
**Type :** PHP — bibliothèque tierce
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Bibliothèque d'analyse et de calcul des expressions cron. Utilisée par `AOR_Scheduled_Reports::shouldRun()` pour déterminer la prochaine exécution d'un rapport planifié à partir d'une expression cron (ex: `0 8 * * 1`).

## Type
autre (bibliothèque tierce — Cron\CronExpression)

## Exports / Symboles principaux
| Symbole | Rôle |
|---|---|
| `Cron\CronExpression` | Classe principale : `factory()`, `isDue()`, `getNextRunDate()` |

## Notes
Bibliothèque tierce dans le namespace `Cron`. Ne pas modifier. Utilisée exclusivement par `AOR_Scheduled_Reports`.
