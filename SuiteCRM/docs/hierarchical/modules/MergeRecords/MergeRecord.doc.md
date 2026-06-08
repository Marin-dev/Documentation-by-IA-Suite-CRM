# MergeRecord.php

**Chemin :** `modules/MergeRecords/MergeRecord.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean SuiteCRM représentant la fusion de deux enregistrements dans un module. Stocke les références aux deux beans à fusionner (`merge_module`, `merge_module2`) et leurs chemins de fichiers. Utilisé dans le processus en plusieurs étapes de fusion de doublons.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)

## Exports / Symboles principaux
- `MergeRecord` (classe) — étend `SugarBean`
  - `$merge_module`, `$merge_bean_class`, `$merge_bean_file_path` — premier bean à fusionner
  - `$merge_module2`, `$merge_bean_class2`, `$merge_bean_file_path2` — second bean
  - `$acl_display_only = true`

## Interactions
- **Appelé par :** `Step1.php`, `Step2.php`, `Step3.php`, `SaveMerge.php`

## Notes
- `acl_display_only = true` : pas d'écriture directe, géré par le flux de fusion.
