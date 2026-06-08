# TrackDetailView.php

**Chemin :** `modules/Campaigns/TrackDetailView.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue de suivi d'activité d'une campagne. Affiche les statistiques d'envoi et les graphiques de réponse par type d'activité. Utilise `Charts.php` pour la génération des graphiques.

## Type

`view` (affichage classique)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `include/DetailView/DetailView.php` | Vue détail base |
| `modules/Campaigns/Charts.php` | Génération graphiques |
| `BeanFactory::newBean('Campaigns')` | Bean campagne |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Bouton "Track" depuis la vue détail Campaign ou WizardHome
- **Appelle :** `campaign_charts::campaign_response_by_activity_type()`

---

## Points d'attention

- INCONNU : contenu complet du fichier non analysé (lecture partielle).
