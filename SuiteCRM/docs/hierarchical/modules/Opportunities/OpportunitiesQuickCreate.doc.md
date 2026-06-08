# Fichier : OpportunitiesQuickCreate.php

**Chemin :** `modules/Opportunities/OpportunitiesQuickCreate.php`
**Type :** `PHP`
**Categorie :** view (quick create)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Formulaire de creation rapide d'une opportunite depuis les sous-panneaux ou le tableau de bord.

## Role technique

Classe `OpportunitiesQuickCreate` heritant de `QuickCreate`. Surcharge `process()` pour configurer les callbacks JavaScript AJAX et injecter les listes de valeurs (sales_stage_dom, etc.).

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `QuickCreate` | Classe parente |
| `javascript` | Validation des champs |
| `BeanFactory::newBean('Opportunities')` | Bean pour la validation |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `OpportunitiesQuickCreate` | classe | Vue Quick Create Opportunities |
| `process()` | methode | Surcharge : listes et JS AJAX inline |

## Points d'attention

- Sous-panneau cible AJAX : `subpanel_opportunities` (code en dur).
