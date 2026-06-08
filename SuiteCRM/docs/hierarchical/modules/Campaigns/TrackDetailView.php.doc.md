# Fichier : TrackDetailView.php

**Chemin :** `modules/Campaigns/TrackDetailView.php`
**Type :** PHP - Script de vue (suivi campagne)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la vue de suivi d'une campagne : statistiques de clics, ouvertures, leads generes, desinscriptions. Presente les graphiques de performance du tracking.

## Role technique

Script procedural. Charge le bean Campaign, utilise `DetailView` pour le rendu des champs et `campaign_charts` pour les graphiques de tracking. Requiert `include/DetailView/DetailView.php` et `modules/Campaigns/Charts.php`.

---

## Dependances cles

- `include/DetailView/DetailView.php` — rendu des champs
- `modules/Campaigns/Charts.php` — graphiques de tracking (`campaign_charts`)
- `BeanFactory::newBean('Campaigns')` — bean campagne

## Exports / Symboles principaux

Aucune classe exportee. Script procedural de rendu HTML.

## Consommateurs identifies

- Action `TrackDetailView` depuis la liste des campagnes (icone de tracking)

## Relations cles

- **Appelle :** `campaign_charts`, `DetailView`
- **Position dans le flux :** Vue analytique de suivi temps-reel de la campagne

---

## Points d'attention

- Analogique a `RoiDetailView.php` mais focuse sur les statistiques de tracking (clics/ouvertures) plutot que sur le ROI financier.
