# 📁 enums

**Chemin :** `include/CalendarSync/domain/enums/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les énumérations du domaine CalendarSync. Elles définissent le vocabulaire des actions possibles (CREATE/UPDATE/DELETE), des localisations (INTERNAL/EXTERNAL), des stratégies de résolution de conflits et des types d'événements. Ces enums constituent le langage ubiquitaire du module.

## ⚙️ Responsabilité technique
Enums PHP typées (backed enums avec valeur string pour la plupart). Utilisées pour le typage fort dans toutes les couches du module et pour la sérialisation/désérialisation via `::from()` et `::tryFrom()`.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarSyncAction.php` | Actions de sync possibles : CREATE, UPDATE, DELETE | [→ fiche](CalendarSyncAction.doc.md) |
| `ConflictResolution.php` | Stratégies de résolution de conflits : TIMESTAMP, EXTERNAL_BASED, INTERNAL_BASED | [→ fiche](ConflictResolution.doc.md) |
| `CalendarLocation.php` | Localisation d'un événement : INTERNAL (SuiteCRM) ou EXTERNAL (tiers) | [→ fiche](CalendarLocation.doc.md) |
| `CalendarEventType.php` | Type d'événement calendrier (MEETING, autres cas INCONNU) | [→ fiche](CalendarEventType.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** rien (enums purs)
- **Expose :** typage des actions, localisations, stratégies et types d'événements — consommées par toutes les couches du module CalendarSync
- **Flux typique :** Les enums sont référencées dans `CalendarSyncOperation`, `CalendarSyncOrchestrator`, `CalendarSyncOperationDiscovery`, `CalendarEventConflictResolver`, `CalendarSync`, `CalendarSyncConfig`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Connaître les actions de synchronisation possibles | [`CalendarSyncAction.php`](CalendarSyncAction.doc.md) |
| Comprendre les stratégies de résolution de conflits | [`ConflictResolution.php`](ConflictResolution.doc.md) |
| Distinguer événement interne et externe | [`CalendarLocation.php`](CalendarLocation.doc.md) |
| Comprendre les types d'événements gérés | [`CalendarEventType.php`](CalendarEventType.doc.md) |

---

## ⚠️ Zones INCONNU
- `CalendarEventType` : seul le cas `MEETING` est confirmé. D'autres cas potentiels (Task, Call ?) non confirmés dans le code source.
- `CalendarLocation` : méthode `getOpposite()` attendue dans `CalendarSyncOperationDiscovery` — existence dans l'enum à confirmer.
