# Schedule.php

**Chemin :** `modules/Campaigns/Schedule.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue de sélection et de planification des envois de messages marketing pour une campagne. Affiche la liste des EmailMarketing disponibles avec cases à cocher. Supporte deux modes : planification réelle (send) et test (envoi immédiat sur liste test).

## Type

`view` (affichage classique)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('Campaigns')` | Bean campagne |
| `BeanFactory::newBean('EmailMarketing')` | Liste des messages marketing |
| `ListView` | Affichage liste multi-sélection |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** `TrackDetailView.php`, bouton "Planifier" dans le wizard
- **Appelle :** `QueueCampaign.php` via soumission formulaire

---

## Points d'attention

- En mode test, filtre les EmailMarketing liés aux listes de type `test` — requête SQL complexe avec jointures (lignes 149-160).
- Si la campagne est `Inactive`, affiche un message d'alerte au lieu du formulaire.
