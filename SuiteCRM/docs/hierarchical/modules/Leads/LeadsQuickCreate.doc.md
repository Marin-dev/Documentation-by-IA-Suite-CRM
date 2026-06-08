# Fichier : LeadsQuickCreate.php

**Chemin :** `modules/Leads/LeadsQuickCreate.php`
**Type :** `PHP`
**Categorie :** view (quick create)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Formulaire de creation rapide d'un lead depuis les sous-panneaux ou le tableau de bord. Ajoute les options de salutation, statut et source du lead en plus du formulaire standard.

## Role technique

Classe `LeadsQuickCreate` heritant de `QuickCreate`. Surcharge `process()` pour assigner les listes de choix (`salutation_dom`, `lead_status_dom`, `lead_source_dom`) et configurer les callbacks JavaScript AJAX inline. Nom de formulaire : `leadsQuickCreate`.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `QuickCreate` | Classe parente |
| `javascript` | Validation des champs |
| `BeanFactory::newBean('Leads')` | Bean pour la validation |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadsQuickCreate` | classe | Vue Quick Create pour le module Leads |
| `process()` | methode | Surcharge : configure listes et JS AJAX inline |

## Points d'attention

- Similaire a `AccountsQuickCreate` avec en plus les listes de choix specifiques aux leads.
- Le sous-panneau cible en mode AJAX est `subpanel_leads` (code en dur).
