# 📁 application

**Chemin :** `custom/Extension/application/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Extensions applicatives SuiteCRM de niveau global (toute l'application, par opposition aux extensions de module). Contient les personnalisations qui affectent le comportement transversal du CRM : hooks globaux, groupements JS personnalisés, etc.

## ⚙️ Responsabilité technique
Convention SuiteCRM : `custom/Extension/application/Ext/` est compilé dans `custom/application/Ext/` via le `Quick Repair and Rebuild`. Ces fichiers ont priorité sur le core.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Ext/` | Extensions compilées (LogicHooks, JSGroupings, etc.) | [→ CONTEXT](Ext/CONTEXT.md) |

### Fichiers documentés
_(aucun fichier à ce niveau)_

---

## 🔗 Interfaces avec le reste du repo
- **Expose :** extensions globales applicatives (hooks, JS groupings personnalisés)

---

## ⚠️ Zones INCONNU
- Autres contenus potentiels dans `application/` non documentés
