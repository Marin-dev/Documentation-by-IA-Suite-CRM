# 📁 custom

**Chemin :** `custom/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient toutes les personnalisations et surcharges de SuiteCRM sans toucher au code core. Il héberge les extensions applicatives (hooks globaux via le système d'extensions), les configurations de modules personnalisées (visibilité recherche unifiée), et tout ajout réalisé via l'interface d'administration ou directement par un développeur. Ces fichiers survivent aux mises à jour SuiteCRM.

## ⚙️ Responsabilité technique
Architecture de surcharge SuiteCRM : les fichiers dans `custom/` ont priorité sur leurs équivalents dans le core. Le sous-dossier `Extension/` utilise un mécanisme de compilation (Quick Repair and Rebuild) qui fusionne les fichiers d'extension dans `custom/application/Ext/` et `custom/modules/{Module}/Ext/`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Extension/` | Extensions compilées : hooks applicatifs, JS groupings personnalisés | [→ CONTEXT](Extension/CONTEXT.md) |
| `modules/` | Surcharges de configuration par module (recherche unifiée, etc.) | [→ CONTEXT](modules/CONTEXT.md) |

### Fichiers documentés
_(tous les fichiers sont dans les sous-dossiers)_

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** framework SuiteCRM (système d'extensions, moteur de recherche unifiée, AOW)
- **Expose :** hook `after_save` global (AOW) et configuration de la recherche unifiée
- **Flux typique :** `SugarBean::save()` → `after_save` → `AOW_WorkFlow::run_bean_flows()` (via hook de `custom/Extension/application/Ext/LogicHooks/`)

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le déclenchement des workflows AOW | [`Extension/application/Ext/LogicHooks/AOW_WorkFlow_Hook.php`](Extension/application/Ext/LogicHooks/AOW_WorkFlow_Hook.php.doc.md) |
| Modifier la visibilité des modules dans la recherche globale | [`modules/unified_search_modules_display.php`](modules/unified_search_modules_display.php.doc.md) |

---

## ⚠️ Zones INCONNU
- Extensions de modules (`custom/Extension/modules/`) potentiellement présentes mais non documentées
- Autres fichiers de surcharge `custom/` non couverts par les fiches documentées
