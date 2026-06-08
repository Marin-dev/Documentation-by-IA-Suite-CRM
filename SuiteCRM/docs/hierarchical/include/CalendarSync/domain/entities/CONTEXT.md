# 📁 entities

**Chemin :** `include/CalendarSync/domain/entities/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les entités de domaine du module CalendarSync. Il modélise les objets métier fondamentaux : un événement calendrier unifié (`CalendarAccountEvent`) et une opération de synchronisation (`CalendarSyncOperation`). Ces entités circulent entre toutes les couches du système (providers, discovery, orchestrateur) sans dépendre d'une couche technique spécifique.

## ⚙️ Responsabilité technique
Implémente le pattern Entity et Value Object du DDD. `CalendarAccountEvent` est l'DTO central avec calcul de checksum MD5 à la construction pour des comparaisons rapides. `CalendarSyncOperation` est un objet immuable representant une commande (CREATE/UPDATE/DELETE) sur un événement.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarAccountEvent.php` | Entité unifiée représentant un événement calendrier (interne ou externe) | [→ fiche](CalendarAccountEvent.doc.md) |
| `CalendarSyncOperation.php` | Value object immuable représentant une opération de sync (CREATE/UPDATE/DELETE) | [→ fiche](CalendarSyncOperation.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `CalendarEventType` (enum), `CalendarLocation` (enum), `CalendarSyncAction` (enum), `DateTimeHelper`
- **Expose :** `CalendarAccountEvent` et `CalendarSyncOperation` — utilisés par toutes les couches du module CalendarSync
- **Flux typique :** Les providers créent des `CalendarAccountEvent`, le discovery les compare et produit des `CalendarSyncOperation`, l'orchestrateur exécute ces opérations.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la structure d'un événement calendrier | [`CalendarAccountEvent.php`](CalendarAccountEvent.doc.md) |
| Comprendre ce qu'est une opération de sync | [`CalendarSyncOperation.php`](CalendarSyncOperation.doc.md) |
| Trouver le checksum de comparaison d'événements | [`CalendarAccountEvent.php`](CalendarAccountEvent.doc.md) |

---

## ⚠️ Zones INCONNU
- `CalendarAccountEvent` : le checksum ne se recalcule pas si les propriétés sont modifiées après construction — comportement potentiellement surprenant.
- `CalendarSyncOperation` : pour CREATE, `subject_id` est vide — l'ID est généré lors de l'exécution réelle.
