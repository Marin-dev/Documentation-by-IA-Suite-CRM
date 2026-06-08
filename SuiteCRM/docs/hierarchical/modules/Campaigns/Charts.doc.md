# Charts.php

**Chemin :** `modules/Campaigns/Charts.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Génère les graphiques de suivi et de ROI d'une campagne. Produit deux types de graphiques : activité par type de réponse (graphique barres groupées horizontal) et retour sur investissement (revenus vs coûts vs budget).

## Type

`helper` (classe utilitaire)

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `include/SugarCharts/SugarChartFactory.php` | Fabrique de graphiques |
| `SugarChartFactory::getInstance()` | Crée l'instance de graphique |
| `BeanFactory::newBean('Campaigns')` | Récupère les données de la campagne |
| `BeanFactory::newBean('Currencies')` | Symbole monétaire |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `campaign_charts` | classe | Contient les méthodes de génération de graphiques |
| `campaign_response_by_activity_type()` | méthode | Graphique barres groupées : activités (link, removed, targeted…) par type de cible |
| `campaign_response_roi()` | méthode | Graphique barres : revenus réels vs investissement vs budget vs revenus attendus |
| `campaign_response_roi_data()` | méthode | Variante données seules pour ROI (même logique, refactoring partiel) |

---

## Interactions

- **Appelé par :** `TrackDetailView.php`, `RoiDetailView.php`, `TopCampaignsDashlet.php`
- **Appelle :** Tables `campaign_log`, `opportunities`, `campaigns` (SQL direct)
- **Position dans le flux global :** Visualisation des résultats d'une campagne

---

## Points d'attention

- `campaign_response_roi_data()` est un quasi-copier-coller de `campaign_response_roi()` avec un TODO de refactoring mentionné en commentaire (ligne 372).
- Les graphiques sont mis en cache sous forme de fichiers XML — invalidés par le flag `$refresh`.
- Le calcul ROI ne prend en compte que les opportunités `Closed Won` liées à la campagne.
