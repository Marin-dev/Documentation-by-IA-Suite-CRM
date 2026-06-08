# 📁 infrastructure

**Chemin :** `include/CalendarSync/infrastructure/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier constitue la couche infrastructure du module CalendarSync. Il implémente les détails techniques d'exécution : les providers de calendrier (accès aux APIs externes), le registre de providers, et la gestion des jobs asynchrones dans la file du scheduler SuiteCRM.

## ⚙️ Responsabilité technique
Trois sous-couches : `registry/` (découverte et cache des providers), `providers/` (pattern Template Method pour les opérations CRUD sur événements), `jobs/` (soumission et nettoyage des jobs scheduler). Cette couche dépend du domaine mais pas de la couche applicative.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `registry/` | Registre central des providers de calendrier (découverte, cache, instanciation) | [→ CONTEXT](registry/CONTEXT.md) |
| `providers/` | Classe abstraite Template Method pour tous les providers de calendrier | [→ CONTEXT](providers/CONTEXT.md) |
| `jobs/` | Création, soumission et nettoyage des jobs scheduler asynchrones | [→ CONTEXT](jobs/CONTEXT.md) |

### Fichiers documentés
Aucun fichier directement dans `infrastructure/` (tous dans les sous-dossiers).

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `providers/external/` (dossier) | Providers concrets (Google, CalDAV, JSON) — hors périmètre de cette vague de documentation |
| `jobs/JobStatusHelper.php` | Utilitaire de constantes — hors périmètre de cette vague |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarJobQueue`, `BeanFactory`, `ModuleInstaller`, `CalendarSyncOperationSerializer`, `CalendarProviderType`, entités et services du domaine
- **Expose :** accès unifié aux providers (via `CalendarProviderRegistry`), CRUD d'événements (via `AbstractCalendarProvider`), gestion de jobs (via `CalendarSyncJobFactory` / `CalendarSyncJobCleaner`)
- **Flux typique :** `CalendarSyncOrchestrator` (couche applicative) appelle `CalendarProviderRegistry` pour obtenir le bon provider, puis appelle ses méthodes CRUD. En mode async, il soumet des jobs via `CalendarSyncJobFactory`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre quels providers sont disponibles | [`registry/CalendarProviderRegistry.php`](registry/CalendarProviderRegistry.doc.md) |
| Comprendre le contrat d'un provider de calendrier | [`providers/AbstractCalendarProvider.php`](providers/AbstractCalendarProvider.doc.md) |
| Comprendre la création de jobs asynchrones | [`jobs/CalendarSyncJobFactory.php`](jobs/CalendarSyncJobFactory.doc.md) |
| Comprendre la gestion des jobs obsolètes | [`jobs/CalendarSyncJobCleaner.php`](jobs/CalendarSyncJobCleaner.doc.md) |

---

## ⚠️ Zones INCONNU
- Providers concrets (GoogleCalendarProvider, CalDAVProvider, JsonFileCalendarProvider, SuiteCRMInternalCalendarProvider) : non documentés.
- `CalendarAccountRelationshipManager` : référencé dans `AbstractCalendarProvider` mais non documenté.
- `JobStatusHelper` : utilitaire non documenté.
