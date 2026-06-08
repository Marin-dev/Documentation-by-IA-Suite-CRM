# 📁 FP_events

**Chemin :** `modules/FP_events/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module FP_events gère les événements (séminaires, conférences, formations) dans SuiteCRM. Il permet de créer des événements avec inscription de participants (contacts, leads). Les événements apparaissent dans le calendrier. Inclut un point d'entrée de réponse (`responseEntryPoint`) pour les inscriptions web.

## ⚙️ Responsabilité technique
Bean `FP_events` (hérite de `FP_events_sugar`, Module Builder). Vues détail et édition personnalisées. Dashlet dédié.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail et édition | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des événements | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `FP_events.php` | Bean principal des événements | [→ fiche](FP_events.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `responseEntryPoint.php` | Point d'entrée pour les réponses d'inscription | [→ fiche](responseEntryPoint.doc.md) |
| `vardefs.php` | Schéma de la table `fp_events` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `FP_Event_Locations`, module Contacts, Leads (inscriptions)
- **Consommé par :** Module Calendar (les événements apparaissent dans le calendrier)
- **Flux typique :** Création événement → inscription participants → réponse via `responseEntryPoint` → visible dans le calendrier

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
