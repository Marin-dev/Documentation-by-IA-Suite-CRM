# 📁 services

**Chemin :** `include/CalendarSync/domain/services/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les services de domaine du module CalendarSync. Il couvre : l'accès aux données (repository des comptes), la validation des comptes avant synchronisation, la résolution de conflits entre événements internes et externes, la construction de requêtes d'événements, et la sérialisation des événements pour les jobs asynchrones.

## ⚙️ Responsabilité technique
Services sans état (stateless) ou à état minimal, implémentant la logique métier pure du domaine. Chaque service a une responsabilité unique. Le repository utilise `BeanFactory` et SQL natif. Le conflict resolver applique des stratégies configurables via l'enum `ConflictResolution`. Le serializer utilise JSON pour la persistance dans les jobs scheduler.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarAccountRepository.php` | Accès BDD aux comptes calendrier (lecture filtrée et batch) | [→ fiche](CalendarAccountRepository.doc.md) |
| `CalendarAccountValidator.php` | Validation d'un compte calendrier avant toute opération de sync | [→ fiche](CalendarAccountValidator.doc.md) |
| `CalendarEventConflictResolver.php` | Résolution de conflits entre versions interne et externe d'un événement | [→ fiche](CalendarEventConflictResolver.doc.md) |
| `CalendarEventQuery.php` | Value object représentant les critères d'une requête d'événements | [→ fiche](CalendarEventQuery.doc.md) |
| `CalendarEventSerializer.php` | Sérialisation/désérialisation JSON d'événements calendrier | [→ fiche](CalendarEventSerializer.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `BeanFactory` (core SuiteCRM), `ConflictResolution` (enum), `CalendarAccountEvent` (entities), `DBManagerFactory`
- **Expose :** accès aux comptes calendrier, validation, résolution de conflits, paramétrage des requêtes d'événements
- **Flux typique :** `CalendarSyncOrchestrator` appelle `CalendarAccountRepository` pour charger les comptes, `CalendarAccountValidator` pour les valider, puis `CalendarSyncOperationDiscovery` appelle `CalendarEventConflictResolver` pour résoudre les conflits lors du diff.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment les comptes calendrier sont chargés | [`CalendarAccountRepository.php`](CalendarAccountRepository.doc.md) |
| Comprendre la stratégie de résolution de conflits | [`CalendarEventConflictResolver.php`](CalendarEventConflictResolver.doc.md) |
| Comprendre la validation d'un compte avant sync | [`CalendarAccountValidator.php`](CalendarAccountValidator.doc.md) |
| Comprendre comment les événements sont persistés dans les jobs | [`CalendarEventSerializer.php`](CalendarEventSerializer.doc.md) |
| Comprendre les paramètres d'une requête d'événements | [`CalendarEventQuery.php`](CalendarEventQuery.doc.md) |

---

## ⚠️ Zones INCONNU
- `CalendarAccountRepository` : ordre SQL `last_sync_attempt_date IS NOT NULL ASC` — comportement exact selon le SGBD à vérifier.
- `CalendarEventSerializer` : échec silencieux (retourne `''` ou `null`) — l'appelant doit vérifier.
- `CalendarEventConflictResolver` : tie-breaker en mode TIMESTAMP avec timestamps égaux non implémenté.
