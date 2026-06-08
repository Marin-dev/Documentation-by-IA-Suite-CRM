# repairSelectModule.php

**Chemin :** `modules/Administration/repairSelectModule.php`
**Type :** PHP (view)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Affiche le formulaire de selection des operations Quick Repair & Rebuild (QRR). Permet de choisir les actions de nettoyage/reconstruction a executer et le module cible (ou tous les modules).

## Role technique
Script procedral. Trie `$beanList`, cree les listes de valeurs pour le dropdown de modules (avec "Tous les modules" en tete) et les cases a cocher des actions disponibles. Affiche via template `QuickRepairAndRebuild.tpl`.

---

## Actions disponibles (checkboxes)
`clearTpls`, `clearJsFiles`, `clearVardefs`, `clearJsLangFiles`, `clearDashlets`, `clearSugarFeedCache`, `clearThemeCache`, `rebuildAuditTables`, `rebuildExtensions`, `clearLangFiles`, `clearSearchCache`, `clearPDFFontCache`

Note : `repairDatabase` est commente.

## Interactions
- **Inclus/appele par :** Action `QuickRepairAndRebuild` de l'administration (INCONNU - chemin exact)
- **Template :** `modules/Administration/templates/QuickRepairAndRebuild.tpl`
- **Execution via :** `QuickRepairAndRebuild.php` (classe RepairAndClear)
