# CalendarEventSerializer.php

**Chemin :** `include/CalendarSync/domain/services/CalendarEventSerializer.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service de serialisation/deserialisation des evenements calendrier (`CalendarAccountEvent`) en JSON. Utilise pour stocker les evenements dans le champ `data` des jobs scheduler lors de la synchronisation asynchrone.

## Role technique

Classe de service stateless. `serializeEvent()` encode toutes les proprietes de l'evenement en JSON (dates au format ISO 8601/ATOM). `deserializeEvent()` reconstruit l'objet `CalendarAccountEvent` depuis le JSON. Utilise `JSON_THROW_ON_ERROR` pour la detection d'erreurs.

---

## Dependances cles

- **Imports principaux :**
  - `CalendarEventType` (enum) — recontruction du type d'evenement
  - `CalendarAccountEvent` — type serialise/deserialise

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarEventSerializer` | classe service | Serialiseur d'evenements |
| `serializeEvent(CalendarAccountEvent): string` | methode | JSON de l'evenement (vide si echec) |
| `deserializeEvent(string): ?CalendarAccountEvent` | methode | Reconstruction depuis JSON (null si echec) |

- **Consommateurs identifies :** `CalendarSyncOperationSerializer` (qui serialise l'operation complete incluant l'evenement)

## Relations cles

- **Appele par :** `CalendarSyncOperationSerializer`
- **Appelle :** `CalendarAccountEvent` (getters), `CalendarEventType::from()`
- **Position dans le flux global :** couche de persistance des evenements pour les jobs asynchrones

---

## Points d'attention

- Echec silencieux : retourne `''` ou `null` plutot que de lancer une exception — l'appelant doit verifier.
- Les dates sont serialisees au format ATOM (ISO 8601) — coherent avec `CalendarAccountEvent::DATE_FORMAT`.
