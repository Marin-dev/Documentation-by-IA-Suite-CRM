# RoiDetailView.php

**Chemin :** `modules/Campaigns/RoiDetailView.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue de suivi du retour sur investissement (ROI) d'une campagne. Affiche les données financières (budget, coûts, revenus attendus vs réels) et le graphique ROI via `Charts.php`.

## Type

`view` (affichage classique)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `include/DetailView/DetailView.php` | Vue détail base |
| `modules/Campaigns/Charts.php` | Graphique ROI |
| `BeanFactory::newBean('Campaigns')` | Bean campagne |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Bouton "ROI" depuis WizardHome
- **Appelle :** `campaign_charts::campaign_response_roi()`

---

## Points d'attention

- INCONNU : contenu complet non analysé (lecture partielle).
