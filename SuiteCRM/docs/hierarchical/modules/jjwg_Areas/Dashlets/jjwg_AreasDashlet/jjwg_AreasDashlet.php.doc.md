# jjwg_AreasDashlet.php

**Chemin :** `modules/jjwg_Areas/Dashlets/jjwg_AreasDashlet/jjwg_AreasDashlet.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Dashlet (widget tableau de bord) du module jjwg_Areas. Affiche une liste configurable des zones geographiques sur la page d'accueil de SuiteCRM.

**Type :** helper (dashlet)

---

## Dependances cles
- `include/Dashlets/DashletGeneric.php` — classe parente
- `modules/jjwg_Areas/jjwg_Areas.php` — bean
- `modules/jjwg_Areas/metadata/dashletviewdefs.php` — colonnes et champs de recherche
- `BeanFactory::newBean('jjwg_Areas')` — creation du seed bean

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `jjwg_AreasDashlet` | Classe | Dashlet generique pour jjwg_Areas |
| `__construct($id, $def)` | Methode | Initialise les colonnes, champs de recherche et le seed bean |

---

## Interactions
- **Herite de :** `DashletGeneric`
- **Utilise :** `dashletviewdefs.php` pour la configuration des colonnes
- **Appele par :** framework Dashlet de SuiteCRM via `$dashletMeta` (jjwg_AreasDashlet.meta.php)

---

## Notes
- Pas de logique metier specifique : toute la logique d'affichage est dans `DashletGeneric`.
