# Fichier : Charts.php

**Chemin :** `modules/Campaigns/Charts.php`
**Type :** PHP - Helper (generation de graphiques)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la classe `campaign_charts` chargee de generer les graphiques de suivi de campagne (taux de ciblage, clics, leads, ROI) affiches dans les vues detail et ROI des campagnes.

## Role technique

Depend de `include/SugarCharts/SugarChartFactory.php`. Genere des graphiques en barres verticales accumulees pour visualiser les statistiques de campagne. Les donnees sont passees en parametres depuis les vues appelantes.

---

## Dependances cles

- `include/SugarCharts/SugarChartFactory.php` — fabrique de graphiques SugarCRM

## Exports / Symboles principaux

- `campaign_charts` — classe — generateur de graphiques de campagne
  - Methodes de generation de graphiques (details des signatures INCONNUS sans lecture complete)

## Consommateurs identifies

- `modules/Campaigns/RoiDetailView.php` (require_once)
- `modules/Campaigns/TrackDetailView.php` (require_once)
- `modules/Campaigns/PopupCampaignRoi.php` (require_once)

## Relations cles

- **Appelle :** `SugarChartFactory`
- **Appele par :** vues detail ROI et tracking

---

## Points d'attention

- La classe est orientee affichage uniquement, pas de persistance en base.
