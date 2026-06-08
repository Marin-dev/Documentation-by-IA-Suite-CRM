# Fichier : FP_Event_LocationsDashlet.php

**Chemin :** `modules/FP_Event_Locations/Dashlets/FP_Event_LocationsDashlet/FP_Event_LocationsDashlet.php`
**Type :** PHP — dashlet (DashletGeneric)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Dashlet affichant une liste des lieux d'evenements (FP_Event_Locations) sur le tableau de bord SuiteCRM.

## Role technique
Etend `DashletGeneric`. Configuration standard via fichier `.meta.php`. Pas de logique metier additionnelle identifiee (fichier presque vide apres la licence).

---

## Dependances cles
- `DashletGeneric` (`include/Dashlets/DashletGeneric.php`)
- `FP_Event_Locations` — module source des donnees

## Exports / Symboles principaux
- `class FP_Event_LocationsDashlet extends DashletGeneric`

## Relations cles
- **Appele par :** Framework dashlets SuiteCRM (tableau de bord)
- **Configuration :** `FP_Event_LocationsDashlet.meta.php`

---

## Points d'attention
- Dashlet generique standard — comportement entierement configure par le fichier meta.
