# Fichier vardefs.php — AOR_Scheduled_Reports

**Chemin :** `modules/AOR_Scheduled_Reports/vardefs.php`
**Type :** PHP — configuration
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Définit le schéma de la table `aor_scheduled_reports` : champs (schedule, email_recipients, status, last_run, aor_report_id).

## Type
config

## Notes
Lié à AOR_Reports via `aor_scheduled_reports_aor_reports` (many-to-one côté scheduled). Template VardefManager `basic`, `assignable`.
