# CalendarEventConflictResolver.php

**Chemin :** `include/CalendarSync/domain/services/CalendarEventConflictResolver.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service de resolution de conflits entre deux versions d'un meme evenement calendrier (interne vs externe). Determine lequel des deux evenements doit "gagner" lors d'une synchronisation bidirectionnelle. Applique la strategie configuree : par timestamp (le plus recent), priorite externe, ou priorite interne.

## Role technique

Classe avec injection de `LoggerManager`. Methode principale `determineWinningEvent()` : 1) validation basique (timestamps aberrants, patterns suspects dans les champs texte), 2) comparaison de checksum (decision rapide si contenu identique), 3) application de la strategie par matching sur enum `ConflictResolution`. Les sous-methodes `resolveBy*` se replient sur le timestamp si les deux evenements ont le meme statut (interne/externe).

---

## Dependances cles

- **Imports principaux :**
  - `ConflictResolution` (enum) — TIMESTAMP / EXTERNAL_BASED / INTERNAL_BASED
  - `LoggerManager` (SuiteCRM core) — logging

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarEventConflictResolver` | classe service | Resolveur de conflits |
| `determineWinningEvent(CalendarAccountEvent, CalendarAccountEvent, ConflictResolution): CalendarAccountEvent` | methode | Determine l'evenement vainqueur |

- **Consommateurs identifies :** `CalendarSyncOperationDiscovery`

## Relations cles

- **Appele par :** `CalendarSyncOperationDiscovery::discoverSyncOperations()`
- **Appelle :** `CalendarAccountEvent::getContentChecksum()`, `getDateModified()`, `isExternal()`
- **Position dans le flux global :** etape de resolution lors du diff, avant la creation d'une operation UPDATE

---

## Points d'attention

- La validation des champs texte (`<script`, `javascript:`, etc. — ligne 117) est un avertissement log, pas un rejet : l'evenement continue son traitement.
- Le check Y2K38 (timestamp > 2147483647 — ligne 112) est egalement un avertissement, pas un blocage.
- Si les deux evenements ont le meme checksum, `determineWinningEvent()` retourne le `targetEvent` — aucun UPDATE n'est genere par l'appelant (optimisation).
- En mode `TIMESTAMP` avec timestamps egaux, le `targetEvent` gagne (pas de tie-breaker par ID mentionne dans les commentaires mais non implemente dans le code actuel).
