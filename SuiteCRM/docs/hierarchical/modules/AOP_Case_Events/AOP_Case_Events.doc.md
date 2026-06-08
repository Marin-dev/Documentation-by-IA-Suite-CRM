# AOP_Case_Events.php

**Chemin :** `modules/AOP_Case_Events/AOP_Case_Events.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant un événement de cas (ticket support) dans le module AOP (Advanced OpenCases Portal). Enregistre automatiquement les changements de statut, priorité, utilisateur assigné et type d'un cas. Non importable, sécurité par ligne désactivée.

## Type
model

## Dépendances clés
- `basic` (classe parente SugarCRM)

## Exports / Symboles principaux
- `AOP_Case_Events` (classe) — étend `basic`
  - Table : `aop_case_events`
  - Champs : `$id`, `$name`, `$description`, `$case_id`, `$date_entered`, `$created_by`, etc.

## Interactions
- **Appelé par :** `CaseEventsHook` (after_save du module Cases)
- **Appelle :** logique `basic`
