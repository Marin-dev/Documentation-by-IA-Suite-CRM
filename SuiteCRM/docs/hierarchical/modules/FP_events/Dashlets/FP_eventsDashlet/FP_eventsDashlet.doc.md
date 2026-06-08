# Fichier : FP_eventsDashlet.php

**Chemin :** `modules/FP_events/Dashlets/FP_eventsDashlet/FP_eventsDashlet.php`
**Type :** PHP — dashlet (DashletGeneric)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Dashlet affichant une liste des evenements (FP_events) sur le tableau de bord SuiteCRM.

## Role technique
Etend `DashletGeneric`. Configuration standard via fichier `.meta.php`. Pas de logique metier additionnelle.

---

## Dependances cles
- `DashletGeneric` (`include/Dashlets/DashletGeneric.php`)
- `FP_events` — module source des donnees

## Exports / Symboles principaux
- `class FP_eventsDashlet extends DashletGeneric`

## Relations cles
- **Appele par :** Framework dashlets SuiteCRM (tableau de bord)

---

## Points d'attention
- Dashlet generique standard.
