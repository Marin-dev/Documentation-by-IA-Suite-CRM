# SoapError.php

**Chemin :** `soap/SoapError.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe représentant une erreur de service web SOAP/REST. Encapsule un code d'erreur numérique, un nom et une description. Utilisée par toute la couche de services pour signaler les erreurs aux clients.

**Type :** modèle / helper

---

## Dépendances clés
- `soap/SoapErrorDefinitions.php` — tableau global `$error_defs` des codes d'erreur

---

## Exports/Symboles principaux
- `SoapError` — classe d'erreur
  - Propriétés : `$name`, `$number`, `$description`
  - `__construct()` — initialise à `no_error` (code 0)
  - `set_error($error_name)` — charge l'erreur depuis `$error_defs`
  - `get_soap_array()` — retourne un tableau associatif `number/name/description`
  - `getName()`, `getFaultCode()`, `getDescription()` — accesseurs

---

## Interactions
- **Utilisé par :** `SugarWebServiceImpl`, `SoapHelperWebServices`, `SugarRest`, `SugarRestJSON`, `NusoapSoap`, `PHP5Soap`, `SugarRestService`, `JsonRPCServer`
- **Consommateurs identifiés :** quasi tous les fichiers du dossier `service/`

---

## Notes
- Classe centrale partagée par SOAP et REST — malgré son nom, elle est utilisée en REST également
- Par défaut initialisée à `no_error` (code 0) — permet de créer l'objet avant de savoir si une erreur survient
