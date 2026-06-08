# Fichier AOS_Utils.php

**Chemin :** `modules/AOS_Products_Quotes/AOS_Utils.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Bibliothèque utilitaire partagée pour tous les modules AOS (Quotes, Invoices, Contracts, Products, Line Item Groups). Fournit la fonction de conversion des montants en dollars US au moment de la sauvegarde, permettant des comparaisons multi-devises.

## Type
helper

---

## Dépendances clés
- `BeanFactory::newBean('Currencies')` — récupération du taux de change
- `unformat_number()` — dénormalisation des valeurs formatées
- `$currency->convertToDollar()` — conversion via le bean Currency

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `perform_aos_save()` | fonction | Parcourt tous les champs du focus, convertit les montants en USD si un champ `{name}_usdollar` existe |
| `fetch_aos_currency()` | fonction | Récupère le bean Currency selon `$focus->currency_id` |
| `amountToConvertIsDatabaseValue()` | fonction | Détecte si la valeur est déjà une valeur DB (non reformatée) pour éviter double conversion |

## Interactions
- **Appelé par :** `AOS_Quotes::save()`, `AOS_Invoices::save()`, `AOS_Contracts::save()`, `AOS_Products::save()`, `AOS_Line_Item_Groups::save()`, `AOS_Products_Quotes::save()`
- **Appelle :** `BeanFactory::newBean('Currencies')`, `unformat_number()`

## Notes
- `amountToConvertIsDatabaseValue()` compare `$focus->fetched_row[$fieldName]` avec `$focus->$fieldName` — si égaux, la valeur est déjà en format DB et ne doit pas être dé-formatée à nouveau.
- La convention de nommage `{field}_usdollar` est utilisée dans tous les vardefs AOS pour stocker le montant en USD.
