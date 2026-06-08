# SaveMerge.php

**Chemin :** `modules/MergeRecords/SaveMerge.php`
**Type :** PHP - Script d'action (sauvegarde de la fusion)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Exécute la fusion finale de deux enregistrements. Vérifie les droits ACL et que le module supporte la fusion (`duplicate_merge`), puis fusionne les enregistrements sélectionnés.

## Type
helper

## Dépendances clés
- `BeanFactory::newBean('MergeRecords')`
- `$_REQUEST['record']`, `$_REQUEST['merge_module']`, `$_REQUEST['merged_ids']`
- `$dictionary[$focus->merge_bean->object_name]['duplicate_merge']` — vérification de permission

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** action SaveMerge du module MergeRecords (Step3 du wizard)
- **Appelle :** `MergeRecord::load_merge_bean()`, `SugarBean::ACLAccess('edit')`

## Notes
- Double vérification de sécurité : `duplicate_merge` dans dictionary + `ACLAccess('edit')`.
- `sugar_die()` si accès refusé.
