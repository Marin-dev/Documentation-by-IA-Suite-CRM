# 📁 Ext

**Chemin :** `custom/Extension/application/Ext/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Dossier d'extensions applicatives compilées par le système d'extensions SuiteCRM. Contient les fichiers générés ou personnalisés qui modifient le comportement global de l'application (hooks, groupements JS, etc.) sans toucher au code core.

## ⚙️ Responsabilité technique
Structure conventionnelle des extensions SuiteCRM : chaque sous-dossier correspond à un type d'extension (LogicHooks, JSGroupings, etc.). Les fichiers sont fusionnés lors du `Quick Repair and Rebuild` dans le répertoire `cache/`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `LogicHooks/` | Hooks de logique applicative globaux (ex. déclenchement AOW) | [→ CONTEXT](LogicHooks/CONTEXT.md) |

### Fichiers documentés
_(aucun fichier à ce niveau)_

---

## 🔗 Interfaces avec le reste du repo
- **Expose :** hooks et extensions globales fusionnés dans le cache SuiteCRM
- **Flux typique :** `Quick Repair and Rebuild` → fusion des fichiers Ext → chargement par le framework

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir le hook AOW after_save global | [`LogicHooks/AOW_WorkFlow_Hook.php`](LogicHooks/AOW_WorkFlow_Hook.php.doc.md) |

---

## ⚠️ Zones INCONNU
- Autres types d'extensions dans ce dossier Ext (JSGroupings, etc.) : non documentés
