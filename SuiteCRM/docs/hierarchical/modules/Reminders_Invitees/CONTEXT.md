# 📁 Reminders_Invitees

**Chemin :** `modules/Reminders_Invitees/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Reminders_Invitees gère les invités (destinataires) des rappels dans SuiteCRM. Lie un rappel à des utilisateurs, contacts ou leads spécifiques.

## ⚙️ Responsabilité technique
Bean `Reminder_Invitee` (hérite de `SugarBean`). Table de liaison entre rappels et invités.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Reminder_Invitee.php` | Bean invité d'un rappel | [→ fiche](Reminder_Invitee.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Module `Reminders`, système de notifications
- **Flux typique :** Rappel créé → invités ajoutés → notifications envoyées aux invités

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
