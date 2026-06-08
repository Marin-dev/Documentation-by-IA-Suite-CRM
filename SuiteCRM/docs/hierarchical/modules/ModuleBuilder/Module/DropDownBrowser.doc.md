# DropDownBrowser.php

**Chemin :** `modules/ModuleBuilder/Module/DropDownBrowser.php`
**Type :** PHP (helper)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Fournit la liste des dropdowns disponibles dans l'éditeur de dropdowns de Studio. Filtre les dropdowns restreints (non éditables par les utilisateurs) et retourne les noeuds de navigation triés alphabétiquement.

## Type
helper

## Dépendances clés
- `$app_list_strings` (global) — source de tous les dropdowns disponibles

## Exports/Symboles principaux
- `DropDownBrowser` — classe
  - `getNodes()` — retourne les noeuds de navigation (un par dropdown accessible)
  - `$restrictedDropdowns` — tableau statique des dropdowns non éditables : `eapm_list`, `eapm_list_documents`, `eapm_list_import`, `extapi_meeting_password`, `Elastic_boost_options`

## Interactions
- **Appelé par :** `DropDownTree`
- **Appelle :** `$app_list_strings` (global)

## Notes
- Seuls les dropdowns dont la valeur est un tableau sont inclus (ligne 65) — les scalaires sont exclus.
- `moduleList` et `moduleListSingular` sont commentés dans `$restrictedDropdowns` — note indique qu'ils pourraient être ajoutés ultérieurement.
