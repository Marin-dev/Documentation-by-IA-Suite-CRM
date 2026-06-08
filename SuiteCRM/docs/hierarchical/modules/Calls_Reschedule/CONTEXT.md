# 📁 Calls_Reschedule

**Chemin :** `modules/Calls_Reschedule/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Calls_Reschedule gère le report des appels dans SuiteCRM. Permet d'enregistrer les historiques de report d'un appel (combien de fois, à quelle date, pour quelle raison).

## ⚙️ Responsabilité technique
Bean `Calls_Reschedule` (hérite de `Calls_Reschedule_sugar`, Module Builder). Module généré automatiquement.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Calls_Reschedule.php` | Bean report d'appel | [→ fiche](Calls_Reschedule.php.doc.md) |
| `reschedule_count.php` | Comptage des reports | [→ fiche](reschedule_count.php.doc.md) |
| `Reschedule_popup.php` | Popup de report | [→ fiche](Reschedule_popup.php.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Module `Calls` (action `Reschedule.php`)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
