# 📁 Response

**Chemin :** `Api/V8/JsonApi/Response/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe tous les objets de valeur (DTOs) représentant la structure d'une réponse JSON:API. Il couvre les noeuds `data`, `attributes`, `relationships`, `links`, `meta`, `errors` et la pagination. Ces objets forment le vocabulaire de construction des réponses de l'API V8.

## ⚙️ Responsabilité technique
Classes PHP implémentant `\JsonSerializable`, organisées en hiérarchie : `MetaResponse` est la classe de base pour les conteneurs de propriétés dynamiques, dont héritent `AttributeResponse` et `RelationshipResponse`. `LinksResponse` est la base de `PaginationResponse`. Toutes les classes filtrent les valeurs nulles lors de la sérialisation (sauf `PaginationResponse`).

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AttributeResponse.php` | Noeud `attributes` JSON:API — étend `MetaResponse` avec validation des clés interdites | [→ fiche](AttributeResponse.doc.md) |
| `DataResponse.php` | Ressource individuelle JSON:API (`type`, `id`, `attributes`, `relationships`, `links`) | [→ fiche](DataResponse.doc.md) |
| `DocumentResponse.php` | Document racine JSON:API (`data`, `meta`, `links`) avec message automatique si vide | [→ fiche](DocumentResponse.doc.md) |
| `ErrorResponse.php` | Réponse d'erreur JSON:API avec support du mode debug (trace d'exception) | [→ fiche](ErrorResponse.doc.md) |
| `LinksResponse.php` | Noeud `links` JSON:API (`self`, `related`) — classe parente de `PaginationResponse` | [→ fiche](LinksResponse.doc.md) |
| `MetaResponse.php` | Conteneur de propriétés dynamiques sérialisable — base de `AttributeResponse` et `RelationshipResponse` | [→ fiche](MetaResponse.doc.md) |
| `PaginationResponse.php` | Liens de navigation de pagination (`first`, `prev`, `next`, `last`) — étend `LinksResponse` | [→ fiche](PaginationResponse.doc.md) |
| `RelationshipResponse.php` | Noeud `relationships` JSON:API — étend `MetaResponse` pour le typage sémantique | [→ fiche](RelationshipResponse.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\Core\Config\ApiConfig` (pour `ErrorResponse`), classes PHP natives (`JsonSerializable`)
- **Expose :** objets de valeur instanciés par les services (`ModuleService`, `UserService`, etc.) et les helpers (`AttributeObjectHelper`, `PaginationObjectHelper`, `RelationshipObjectHelper`)
- **Flux typique :** un service construit `DocumentResponse` → y attache un ou plusieurs `DataResponse` (chacun avec `AttributeResponse` et `RelationshipResponse`) → `DocumentResponse::jsonSerialize()` produit le JSON final retourné par le contrôleur.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la structure d'une réponse JSON:API complète | [`DocumentResponse.php`](DocumentResponse.doc.md) |
| Comprendre la structure d'une ressource individuelle | [`DataResponse.php`](DataResponse.doc.md) |
| Modifier le format des erreurs API | [`ErrorResponse.php`](ErrorResponse.doc.md) |
| Comprendre la structure de pagination | [`PaginationResponse.php`](PaginationResponse.doc.md) |
| Comprendre la base des conteneurs dynamiques | [`MetaResponse.php`](MetaResponse.doc.md) |

---

## ⚠️ Zones INCONNU
- `ErrorResponse` : instanciateurs non identifiés via grep dans `Api/` — probablement appelé dans des middlewares d'erreur non documentés.
- `PaginationResponse` : retourne les 4 clés même nulles (contrairement à `LinksResponse`) — comportement asymétrique à vérifier côté clients.
- `ErrorResponse` : TODO mentionné dans le code concernant la documentation du mode debug.
