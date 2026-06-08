# 📁 Alerts

**Chemin :** `modules/Alerts/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Alerts gère les alertes et notifications utilisateur dans SuiteCRM. Il stocke les alertes à afficher dans l'interface (table `alerts`). Module simple sans logique métier complexe.

## ⚙️ Responsabilité technique
Bean `Alert` (hérite de `Basic`). Table `alerts`. Sécurité par ligne désactivée. Non importable.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Alert.php` | Bean alerte/notification | [→ fiche](Alert.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Vues SuiteCRM pour afficher les notifications
- **Flux typique :** Événement déclenché → création `Alert` → affichage dans l'interface

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
