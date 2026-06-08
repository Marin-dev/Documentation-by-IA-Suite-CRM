# CasesQuickCreate.php

**Chemin :** `modules/Cases/CasesQuickCreate.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Gere le formulaire de creation rapide (Quick Create) d'un cas client depuis un sous-panneau ou une popup. Permet de creer un case sans naviguer vers la vue d'edition complete.

## Type
controller / helper vue

## Dependances cles
- `include/EditView/QuickCreate.php` — classe parente `QuickCreate`
- `BeanFactory::newBean('Cases')` — instanciation du bean pour la validation JS
- `javascript` (classe SuiteCRM) — generation des scripts de validation
- `$app_list_strings` — listes de valeurs (case_priority_dom, case_status_dom)
- `getJSONobj()` — encodage JSON de la configuration popup

## Exports / Symboles principaux
- `class CasesQuickCreate extends QuickCreate`
- Methode `process()` — prepare les options de formulaire, scripts JS et donnees popup compte

## Interactions
- **Appelle :** `parent::process()`, `BeanFactory::newBean('Cases')`, `get_select_options_with_id()`, `getJSONobj()`, `javascript->setFormName/setSugarBean/addAllFields/getScript`
- **Appele par :** framework SuiteCRM lors du rendu d'un sous-panneau Cases avec action QuickCreate

## Notes
- Form name fixe : `casesQuickCreate`. Sous-panneau cible : `subpanel_cases`.
- Inclut une configuration popup de selection de compte (`account_id`, `account_name`).
