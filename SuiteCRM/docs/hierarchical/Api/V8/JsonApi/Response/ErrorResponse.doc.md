# Fichier : ErrorResponse.php

**Chemin :** `Api/V8/JsonApi/Response/ErrorResponse.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Objet de valeur représentant une réponse d'erreur JSON:API. Encapsule le code HTTP, le titre et le détail de l'erreur. En mode debug, inclut la trace complète de l'exception dans la réponse.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\Core\Config\ApiConfig` | Consulte `ApiConfig::getDebugExceptions()` pour activer le mode debug |
| `Exception` (PHP natif) | Stocké optionnellement pour export dans la réponse en mode debug |
| `JsonSerializable` (PHP natif) | Interface implémentée pour la sérialisation |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ErrorResponse` | classe | DTO d'erreur JSON:API avec support du mode debug |
| `__construct(?bool $debugExceptions)` | méthode publique | Initialise le mode debug depuis `ApiConfig` ou la valeur passée |
| `setStatus(int)` / `getStatus()` | méthodes publiques | Code HTTP de l'erreur |
| `setTitle(string)` / `getTitle()` | méthodes publiques | Titre court de l'erreur |
| `setDetail(string)` / `getDetail()` | méthodes publiques | Description détaillée de l'erreur |
| `setException(Exception)` | méthode publique | Attache une exception pour export en mode debug |
| `getExceptionArray()` | méthode publique | Sérialise l'exception en tableau (code, file, line, message, trace) |
| `jsonSerialize()` | méthode publique | Retourne le tableau `errors` JSON:API, avec exception si mode debug |

---

## Interactions

**Appelé par :** INCONNU (aucune correspondance trouvée dans `Api/` via grep — probablement instancié dans les controllers ou middleware d'erreur)

**Appelle :**
- `Api\Core\Config\ApiConfig::getDebugExceptions()` — lors de la construction (ligne 47)
- `Exception::getCode()`, `getFile()`, `getLine()`, `getMessage()`, `getPrevious()`, `getTrace()`, `getTraceAsString()` — via `exceptionToArray()` (lignes 116-124)

---

## Notes

- Le mode debug est activé soit via le paramètre du constructeur, soit via `ApiConfig::getDebugExceptions()` (ligne 44-49). Il ne doit jamais être actif en production.
- `exceptionToArray()` est récursive via `getPrevious()` (ligne 121), ce qui peut causer une récursion infinie si la chaîne d'exceptions est circulaire.
- TODO mentionné dans le code : "documentation needs to be updated at this point (about debug exceptions)" (ligne 35).
