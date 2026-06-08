# 📁 application

**Chemin :** `include/CalendarSync/application/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier constitue la couche applicative du module CalendarSync. Il orchestre le cycle complet de synchronisation : découverte des différences entre calendriers, exécution ou planification des opérations, et gestion des jobs asynchrones. C'est le cerveau fonctionnel du module entre la façade publique et l'infrastructure.

## ⚙️ Responsabilité technique
Pattern Pipeline dans `CalendarSyncOrchestrator` : récupération des comptes → interrogation des providers → découverte des différences (`CalendarSyncOperationDiscovery`) → exécution ou soumission en file. `CalendarSyncJobManager` agit comme garde-fou anti-doublon. Support des modes synchrone et asynchrone.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarSyncOrchestrator.php` | Orchestrateur principal du cycle de synchronisation calendrier | [→ fiche](CalendarSyncOrchestrator.doc.md) |
| `CalendarSyncOperationDiscovery.php` | Service de "diff" entre calendriers — produit la liste des opérations à exécuter | [→ fiche](CalendarSyncOperationDiscovery.doc.md) |
| `CalendarSyncJobManager.php` | Vérification des jobs actifs pour éviter les doublons en mode async | [→ fiche](CalendarSyncJobManager.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `CalendarAccountRepository`, `CalendarAccountValidator`, `CalendarProviderRegistry`, `CalendarSyncConfig`, `CalendarSyncJobFactory`, `CalendarSyncOperationDiscovery`, `CalendarEventConflictResolver`, enums du domaine
- **Expose :** `syncAllCalendarAccounts()`, `syncCalendarAccount()`, `syncEvent()` — consommés par la façade `CalendarSync`
- **Flux typique :** `CalendarSync` (façade) appelle `CalendarSyncOrchestrator::syncCalendarAccount()`, qui appelle `CalendarSyncOperationDiscovery::discoverSyncOperations()` pour le diff, puis exécute chaque opération via les providers.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le flux complet de synchronisation | [`CalendarSyncOrchestrator.php`](CalendarSyncOrchestrator.doc.md) |
| Comprendre comment les différences sont détectées | [`CalendarSyncOperationDiscovery.php`](CalendarSyncOperationDiscovery.doc.md) |
| Comprendre la protection anti-doublon des jobs | [`CalendarSyncJobManager.php`](CalendarSyncJobManager.doc.md) |

---

## ⚠️ Zones INCONNU
- `CalendarSyncOrchestrator::discoverAndExecuteOperations()` : les opérations au-delà de `$maxOperationsPerAccount` sont silencieusement ignorées.
- `CalendarSyncOperationDiscovery` : paramètre `$targetProvider` accepté mais non utilisé — dette technique potentielle.
- `CalendarSyncJobManager` : `get_list()` sans limite pour les jobs de réunion — potentiellement coûteux.
