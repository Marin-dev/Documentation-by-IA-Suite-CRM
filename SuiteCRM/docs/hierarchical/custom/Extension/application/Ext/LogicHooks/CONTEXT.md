# 📁 LogicHooks

**Chemin :** `custom/Extension/application/Ext/LogicHooks/`
**Profondeur :** 6
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les hooks de logique applicative globaux (niveau application, pas module). Le seul fichier documenté enregistre le hook `after_save` du moteur de workflows AOW (Advanced OpenWorkflow), déclenchant l'évaluation des workflows sur chaque bean sauvegardé.

## ⚙️ Responsabilité technique
Fichiers d'extension SuiteCRM compilés lors du `Quick Repair and Rebuild`. Ces fichiers sont fusionnés par le système d'extensions dans `cache/` et chargés par le framework SuiteCRM pour alimenter `$hook_array`. Ne pas modifier directement — passer par l'interface d'administration pour les changements.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOW_WorkFlow_Hook.php` | Enregistre after_save → AOW_WorkFlow::run_bean_flows() (priorité 99) | [→ fiche](AOW_WorkFlow_Hook.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `modules/AOW_WorkFlow/AOW_WorkFlow.php` (méthode `run_bean_flows`)
- **Expose :** hook `after_save` global sur tous les beans de l'application
- **Flux typique :** `SugarBean::save()` → trigger `after_save` → `AOW_WorkFlow::run_bean_flows($bean)` → évaluation des workflows configurés

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le déclenchement des workflows AOW | [`AOW_WorkFlow_Hook.php`](AOW_WorkFlow_Hook.php.doc.md) |

---

## ⚠️ Zones INCONNU
- Autres hooks applicatifs potentiellement présents mais non documentés
