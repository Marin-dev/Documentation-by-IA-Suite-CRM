# AOS_Utils.php

**Chemin :** `modules/AOS_Products_Quotes/AOS_Utils.php`
**Type :** PHP - Helper (fonctions utilitaires AOS)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bibliotheque de fonctions utilitaires partagees par tous les modules AOS (Quotes, Invoices, Contracts). Gere principalement la conversion des montants en USD et le chargement de la devise associee a un document.

## Role technique
Fichier de fonctions globales PHP. `perform_aos_save` est appelee avant toute sauvegarde d'un document AOS pour calculer les equivalents en USD de tous les champs montant. Utilise le pattern de nommage `{fieldname}_usdollar` present dans les vardefs AOS.

---

## Fonctions exposees
| Fonction | Role |
|---|---|
| `perform_aos_save($focus)` | Calcule et stocke les equivalents USD de tous les champs montant |
| `fetch_aos_currency($focus)` | Charge le bean `Currencies` correspondant a `$focus->currency_id` |
| `amountToConvertIsDatabaseValue($focus, $fieldName)` | Determine si le montant est deja au format DB (INCONNU — suite du fichier non lue) |
| `number_empty($fieldDef)` | INCONNU — suite du fichier non lue |
| `unformat_number($value)` | INCONNU — probablement desformater un montant depuis le format utilisateur |

**Consommateurs :**
- `AOS_Quotes->save()`
- `AOS_Invoices->save()`
- `AOS_Contracts->save()`

## Relations cles
- **Appelle :** `BeanFactory::newBean('Currencies')`, `$currency->convertToDollar()`
- **Depends on :** Schema des vardefs — presence de champs `*_usdollar`

---

## Points d'attention
- Si `currency_id` n'est pas definie sur le focus, la devise par defaut est chargee via `$currency->retrieve()` sans argument.
- La conversion utilise `unformat_number()` si la valeur n'est pas deja au format DB — detecte via `amountToConvertIsDatabaseValue()`.
- Les warnings sont loggues si des champs sont absents du focus.
