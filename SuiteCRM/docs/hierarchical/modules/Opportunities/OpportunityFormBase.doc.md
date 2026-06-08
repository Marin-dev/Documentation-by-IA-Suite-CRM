# Fichier : OpportunityFormBase.php

**Chemin :** `modules/Opportunities/OpportunityFormBase.php`
**Type :** `PHP`
**Categorie :** helper / form handler
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe de base gerant la logique des formulaires d'opportunite : detection de doublons par nom, rendu HTML, sauvegarde et redirection. Equivalent de `AccountFormBase` pour les opportunites.

## Role technique

Classe standalone `OpportunityFormBase`. La detection de doublons utilise une recherche LIKE sur le nom avec `getLikeForEachWord()` en plus d'un match exact. Contient les methodes `handleSave`, `checkForDuplicates`, `buildTableForm`, `getForm`, `getFormBody`.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `BeanFactory::newBean('Opportunities')` | Bean Opportunity |
| `ACLController` | Verification des droits |
| `javascript` | Validation JS |
| `include/formbase.php` | Utilitaires formulaire |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `OpportunityFormBase` | classe | Gestionnaire formulaire Opportunity |
| `checkForDuplicates($prefix)` | methode | Recherche doublons par nom (LIKE + decomposition par mots) |
| `handleSave($prefix, $redirect, $useRequired)` | methode | Orchestre la sauvegarde |
| `buildTableForm($rows)` | methode | HTML tableau de selection de doublons |
| `getForm($prefix, $mod, $form)` | methode | Formulaire compact |
| `getFormBody($prefix, $mod, $formname)` | methode | Corps du formulaire |

**Consommateurs identifies dans le repo :**

- `modules/Opportunities/Save.php`

## Points d'attention

- La recherche de doublons utilise `getLikeForEachWord()` : decompose le nom en mots pour une recherche plus large.
- La requete de doublon porte sur `name`, `sales_stage`, `amount` et `date_closed`.
