# 📁 Helper

**Chemin :** `Api/V8/Helper/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les utilitaires transversaux de l'API V8. Ils couvrent l'introspection des VarDefs SuiteCRM (définitions de champs/relations), la liste des modules accessibles par l'utilisateur, et la détection du système d'exploitation.

## ⚙️ Responsabilité technique
Trois classes de service injectable ou statique. `VarDefHelper` et `ModuleListProvider` sont enregistrées dans le DI via `helpers.php`. `OsHelper` est statique, utilisé uniquement dans la configuration des middlewares OAuth2 pour adapter les permissions de fichiers de clés selon l'OS.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `VarDefHelper.php` | Introspection des relations d'un bean SuiteCRM via VarDefs — retourne `[relationName => moduleName]` | [→ fiche](VarDefHelper.doc.md) |
| `ModuleListProvider.php` | Fournit la liste des modules SuiteCRM filtrés par ACL avec labels traduits et actions autorisées | [→ fiche](ModuleListProvider.doc.md) |
| `OsHelper.php` | Détection du système d'exploitation (Windows/Linux/OSX) via `PHP_OS` | [→ fiche](OsHelper.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean` (global SuiteCRM), fonctions ACL globales (`ACLController`, `query_module_access_list`), `PHP_OS`
- **Expose :** `VarDefHelper` consommé par `RelationshipObjectHelper` ; `ModuleListProvider` consommé par `MetaService` ; `OsHelper` consommé par `middlewares.php`
- **Flux typique :** `MetaController::getModuleList()` → `MetaService` → `ModuleListProvider::getModuleList()` → liste filtrée ACL.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'introspection des relations de modules | [`VarDefHelper.php`](VarDefHelper.doc.md) |
| Comprendre comment la liste de modules est filtrée | [`ModuleListProvider.php`](ModuleListProvider.doc.md) |
| Comprendre l'adaptation aux permissions de clés OAuth2 selon l'OS | [`OsHelper.php`](OsHelper.doc.md) |

---

## ⚠️ Zones INCONNU
- `ModuleListProvider` : bug probable ligne 149 — double appel `is_admin(is_admin($current_user))`.
- `VarDefHelper` : appel `load_relationship` sur tous les champs liés — peut être coûteux pour des modules avec de nombreuses relations.
