# MyCasesDashlet.php

**Chemin :** `modules/Cases/Dashlets/MyCasesDashlet/MyCasesDashlet.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Dashlet affichant la liste des cases assignes a l'utilisateur courant sur le tableau de bord SuiteCRM.

## Type
view / dashlet

## Dependances cles
- `include/Dashlets/DashletGeneric.php` — classe parente `DashletGeneric`
- `MyCasesDashlet.data.php` — definition des colonnes et champs de recherche
- `BeanFactory::newBean('Cases')` — bean de reference

## Exports / Symboles principaux
- `class MyCasesDashlet extends DashletGeneric`

## Interactions
- **Appelle :** `BeanFactory::newBean('Cases')`, `translate('LBL_LIST_MY_CASES', 'Cases')`
- **Appele par :** framework Dashlets SuiteCRM

## Notes
- Pas de surcharge de `displayOptions()` contrairement au dashlet Bugs (pas de filtre release).
