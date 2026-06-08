# CaseEventsHook.php

**Chemin :** `modules/AOP_Case_Events/CaseEventsHook.php`
**Type :** PHP - Hook
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Hook after_save déclenché lors de la sauvegarde d'un cas. Compare l'ancien et le nouveau bean pour détecter les changements sur les champs surveillés (priority, status, assigned_user_id, type) et crée un bean `AOP_Case_Events` pour chaque modification détectée.

## Type
hook

## Dépendances clés
- `BeanFactory` (AOP_Case_Events)

## Exports / Symboles principaux
- `CaseEventsHook` (classe)
  - `$diffFields` (static array) — champs surveillés : priority, status, assigned_user_id, type
  - `compareBeans($old, $new)` — (private) compare et génère les événements

## Interactions
- **Appelé par :** hook after_save du module Cases (déclaré dans `logic_hooks.php`)
- **Appelle :** `BeanFactory::newBean('AOP_Case_Events')`

## Notes
- Crée un enregistrement `AOP_Case_Events` par champ modifié avec description textuelle du changement.
