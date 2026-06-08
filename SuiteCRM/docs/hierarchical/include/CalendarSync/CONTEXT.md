# 📁 CalendarSync

**Chemin :** `include/CalendarSync/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier implémente le module complet de synchronisation bidirectionnelle de calendriers entre SuiteCRM et des fournisseurs externes (Google Calendar, CalDAV, etc.). Il gère la synchronisation des réunions SuiteCRM vers les calendriers externes et vice versa, en mode synchrone ou asynchrone via le scheduler. Il couvre également la migration depuis l'ancien système Google Sync legacy.

## ⚙️ Responsabilité technique
Architecture en couches DDD : `domain/` (entités, services, enums), `application/` (orchestration, diff), `infrastructure/` (providers, registry, jobs), `migrations/` (one-shot), `Extension/` (configuration des providers). La façade `CalendarSync` (singleton) est le point d'entrée unique. Pattern Template Method pour les providers, pattern Pipeline pour l'orchestrateur.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `domain/` | Couche domaine : entités, services, enums, value objects, configuration | [→ CONTEXT](domain/CONTEXT.md) |
| `application/` | Couche applicative : orchestrateur de sync, discovery d'opérations, gestion jobs | [→ CONTEXT](application/CONTEXT.md) |
| `infrastructure/` | Couche infrastructure : registry providers, classes abstraites, jobs scheduler | [→ CONTEXT](infrastructure/CONTEXT.md) |
| `migrations/` | Migrations one-shot : transition legacy Google Sync → nouveau système | [→ CONTEXT](migrations/CONTEXT.md) |
| `Extension/` | Configuration extensible des providers (fichiers inclus dynamiquement) | [→ CONTEXT](Extension/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarSync.php` | Façade singleton — point d'entrée unique de toute la synchronisation calendrier | [→ fiche](CalendarSync.doc.md) |
| `CalendarSyncInterface.php` | Contrat (interface) définissant l'API publique du module | [→ fiche](CalendarSyncInterface.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarConfig`, `Configurator`, `BeanFactory`, `DBManagerFactory`, `SugarJobQueue`, `LoggerManager`, `ModuleInstaller` (core SuiteCRM)
- **Expose :** `CalendarSync::getInstance()` — utilisé par le scheduler, les logic hooks sur Meeting, et les vues d'administration
- **Flux typique :** Le scheduler appelle `CalendarSync::syncAllCalendarAccounts()` → `CalendarSyncOrchestrator` charge les comptes, interroge les providers (interne + externe), `CalendarSyncOperationDiscovery` calcule le diff, puis les opérations sont exécutées ou soumises en file.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'API publique du module | [`CalendarSyncInterface.php`](CalendarSyncInterface.doc.md) |
| Comprendre le point d'entrée (façade) | [`CalendarSync.php`](CalendarSync.doc.md) |
| Comprendre le flux complet de synchronisation | [`application/CalendarSyncOrchestrator.php`](application/CalendarSyncOrchestrator.doc.md) |
| Comprendre la gestion des conflits | [`domain/services/CalendarEventConflictResolver.php`](domain/services/CalendarEventConflictResolver.doc.md) |
| Comprendre comment les providers sont gérés | [`infrastructure/registry/CalendarProviderRegistry.php`](infrastructure/registry/CalendarProviderRegistry.doc.md) |

---

## ⚠️ Zones INCONNU
- Les logic hooks CalendarSync sont **désactivés par défaut** (`enableCalendarSyncLogicHooks = false`) — la sync depuis les hooks Meeting nécessite une configuration explicite.
- Point d'entrée des migrations non identifié (script CLI ou endpoint admin).
- Providers concrets (GoogleCalendarProvider, CalDAVProvider) non documentés dans ce périmètre.
- `CalendarAccountRelationshipManager` référencé mais non documenté.
