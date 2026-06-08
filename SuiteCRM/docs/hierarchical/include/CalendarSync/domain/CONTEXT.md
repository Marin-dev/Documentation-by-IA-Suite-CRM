# 📁 domain

**Chemin :** `include/CalendarSync/domain/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier constitue la couche domaine du module CalendarSync. Il regroupe les entités métier, les énumérations, les services de domaine et les value objects qui forment le modèle conceptuel de la synchronisation de calendriers entre SuiteCRM et des fournisseurs externes. Il est indépendant des technologies d'infrastructure (BDD, API externes, scheduler).

## ⚙️ Responsabilité technique
Implémentation du Domain Layer selon les principes DDD. Contient : les entités (`entities/`), les value objects (`valueObjects/`), les enums du vocabulaire métier (`enums/`), les services domaine (`services/`), et les fichiers de configuration/interface de la couche (`CalendarSyncConfig`, `CalendarSyncConfigInterface`, `CalendarProviderType`). Aucune dépendance vers les couches application ou infrastructure.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `entities/` | Entités métier : événement calendrier et opération de sync | [→ CONTEXT](entities/CONTEXT.md) |
| `services/` | Services domaine : repository, validation, résolution de conflits, sérialisation | [→ CONTEXT](services/CONTEXT.md) |
| `enums/` | Énumérations : actions, localisations, stratégies de conflit, types d'événements | [→ CONTEXT](enums/CONTEXT.md) |
| `valueObjects/` | Value objects : résultat de test de connexion | [→ CONTEXT](valueObjects/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarSyncConfig.php` | Gestionnaire de configuration CalendarSync (lecture/écriture `sugar_config`) | [→ fiche](CalendarSyncConfig.doc.md) |
| `CalendarSyncConfigInterface.php` | Interface de contrat pour la configuration CalendarSync | [→ fiche](CalendarSyncConfigInterface.doc.md) |
| `CalendarProviderType.php` | Value object décrivant les métadonnées statiques d'un fournisseur de calendrier | [→ fiche](CalendarProviderType.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarConfig`, `Configurator`, `BeanFactory`, `DBManagerFactory`, `LoggerManager` (core SuiteCRM)
- **Expose :** les types de base du module (entités, enums, services) — consommés par les couches `application/` et `infrastructure/`
- **Flux typique :** La couche applicative (`CalendarSyncOrchestrator`) charge les comptes via `CalendarAccountRepository`, valide via `CalendarAccountValidator`, lit la config via `CalendarSyncConfig`, puis déclenche le diff via les entités et services du domaine.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la configuration globale de CalendarSync | [`CalendarSyncConfig.php`](CalendarSyncConfig.doc.md) |
| Comprendre la structure d'un événement calendrier | [`entities/CalendarAccountEvent.php`](entities/CalendarAccountEvent.doc.md) |
| Comprendre comment sont gérés les conflits de sync | [`services/CalendarEventConflictResolver.php`](services/CalendarEventConflictResolver.doc.md) |
| Comprendre les actions de sync disponibles | [`enums/CalendarSyncAction.php`](enums/CalendarSyncAction.doc.md) |
| Comprendre comment charger les comptes calendrier | [`services/CalendarAccountRepository.php`](services/CalendarAccountRepository.doc.md) |

---

## ⚠️ Zones INCONNU
- `CalendarEventType` : seul le cas `MEETING` confirmé — autres types potentiels non vérifiés.
- `CalendarConnectionTestResult` : structure exacte non entièrement documentée.
- `CalendarLocation::getOpposite()` : méthode attendue mais non confirmée dans le fichier source.
