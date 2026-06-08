# view.detail.php

**Chemin :** `modules/Campaigns/views/view.detail.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue détail personnalisée du module Campaigns. Surcharge la vue détail standard pour : filtrer les sous-panneaux affichés (uniquement prospectlists, emailmarketing, tracked_urls, history), gérer le bouton "Set Target", et afficher la devise de la campagne.

## Type

`view`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `ViewDetail` (extend) | Vue détail de base SuiteCRM |
| `modules/Campaigns/utils.php` | `track_campaign_prospects()` (mode set_target) |
| `include/SubPanel/SubPanelTiles.php` | Gestion des sous-panneaux filtrés |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `CampaignsViewDetail` | classe | Vue détail custom du module Campaigns |

---

## Interactions

- **Appelé par :** Framework MVC SuiteCRM (action=DetailView)
- **Appelle :** `track_campaign_prospects()`, `SubPanelTiles`

---

## Points d'attention

- Les sous-panneaux sont filtrés manuellement (lignes 128-148) — seuls prospectlists, emailmarketing, tracked_urls et history sont affichés.
- Le sous-panneau emailmarketing est masqué pour les campagnes non-Email/Newsletter.
- Le mode `set_target` dans la requête déclenche la regénération des logs ciblés.
