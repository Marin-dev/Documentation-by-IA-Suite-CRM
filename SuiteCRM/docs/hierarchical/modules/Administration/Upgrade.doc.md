# Upgrade.php

**Chemin :** `modules/Administration/Upgrade.php`
**Type :** PHP (view / page)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page "Upgrade" de l'administration. Affiche les liens vers les outils de mise a jour, reparation et maintenance avances (RebuildFulltextIndices, RebuildSchedulers, RebuildRelationship, etc.).

## Role technique
Script procedral avec HTML inline. Affiche conditionnellement certains liens selon les capacites BDD (`supports('fulltext')`) et OS (IIS vs Apache).

---

## Interactions
- **Appele par :** `index.php?module=Administration&action=Upgrade`
- **Lie vers :** `RebuildFulltextIndices`, `RebuildSchedulers`, `RebuildRelationship`, `RepairSeedUsers`, `UpgradeAccess`, `UpgradeIISAccess`, etc.
