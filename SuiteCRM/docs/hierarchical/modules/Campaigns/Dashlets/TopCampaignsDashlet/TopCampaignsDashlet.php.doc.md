# Fichier : TopCampaignsDashlet.php

**Chemin :** `modules/Campaigns/Dashlets/TopCampaignsDashlet/TopCampaignsDashlet.php`
**Type :** PHP - Composant Dashlet (tableau de bord)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Dashlet affichant les meilleures campagnes en cours sur la page d'accueil SuiteCRM. Presente un classement des campagnes selon leur performance (impressions, clics, leads generes).

## Role technique

Etend `include/Dashlets/Dashlet.php`. Stocke la liste des campagnes dans `$top_campaigns`. Implemente le constructeur et les methodes de rendu standard des Dashlets.

---

## Dependances cles

- `include/Dashlets/Dashlet.php` — classe parente
- `BeanFactory` ou requetes SQL — chargement des campagnes

## Exports / Symboles principaux

- `TopCampaignsDashlet` — classe — dashlet des meilleures campagnes
  - `__construct($id, $def)` — initialisation (l.59)
  - Methodes de rendu Dashlet (INCONNU sans lecture complete)

## Consommateurs identifies

- Framework Dashlet SuiteCRM (page d'accueil / Home)
- Metadata dans `TopCampaignsDashlet.meta.php`

## Relations cles

- **Position dans le flux :** Widget analytique sur la page d'accueil

---

## Points d'attention

- Dependant des donnees `campaign_log` pour calculer les performances — performances a surveiller si beaucoup de logs.
