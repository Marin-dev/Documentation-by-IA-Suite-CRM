# 📁 JsonApi

**Chemin :** `Api/V8/JsonApi/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe toute la couche de sérialisation JSON:API de l'API V8. Il couvre la construction des objets de réponse (DTOs), les helpers de transformation bean → JSON:API, et les services de traduction des paramètres de requête (filtres, tri) en SQL.

## ⚙️ Responsabilité technique
Organisé en trois sous-dossiers : `Helper/` (services de construction des noeuds JSON:API), `Repository/` (translation paramètres → SQL), et `Response/` (DTOs `JsonSerializable`). Ces composants forment la couche de sérialisation utilisée par tous les services de `Api/V8/Service/`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Helper/` | Helpers de construction des noeuds `attributes`, `relationships` et liens de pagination JSON:API | [→ CONTEXT](Helper/CONTEXT.md) |
| `Repository/` | Services de traduction filtres/tri JSON:API en clauses SQL WHERE/ORDER BY | [→ CONTEXT](Repository/CONTEXT.md) |
| `Response/` | DTOs `JsonSerializable` représentant la structure complète d'une réponse JSON:API | [→ CONTEXT](Response/CONTEXT.md) |

### Fichiers documentés
Aucun fichier direct dans ce dossier (tout est dans les sous-dossiers).

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\V8\BeanDecorator\BeanManager`, `SugarBean`, `DBManager`, `Slim\Http\Request`, `Api\Core\Config\ApiConfig`
- **Expose :** objets de réponse et helpers consommés par `Api/V8/Service/*` ; services de filtrage consommés par `Api/V8/Param/Options/*`
- **Flux typique :** service → `AttributeObjectHelper::getAttributes($bean)` → `AttributeResponse` injecté dans `DataResponse` → injecté dans `DocumentResponse` → sérialisé par `BaseController::generateResponse()`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la structure complète des réponses JSON:API | [`Response/`](Response/CONTEXT.md) |
| Comprendre la construction des attributs/relations d'un bean | [`Helper/`](Helper/CONTEXT.md) |
| Comprendre la traduction des filtres en SQL | [`Repository/`](Repository/CONTEXT.md) |

---

## ⚠️ Zones INCONNU
- INCONNU remontés depuis les sous-dossiers : conflit potentiel dans `RelationshipObjectHelper` (clé tableau = module), comportement des clés null dans `PaginationResponse`.
