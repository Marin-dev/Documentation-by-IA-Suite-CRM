# Fichier : view.modulelistmenu.php (Campaigns)

**Chemin :** `modules/Campaigns/views/view.modulelistmenu.php`
**Type :** PHP - Vue (menu liste module)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge la vue du menu de liste du module Campaigns pour inclure l'historique des enregistrements recemment consultes (campagnes, listes de prospection, prospects) dans le menu de navigation rapide.

## Role technique

Etend `ViewModulelistmenu`. Override `display()` pour recuperer l'historique recent via `BeanFactory::newBean('Trackers')->get_recently_viewed()` pour les modules Campaigns, ProspectLists et Prospects.

---

## Dependances cles

- `ViewModulelistmenu` — classe parente
- `BeanFactory::newBean('Trackers')` — acces a l'historique de navigation
- `getTrackerSubstring()` — troncature des noms

## Exports / Symboles principaux

- `CampaignsViewModulelistmenu` — classe — menu de navigation du module avec historique

## Consommateurs identifies

- Framework MVC SuiteCRM (barre de navigation du module)

## Relations cles

- **Appelle :** `Trackers->get_recently_viewed()` pour Campaigns, ProspectLists, Prospects

---

## Points d'attention

- L'historique inclut trois modules associes (ProspectLists, Prospects) en plus de Campaigns.
