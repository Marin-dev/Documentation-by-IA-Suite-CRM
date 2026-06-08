# Fichier : SurveysDashlet.php

**Chemin :** `modules/Surveys/Dashlets/SurveysDashlet/SurveysDashlet.php`
**Type :** PHP — dashlet (DashletGeneric)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Dashlet affichant une liste des sondages (Surveys) sur le tableau de bord SuiteCRM.

## Role technique
Etend `DashletGeneric`. Importe `modules/Surveys/Surveys.php`. Configuration via `.meta.php`. La logique d'affichage est standard DashletGeneric.

---

## Dependances cles
- `DashletGeneric` (`include/Dashlets/DashletGeneric.php`)
- `Surveys` (`modules/Surveys/Surveys.php`)

## Exports / Symboles principaux
- `class SurveysDashlet extends DashletGeneric`

## Relations cles
- **Appele par :** Framework dashlets SuiteCRM (tableau de bord)

---

## Points d'attention
- Dashlet generique standard.
