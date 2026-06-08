# 📁 Reminders

**Chemin :** `modules/Reminders/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Reminders gère les rappels associés aux réunions et appels dans SuiteCRM. Un rappel déclenche une notification à une date/heure définie avant l'activité planifiée.

## ⚙️ Responsabilité technique
Bean `Reminder` (hérite de `SugarBean`). Utilisé par `Meeting::save()` pour stocker les données de rappels JSON.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Reminder.php` | Bean principal des rappels | [→ fiche](Reminder.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `Meeting::save()`, `AOS_Contracts::save()` (rappel de renouvellement)
- **Lié à :** `Reminders_Invitees` (destinataires du rappel)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
