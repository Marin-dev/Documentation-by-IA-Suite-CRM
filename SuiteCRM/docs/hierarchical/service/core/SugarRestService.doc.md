# SugarRestService.php

**Chemin :** `service/core/SugarRestService.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe de service REST concrète. Elle détermine dynamiquement le format de sérialisation (JSON, RSS, Serialize) d'après les paramètres `input_type` et `response_type` de la requête, instancie le serveur approprié, et orchestre la chaîne requête → implémentation → réponse.

**Type :** service

---

## Dépendances clés
- `service/core/SugarWebService.php` — classe parente abstraite
- `service/core/SugarRestServiceImpl.php` — implémentation par défaut
- `service/core/REST/SugarRest*.php` — classes de sérialisation (JSON, RSS, Serialize) chargées dynamiquement

---

## Exports/Symboles principaux
- `SugarRestService` — (étend `SugarWebService`)
  - `__construct($url)` — détermine `$serverClass` et `$responseClass` depuis `$_REQUEST`
  - `serve()` — instancie le serveur et le responseur, chaîne `server->serve()` → `generateResponse()`
  - `registerImplClass($className)` — instancie l'implémentation et le serveur REST
  - `registerFunction(...)` — enregistre les fonctions disponibles (stockées dans `$registeredFunc`)
  - `registerType(...)` — no-op (REST n'a pas de types WSDL)
  - `error($errorObject)` — délègue à `$this->server->fault()`
  - `_getTypeName($name)` — mappe `json`→`JSON`, `rss`→`RSS`, `serialize`→`Serialize`

---

## Interactions
- **Appelé par :** `service/v*/rest.php` (points d'entrée versionnés via `service/core/webservice.php`)
- **Appelle :** classes `SugarRest*`, `SugarRestServiceImpl` (ou implémentation versionnée)

---

## Notes
- `_getTypeName()` vérifie l'existence physique du fichier `service/core/REST/{ClassName}.php` avant de retourner le nom (ligne 82-84) — fallback vers `SugarRest` si absent
- `$registeredFunc` est transmis au serveur via `$this->server->registerd = $this->registeredFunc` (ligne 192) — probablement une faute de frappe (`registerd` au lieu de `registered`)
- `register()` est une no-op (ligne 146-148) — le mécanisme d'enregistrement REST ne nécessite pas d'enregistrement explicite des fonctions côté serveur
