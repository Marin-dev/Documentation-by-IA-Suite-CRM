# Fichier : SaveOverload.php

**Chemin :** `modules/Opportunities/SaveOverload.php`
**Type :** `PHP`
**Categorie :** helper (conversion monetaire)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la fonction `perform_save()` qui convertit le montant d'une opportunite dans la devise de reference (USD) avant la sauvegarde en base.

## Role technique

Fichier procedural declarant la fonction globale `perform_save(&$focus)`. Si `$focus->amount` est non vide, recupere la devise via `BeanFactory`, calcule `amount_usdollar` via `currency->convertToDollar(unformat_number($focus->amount))`. Modifie `$focus` par reference.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `BeanFactory::newBean('Currencies')` | Recuperation du bean Currencies pour la conversion |
| `unformat_number()` | Deformate le nombre saisi (retire separateurs) |
| `number_empty()` | Teste si le montant est significatif |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `perform_save(&$focus)` | fonction globale | Convertit le montant en USD avant sauvegarde |

**Consommateurs identifies dans le repo :**

- `modules/Opportunities/Opportunity.php` (ligne 371 : `perform_save($this)`)

## Points d'attention

- Charge via `require_once` dans `Opportunity::save()`.
- Si `amount` est vide ou nul, aucune conversion n'est effectuee.
- Le montant USD n'est pas mis a jour automatiquement si le taux de change change apres la sauvegarde.
