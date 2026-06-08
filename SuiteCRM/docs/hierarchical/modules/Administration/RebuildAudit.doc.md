# RebuildAudit.php

**Chemin :** `modules/Administration/RebuildAudit.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Recree les tables d'audit manquantes pour tous les beans qui ont l'audit active. Script de reparation leger appele depuis le panneau Quick Repair.

## Role technique
Itere sur `$beanFiles` via `include/modules.php`, instancie chaque bean, verifie `is_AuditEnabled()`, et appelle `create_audit_table()` si la table `{module}_audit` n'existe pas. Affiche l'avancement.

---

## Interactions
- **Inclus par :** Probablement appele depuis `QuickRepairAndRebuild::rebuildAuditTables()` (via include direct)
- **Appelle :** `SugarBean::is_AuditEnabled()`, `SugarBean::create_audit_table()`, `DBManager::tableExists()`
