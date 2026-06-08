# Fichier : PopupCampaignRoi.php

**Chemin :** `modules/Campaigns/PopupCampaignRoi.php`
**Type :** PHP - Script de vue (popup ROI)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche une popup avec les informations ROI detaillees d'une campagne (couts, revenus, ratio). Complement a la vue detail standard, accessible depuis un lien dans la vue ROI.

## Role technique

Script procedural. Charge le bean Campaign via `BeanFactory`, puis utilise `DetailView` et `campaign_charts` pour generer le contenu de la popup. Requiert `include/DetailView/DetailView.php` et `modules/Campaigns/Charts.php`.

---

## Dependances cles

- `include/DetailView/DetailView.php` — rendu des champs
- `modules/Campaigns/Charts.php` — graphiques ROI
- `BeanFactory::newBean('Campaigns')` — bean campagne

## Exports / Symboles principaux

Aucune classe exportee. Script procedural de rendu HTML.

## Consommateurs identifies

- Lien popup depuis `RoiDetailView.php`

## Relations cles

- **Appelle :** `campaign_charts`, `DetailView`
- **Position dans le flux :** Vue secondaire ROI en popup

---

## Points d'attention

- Concu pour affichage en fenetre popup — peut avoir des styles CSS specifiques differents de la vue principale.
