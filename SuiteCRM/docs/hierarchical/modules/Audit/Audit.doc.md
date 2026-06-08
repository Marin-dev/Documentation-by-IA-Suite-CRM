# Audit.php

**Chemin :** `modules/Audit/Audit.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant les enregistrements d'audit dans SuiteCRM. Stocke les modifications apportées aux champs audités des beans (qui a changé quoi et quand). S'appuie sur `field_assoc.php` pour la correspondance des champs.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)
- `modules/Audit/field_assoc.php` — association des champs auditables

## Exports / Symboles principaux
- `Audit` (classe) — étend `SugarBean`
  - `$module_dir = "Audit"`, `$object_name = "Audit"`
  - `$additional_column_fields` — champs supplémentaires POST

## Interactions
- **Appelé par :** framework SugarBean (after_save hook automatique pour modules auditables)
- **Appelle :** `field_assoc.php`
