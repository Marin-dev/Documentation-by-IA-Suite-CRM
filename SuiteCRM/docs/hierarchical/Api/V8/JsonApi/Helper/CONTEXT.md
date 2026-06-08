# 📁 Helper

**Chemin :** `Api/V8/JsonApi/Helper/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les helpers de construction des réponses JSON:API. Ils transforment les données brutes des `SugarBean` SuiteCRM en objets conformes à la spec JSON:API : attributs filtrés, liens de relations et méta-données de pagination.

## ⚙️ Responsabilité technique
Trois classes de service injectable (pattern helper), enregistrées dans le conteneur DI via `helpers.php`. Elles construisent des objets de réponse (`AttributeResponse`, `RelationshipResponse`, `MetaResponse`, `PaginationResponse`) consommés par les services de la couche `Service/`.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AttributeObjectHelper.php` | Convertit un `SugarBean` en `AttributeResponse` JSON:API avec filtrage des champs sensibles et normalisation des dates | [→ fiche](AttributeObjectHelper.doc.md) |
| `PaginationObjectHelper.php` | Construit les méta-données et liens de pagination JSON:API à partir de la requête HTTP courante | [→ fiche](PaginationObjectHelper.doc.md) |
| `RelationshipObjectHelper.php` | Construit l'objet `relationships` JSON:API d'un bean en listant toutes ses relations disponibles | [→ fiche](RelationshipObjectHelper.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\V8\BeanDecorator\BeanManager`, `Api\V8\Helper\VarDefHelper`, objets `Response/*`, `Slim\Http\Request`
- **Expose :** `AttributeObjectHelper`, `RelationshipObjectHelper`, `PaginationObjectHelper` — injectés dans les services `ModuleService`, `UserService`, `ListViewService`, `RelationshipService`, `ListViewSearchService`
- **Flux typique :** un service appelle `AttributeObjectHelper::getAttributes($bean, $fields)` → reçoit un `AttributeResponse` → l'injecte dans un `DataResponse` → transmis au contrôleur.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le filtrage des champs dans les réponses JSON:API | [`AttributeObjectHelper.php`](AttributeObjectHelper.doc.md) |
| Comprendre la construction des liens de pagination | [`PaginationObjectHelper.php`](PaginationObjectHelper.doc.md) |
| Comprendre la construction du noeud `relationships` | [`RelationshipObjectHelper.php`](RelationshipObjectHelper.doc.md) |

---

## ⚠️ Zones INCONNU
- `RelationshipObjectHelper` : conflit potentiel si deux relations pointent vers le même module (la clé du tableau est le module, pas la relation). À investiguer.
