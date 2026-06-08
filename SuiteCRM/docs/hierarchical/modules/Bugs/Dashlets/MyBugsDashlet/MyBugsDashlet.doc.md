# MyBugsDashlet.php

**Chemin :** `modules/Bugs/Dashlets/MyBugsDashlet/MyBugsDashlet.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Dashlet affichant la liste des bugs assignes a l'utilisateur courant sur le tableau de bord SuiteCRM. Permet le filtrage par statut, priorite, type, release.

## Type
view / dashlet

## Dependances cles
- `include/Dashlets/DashletGeneric.php` — classe parente `DashletGeneric`
- `MyBugsDashlet.data.php` — definition des colonnes et champs de recherche
- `BeanFactory::newBean('Bugs')` — bean de reference
- `BeanFactory::newBean('Releases')` — pour les dropdowns de release

## Exports / Symboles principaux
- `class MyBugsDashlet extends DashletGeneric`
- Methode `displayOptions()` — surcharge pour injecter les selects de release (found/fixed)

## Interactions
- **Appelle :** `BeanFactory::newBean('Releases')`, `get_select_options_with_id()`, `$this->processDisplayOptions()`
- **Appele par :** framework Dashlets SuiteCRM lors du rendu du tableau de bord

## Notes
- Filtre par defaut : statuts `Assigned`, `New`, `Pending` (defini dans data.php).
- Les releases sont chargees dynamiquement (statut Active uniquement).
