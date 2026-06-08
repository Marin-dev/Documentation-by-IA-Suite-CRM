# Alert.php

**Chemin :** `modules/Alerts/Alert.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une alerte/notification dans SuiteCRM. Stocke les alertes utilisateur affichées dans l'interface (table `alerts`). Non importable. La sécurité par ligne est désactivée.

## Type
model

## Dépendances clés
- `Basic` (classe parente SugarCRM)

## Exports / Symboles principaux
- `Alert` (classe) — étend `Basic`
  - Table : `alerts`
  - Champs : `$id`, `$name`, `$description`, `$date_entered`, `$created_by`, etc.
  - `$disable_row_level_security = true`
  - `$importable = false`

## Interactions
- **Appelé par :** vues Alerts, contrôleur Alerts
- **Appelle :** logique `Basic` / `SugarBean`
