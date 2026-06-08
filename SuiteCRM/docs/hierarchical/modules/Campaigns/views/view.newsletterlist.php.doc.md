# Fichier : view.newsletterlist.php (Campaigns)

**Chemin :** `modules/Campaigns/views/view.newsletterlist.php`
**Type :** PHP - Vue (liste newsletters)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la vue liste filtree sur les campagnes de type `NewsLetter` uniquement. Surcharge la vue liste standard pour presenter uniquement les newsletters, avec les colonnes et actions adaptees.

## Role technique

Etend `ViewList`. Applique un filtre sur `campaign_type = 'NewsLetter'` dans la requete de liste. L'action `newsletterlist` est routee vers cette vue par `CampaignsController::action_newsletterlist()`.

---

## Dependances cles

- `ViewList` — classe parente

## Exports / Symboles principaux

- `ViewNewsLetterList` — classe — vue liste newsletters

## Consommateurs identifies

- `CampaignsController::action_newsletterlist()` — route vers cette vue
- Accessible via `index.php?module=Campaigns&action=newsletterlist`

## Relations cles

- **Filtre sur :** `campaigns.campaign_type = 'NewsLetter'`
- **Position dans le flux :** Vue liste specialisee pour les newsletters

---

## Points d'attention

- Vue distincte de la liste generale — les campagnes de type Email n'apparaissent pas ici.
