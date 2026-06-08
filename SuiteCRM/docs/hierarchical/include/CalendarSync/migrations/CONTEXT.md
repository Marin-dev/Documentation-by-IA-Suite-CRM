# 📁 migrations

**Chemin :** `include/CalendarSync/migrations/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier gère les migrations de données CalendarSync. Il assure la transition depuis l'ancien système de synchronisation Google (stockage dans les préférences utilisateurs) vers le nouveau système basé sur `CalendarAccount` et `ExternalOAuthConnection`. C'est une couche one-shot, idempotente, destinée à être jouée une seule fois lors de la mise à jour.

## ⚙️ Responsabilité technique
Orchestration de services de migration spécialisés (utilisateurs, providers, réunions, scheduler) avec registre d'idempotence via la table `config` BDD. Utilise `INSERT IGNORE` pour la protection contre les exécutions multiples.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Services/` | Services de migration : registre d'idempotence + orchestrateur migration Google | [→ CONTEXT](Services/CONTEXT.md) |

### Fichiers documentés
Aucun fichier directement dans `migrations/`.

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `DBManagerFactory`, sous-services de migration, `MigrationRegistry`
- **Expose :** services de migration — appelés depuis un script/endpoint d'administration (INCONNU)
- **Flux typique :** Lors d'une mise à jour, un script appelle `LegacyGoogleSyncMigrationService`, qui orchestre la migration des données Google legacy vers le nouveau format `CalendarAccount`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la migration depuis l'ancien Google Sync | [`Services/LegacyGoogleSyncMigrationService.php`](Services/LegacyGoogleSyncMigrationService.doc.md) |
| Vérifier l'état d'une migration | [`Services/MigrationRegistry.php`](Services/MigrationRegistry.doc.md) |

---

## ⚠️ Zones INCONNU
- Point d'entrée des migrations non identifié (script CLI ou endpoint admin).
- Sous-services UserMigration, ProviderMigration, MeetingMigration, SchedulerMigration non documentés.
