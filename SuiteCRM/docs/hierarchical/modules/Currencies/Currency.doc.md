# Currency.php

**Chemin :** `modules/Currencies/Currency.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean central pour la gestion des devises dans SuiteCRM. Encapsule les conversions monétaires et le formatage. Utilisé massivement par les modules financiers (Opportunities, Quotes, Invoices, etc.) pour les calculs multi-devises.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)

## Exports / Symboles principaux
- `Currency` (classe) — étend `SugarBean`
  - Champs : symbol, conversion_rate, name, iso4217 (INCONNU — lecture partielle)
  - Méthodes de conversion et formatage (INCONNU)

## Interactions
- **Appelé par :** `PipelineBySalesStageDashlet`, `CampaignROIChartDashlet`, et tout module financier

## Notes
- L'ID `-99` correspond à la devise par défaut du système.
