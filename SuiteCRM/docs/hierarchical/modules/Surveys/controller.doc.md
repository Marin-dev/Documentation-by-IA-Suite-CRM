# Fichier : controller.php

**Chemin :** `modules/Surveys/controller.php`
**Type :** PHP — controller (SugarController)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Controller du module Surveys. Gere l'action specifique "Reports" qui affiche les rapports de resultats de sondages.

## Role technique
Etend `SugarController`. Une seule action surchargee : `action_Reports()` qui redirige vers la vue 'Reports'. Toutes les autres actions utilisent le comportement par defaut de SugarController.

---

## Dependances cles
- `SugarController` — classe parente

## Exports / Symboles principaux
- `class SurveysController extends SugarController`
- `action_Reports()` — route vers la vue Reports

## Relations cles
- **Appele par :** framework MVC SugarCRM (action Reports du module Surveys)
- **Appelle :** `modules/Surveys/views/view.reports.php`

---

## Points d'attention
- Controller minimaliste — une seule action custom.
