# RepairCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/RepairCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commandes Robo de reparation et maintenance de SuiteCRM : synchronisation BDD/vardefs, reconstruction extensions et relations, normalisation encodage des enregistrements.

## Role technique
Quatre commandes independantes. Utilise les outils internes SuiteCRM (`RepairAndClear`, `VardefManager`, `NormalizeRecords`, `NormalizeRecordsSchedulerJob`). La commande `repairNormalizeRecordEncoding` supporte le mode synchrone et le mode scheduler.

---

## Dependances cles
- `Robo\Tasks`
- `DBManagerFactory`, `VardefManager` — acces BDD et vardefs
- `RepairAndClear` — outil de reparation SuiteCRM
- `NormalizeRecords`, `NormalizeRecordsSchedulerJob` — normalisation encodage

## Exports / Symboles principaux
- `RepairCommands` — classe commandes Robo
  - `repairDatabase($opts): void` — sync BDD/vardefs (option `--no-execute`)
  - `repairRebuildExtensions($opts): void` — rebuild des extensions
  - `repairRebuildRelationships($opts): void` — rebuild des relations
  - `repairNormalizeRecordEncoding($opts): void` — normalisation UTF-8 (options `--sync-run`, `--repair-from`, `--keep-tracking`)

## Relations cles
- **Appele par :** CLI Robo (`./vendor/bin/robo repair:*`)
- **Appelle :** `RepairAndClear`, `VardefManager`, `NormalizeRecords`

---

## Points d'attention
- `repairDatabase()` lit `$beanFiles` global — necessite l'initialisation SuiteCRM.
- `repairNormalizeRecordEncoding()` affiche plusieurs prompts de confirmation avant de modifier les donnees.
- En mode asynchrone, necessite que cron soit configure pour executer le job.
