# 📁 Services

**Chemin :** `include/CalendarSync/migrations/Services/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les services de migration CalendarSync. Il gère la transition one-shot depuis l'ancien système Google Sync (legacy) vers le nouveau système CalendarSync basé sur `CalendarAccount`. Il inclut le registre d'idempotence des migrations et l'orchestrateur de migration Google.

## ⚙️ Responsabilité technique
`MigrationRegistry` assure l'idempotence via `INSERT IGNORE` dans la table `config`. `LegacyGoogleSyncMigrationService` orchestre des sous-services spécialisés (UserMigration, ProviderMigration, MeetingMigration, SchedulerMigration — hors périmètre documenté).

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `MigrationRegistry.php` | Suivi d'idempotence des migrations via table `config` BDD | [→ fiche](MigrationRegistry.doc.md) |
| `LegacyGoogleSyncMigrationService.php` | Migration one-shot legacy Google Sync → nouveau système CalendarSync | [→ fiche](LegacyGoogleSyncMigrationService.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `UserMigrationService.php`, `ProviderMigrationService.php`, `MeetingMigrationService.php`, `SchedulerMigrationService.php` | Services spécialisés — hors périmètre de cette vague |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `DBManagerFactory`, `LoggerManager`, sous-services de migration
- **Expose :** `MigrationRegistry::hasMigrationRun()` / `recordMigrationCompletion()` — utilisé par tous les services de migration
- **Flux typique :** Un script d'administration appelle `LegacyGoogleSyncMigrationService`, qui vérifie via `MigrationRegistry` si la migration a déjà été jouée, puis orchestre les sous-services.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Vérifier si une migration CalendarSync a déjà été exécutée | [`MigrationRegistry.php`](MigrationRegistry.doc.md) |
| Comprendre la migration depuis l'ancien Google Sync | [`LegacyGoogleSyncMigrationService.php`](LegacyGoogleSyncMigrationService.doc.md) |

---

## ⚠️ Zones INCONNU
- Point d'entrée de `LegacyGoogleSyncMigrationService` non identifié (script ou endpoint admin ?).
- Sous-services de migration (UserMigration, ProviderMigration, etc.) non documentés.
- `MigrationRegistry::hasMigrationRun()` retourne `false` en cas d'erreur BDD — migration peut être rejouée accidentellement.
