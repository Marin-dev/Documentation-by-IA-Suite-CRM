# 📁 providers

**Chemin :** `include/CalendarSync/infrastructure/providers/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient la classe abstraite de base pour tous les fournisseurs de calendrier (Google Calendar, CalDAV, JSON de test, SuiteCRM interne). Elle définit le contrat des opérations CRUD sur les événements calendrier et garantit une gestion cohérente du timestamp de synchronisation.

## ⚙️ Responsabilité technique
Pattern Template Method : les méthodes publiques `final` (`createEventFromSource`, `updateEventFromSource`, `deleteEvent`) délèguent aux méthodes abstraites `doCreateEvent`, `doUpdateEvent`, `doDeleteEvent` que chaque provider concret implémente. Assure que `setLastSync()` est toujours appelé avant chaque opération.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AbstractCalendarProvider.php` | Classe abstraite Template Method pour tous les providers de calendrier | [→ fiche](AbstractCalendarProvider.doc.md) |

### Fichiers non documentés (volontairement)
Aucun — les providers concrets (Google, CalDAV, JSON, SuiteCRM interne) sont dans `external/` (non documentés dans ce périmètre).

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `CalendarAccountEvent`, `CalendarEventQuery`, `CalendarAccountEventFactory`, `CalendarConnectionTestResult`, `CalendarSyncConfig`, `CalendarAccountRelationshipManager`
- **Expose :** interface CRUD d'événements calendrier — consommée par `CalendarSyncOrchestrator`
- **Flux typique :** `CalendarSyncOrchestrator::syncEvent()` appelle `AbstractCalendarProvider::createEventFromSource()` / `updateEventFromSource()` / `deleteEvent()`, qui délèguent à l'implémentation concrete (Google, CalDAV...).

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le contrat d'un provider de calendrier | [`AbstractCalendarProvider.php`](AbstractCalendarProvider.doc.md) |
| Implémenter un nouveau provider de calendrier | [`AbstractCalendarProvider.php`](AbstractCalendarProvider.doc.md) |

---

## ⚠️ Zones INCONNU
- `generateEventId()` utilise `uniqid()` + `date()` — non-unique sous haute concurrence.
- Les providers concrets (GoogleCalendarProvider, CalDAVProvider...) sont dans `external/` et non documentés dans ce périmètre.
