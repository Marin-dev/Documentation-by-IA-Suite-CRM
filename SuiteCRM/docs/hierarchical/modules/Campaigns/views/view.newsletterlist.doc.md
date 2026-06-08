# view.newsletterlist.php

**Chemin :** `modules/Campaigns/views/view.newsletterlist.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue liste filtrée affichant uniquement les campagnes de type `NewsLetter`. Surcharge la vue liste standard pour forcer le filtre `campaign_type = 'NewsLetter'` dans la clause WHERE et adapter les libellés.

## Type

`view`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `ViewList` (extend) | Vue liste de base SuiteCRM |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ViewNewsLetterList` | classe | Vue liste filtrée newsletters |

---

## Interactions

- **Appelé par :** `CampaignsController::action_newsletterlist()` (action=newsletterlist)

---

## Points d'attention

- Aucune navigation directe vers cette vue dans le menu (lien commenté dans Menu.php) — accessible uniquement via URL directe ou programmation.
