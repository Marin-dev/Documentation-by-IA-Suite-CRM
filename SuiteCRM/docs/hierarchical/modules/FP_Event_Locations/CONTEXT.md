# 📁 FP_Event_Locations

**Chemin :** `modules/FP_Event_Locations/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module FP_Event_Locations gère les lieux d'événements dans SuiteCRM. Un lieu représente une salle, un bâtiment ou une adresse associée aux événements FP_events.

## ⚙️ Responsabilité technique
Bean `FP_Event_Locations` (hérite de `FP_Event_Locations_sugar`, Module Builder). Module simple généré automatiquement.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlet liste des lieux | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `FP_Event_Locations.php` | Bean lieu d'événement | [→ fiche](FP_Event_Locations.doc.md) |
| `vardefs.php` | Schéma de la table des lieux | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Module `FP_events` (relation lieu-événement)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
