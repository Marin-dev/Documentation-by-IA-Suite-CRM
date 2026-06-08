# DropDownHelper.php

**Chemin :** `modules/Studio/DropDowns/DropDownHelper.php`
**Type :** PHP - Helper (gestion des dropdowns Studio)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe helper pour la gestion des listes déroulantes (dropdowns) dans le Studio. Scanne tous les modules pour détecter les dropdowns utilisées dans les EditView, et fournit les utilitaires de création/modification de dropdowns.

## Type
helper

## Dépendances clés
- `modules/Administration/Common.php`
- `modules/Administration/QuickRepairAndRebuild.php`
- Répertoire `modules/` — scan dynamique des EditView.php

## Exports / Symboles principaux
- `DropDownHelper` (classe)
  - `$modules` — liste des modules scannés
  - `getDropDownModules()` — scanne tous les modules pour trouver les EditView.php et leurs dropdowns
  - `scanForDropDowns($file, $module)` — analyse un fichier EditView pour identifier les champs dropdown

## Interactions
- **Appelé par :** Studio (interface d'édition des dropdowns)
- **Appelle :** `QuickRepairAndRebuild`, scan du système de fichiers

## Notes
- Scan complet du répertoire `modules/` à chaque appel de `getDropDownModules()` — peut être lent.
