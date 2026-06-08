# Development.php

**Chemin :** `modules/Administration/Development.php`
**Type :** PHP (view / page)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page "Migration des champs" dans l'administration. Affiche les liens vers les outils d'import et d'export de la structure des champs personnalises (`ImportCustomFieldStructure` et `ExportCustomFieldStructure`).

## Role technique
Script procedral minimal avec HTML inline. Affiche deux liens avec icones via `SugarThemeRegistry`.

---

## Interactions
- **Appele par :** `index.php?module=Administration&action=Development`
- **Lie vers :** `ImportCustomFieldStructure`, `ExportCustomFieldStructure`
