# SugarWebServiceUtilv3.php

**Chemin :** `service/v3/SugarWebServiceUtilv3.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Helper utilitaire pour la v3 de l'API. Étend `SoapHelperWebServices` et surcharge `get_name_value()` pour gérer les objets `Link2` qui ne peuvent pas être sérialisés directement.

**Type :** helper

---

## Dépendances clés
- `service/core/SoapHelperWebService.php` — classe parente

---

## Exports/Symboles principaux
- `SugarWebServiceUtilv3` — (étend `SoapHelperWebServices`)
  - `get_name_value($field, $value)` — surcharge : si `$value` est une instance de `Link2` sans méthode `__toString()`, retourne `''` au lieu de l'objet

---

## Interactions
- **Injecté dans :** `SugarWebServiceImplv3::$helperObject`
- **Étendu par :** `SugarWebServiceUtilv3_1`

---

## Notes
- Correction de bug : les objets `Link2` provoqueraient des erreurs de sérialisation SOAP sans cette surcharge
