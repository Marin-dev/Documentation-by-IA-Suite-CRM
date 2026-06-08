# 📁 Extension

**Chemin :** `custom/Extension/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Dossier racine du système d'extensions SuiteCRM. Contient toutes les personnalisations applicatives et de modules qui sont compilées via le mécanisme d'extensions (Quick Repair and Rebuild). Ces fichiers surchargent ou complètent le comportement du core sans le modifier directement.

## ⚙️ Responsabilité technique
Architecture d'extensions SuiteCRM : `custom/Extension/{scope}/{type}/` où `scope` peut être `application` (global) ou `modules/{ModuleName}` (par module), et `type` peut être `Ext/LogicHooks/`, `Ext/JSGroupings/`, etc. Les fichiers sont fusionnés dans `custom/{scope}/Ext/` lors du rebuild.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `application/` | Extensions globales (hooks applicatifs, JS groupings...) | [→ CONTEXT](application/CONTEXT.md) |

### Fichiers documentés
_(aucun fichier à ce niveau)_

---

## 🔗 Interfaces avec le reste du repo
- **Expose :** ensemble des extensions personnalisées (hooks, configurations JS, etc.)
- **Flux typique :** fichiers ajoutés ici → `Quick Repair and Rebuild` → fusionnés dans `custom/application/Ext/` ou `custom/modules/{Module}/Ext/`

---

## ⚠️ Zones INCONNU
- Extensions de modules (`custom/Extension/modules/`) potentiellement présentes mais non documentées
