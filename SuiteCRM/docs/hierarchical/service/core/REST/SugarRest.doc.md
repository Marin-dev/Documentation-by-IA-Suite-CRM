# SugarRest.php

**Chemin :** `service/core/REST/SugarRest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe de base pour le protocole REST dans SuiteCRM. Elle reçoit les requêtes HTTP entrantes, route vers la méthode appropriée de la classe d'implémentation (via `$_REQUEST['method']`), et gère les erreurs. Sert de parent commun à `SugarRestJSON`, `SugarRestRSS` et `SugarRestSerialize`.

**Type :** service

---

## Dépendances clés
- `SoapError` (soap/SoapError.php) — utilisé pour signaler les erreurs `invalid_call`

---

## Exports/Symboles principaux
- `SugarRest` — classe de base REST
  - `__construct($implementation)` — reçoit et stocke l'instance de la classe d'implémentation
  - `serve()` — dispatche vers `$this->implementation->{$_REQUEST['method']}()` ; si pas de méthode : affiche la réflexion de classe (WSDL-like)
  - `generateResponse($input)` — sortie brute via `print_r` (à surcharger dans les sous-classes)
  - `fault($errorObject)` — délègue à `$this->faultServer->generateFaultResponse()`
  - `generateFaultResponse($errorObject)` — émet HTTP 500 avec détails de l'erreur

---

## Interactions
- **Appelé par :** `SugarRestService` (service/core/SugarRestService.php) — instancie les sous-classes
- **Appelle :** classe d'implémentation (ex. `SugarRestServiceImpl`, `SugarWebServiceImplv4_1`)
- **Sous-classes :** `SugarRestJSON`, `SugarRestRSS`, `SugarRestSerialize`

---

## Notes
- La méthode `serve()` expose la structure de la classe d'implémentation via `ReflectionClass` si aucun paramètre `method` n'est fourni — equivalent d'un "WSDL" REST
- `generateFaultResponse` n'utilise pas JSON même pour des réponses REST — c'est la version HTML de base (surcharge nécessaire dans les sous-classes)
