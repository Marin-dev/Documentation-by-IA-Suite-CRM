# Fichier vardefs.php — AOR_Fields

**Chemin :** `modules/AOR_Fields/vardefs.php`
**Type :** PHP — configuration
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Définit le schéma de la table `aor_fields` : champs (field, display, label, field_function, sort_by, format, group_by, group_order, group_display, link, total, module_path, aor_report_id).

## Type
config

## Notes
FK one-to-many avec AOR_Reports. Utilisé par `AOR_Report::build_report_query_select()` et `getReportFields()`.
