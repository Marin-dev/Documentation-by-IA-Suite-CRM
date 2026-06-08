# Fichier : RoiDetailView.php

**Chemin :** `modules/Campaigns/RoiDetailView.php`
**Type :** PHP - Script de vue (detail ROI)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la vue detaillee du retour sur investissement (ROI) d'une campagne. Presente les indicateurs financiers (budget, couts reels, revenus attendus/reels), les statistiques d'envoi et les graphiques de performance.

## Role technique

Script procedural. Charge le bean Campaign, utilise `DetailView` pour le rendu des champs et `campaign_charts` pour les graphiques. Requiert `include/DetailView/DetailView.php` et `modules/Campaigns/Charts.php`.

---

## Dependances cles

- `include/DetailView/DetailView.php` — rendu des champs du bean
- `modules/Campaigns/Charts.php` — graphiques ROI (`campaign_charts`)
- `BeanFactory::newBean('Campaigns')` — bean campagne

## Exports / Symboles principaux

Aucune classe exportee. Script procedural de rendu HTML.

## Consommateurs identifies

- Action `RoiDetailView` du module Campaigns
- Lien "Voir le ROI" dans la vue detail de la campagne

## Relations cles

- **Appelle :** `campaign_charts`, `DetailView`
- **Position dans le flux :** Vue analytique apres execution de la campagne

---

## Points d'attention

- Les graphiques dependant de `campaign_charts` (Charts.php) — voir ce fichier pour les details de generation.
