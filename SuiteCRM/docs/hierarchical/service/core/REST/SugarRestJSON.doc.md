# SugarRestJSON.php

**Chemin :** `service/core/REST/SugarRestJSON.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation REST au format JSON. Décode les données `rest_data` de la requête POST (JSON), appelle la méthode d'implémentation correspondante, et encode la réponse en JSON. Supporte le JSONP via le paramètre GET `jsoncallback`.

**Type :** service

---

## Dépendances clés
- `service/core/REST/SugarRest.php` — classe parente
- `getJSONObj()` — helper global pour encoder/décoder JSON
- `SoapError` — classe d'erreur

---

## Exports/Symboles principaux
- `SugarRestJSON` — (étend `SugarRest`)
  - `serve()` — décode `$GLOBALS['RAW_REQUEST']['rest_data']` (JSON) et dispatche via `$this->implementation->{$method}(...array_values($data))`
  - `generateResponse($input)` — encode `$input` en JSON + headers `Content-Type: application/json; charset=UTF-8`
  - `fault($errorObject)` — stocke l'erreur dans `$this->faultServer->faultObject`
  - `generateFaultResponse($errorObject)` — encode l'objet erreur en JSON (ou JSONP)

---

## Interactions
- **Appelé par :** `SugarRestService->serve()` (service/core/SugarRestService.php) via `response_type=json`
- **Appelle :** classe d'implémentation (ex. `SugarWebServiceImplv4_1`)

---

## Notes
- Utilise `$GLOBALS['RAW_REQUEST']['rest_data']` pour éviter les injections (ligne 87) — pas `$_REQUEST` directement
- Le paramètre `application` est mappé vers `application_name` si manquant (ligne 97-99)
- JSONP activé si `$_GET["jsoncallback"]` est défini
- `fault()` ne génère pas immédiatement la réponse — stocke dans `faultObject` ; c'est `generateResponse()` qui détecte et appelle `generateFaultResponse()` (ligne 66-67)
