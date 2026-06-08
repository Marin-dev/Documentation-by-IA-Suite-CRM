# 📁 Service

**Chemin :** `Api/V8/Service/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient la couche service (logique métier) de l'API V8 SuiteCRM. Les services implémentent toutes les opérations fonctionnelles exposées par l'API : CRUD sur les modules, gestion des relations, authentification/déconnexion, accès à l'utilisateur courant, métadonnées et vues liste.

## ⚙️ Responsabilité technique
Huit classes de service injectable (pattern DI via Slim container), enregistrées dans `services.php`. Chaque service reçoit `BeanManager` et les helpers JSON:API nécessaires. Les services appliquent les contrôles ACL SuiteCRM, construisent les réponses `DocumentResponse`/`DataResponse` et délèguent à `BeanManager` pour l'accès aux beans.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ModuleService.php` | Service CRUD principal : lecture, liste, création, mise à jour, suppression d'enregistrements avec ACL et gestion des uploads | [→ fiche](ModuleService.php.doc.md) |
| `RelationshipService.php` | Gestion des relations inter-beans : lecture, création (auto ou par lien), suppression avec ACL | [→ fiche](RelationshipService.php.doc.md) |
| `UserService.php` | Résolution et retour de l'utilisateur courant à partir du token OAuth2 | [→ fiche](UserService.php.doc.md) |
| `UserPreferencesService.php` | Lecture des préférences utilisateur | [→ fiche](UserPreferencesService.php.doc.md) |
| `MetaService.php` | Exposition des métadonnées : liste modules, vardefs filtrés, schéma Swagger | [→ fiche](MetaService.php.doc.md) |
| `LogoutService.php` | Révocation du token OAuth2 (soft-delete en base) | [→ fiche](LogoutService.php.doc.md) |
| `ListViewService.php` | Lecture de colonnes et lignes de vue liste SuiteCRM | [→ fiche](ListViewService.php.doc.md) |
| `ListViewSearchService.php` | Lecture des définitions de recherche d'une vue liste | [→ fiche](ListViewSearchService.php.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\V8\BeanDecorator\BeanManager`, `Api\V8\JsonApi\Helper\*`, `Api\V8\JsonApi\Response\*`, `Api\V8\Param\*`, classes SuiteCRM natives (`BeanFactory`, `ACLController`, `SugarBean`)
- **Expose :** méthodes de service appelées par les contrôleurs `Api/V8/Controller/`
- **Flux typique :** contrôleur reçoit la requête → transmet les `Params` validés au service correspondant → le service appelle `BeanManager`, applique ACL, construit le `DocumentResponse` → retourné au contrôleur.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre les opérations CRUD sur les modules | [`ModuleService.php`](ModuleService.php.doc.md) |
| Comprendre la gestion des relations entre beans | [`RelationshipService.php`](RelationshipService.php.doc.md) |
| Comprendre l'accès à l'utilisateur courant | [`UserService.php`](UserService.php.doc.md) |
| Comprendre les métadonnées exposées par l'API | [`MetaService.php`](MetaService.php.doc.md) |
| Comprendre la déconnexion OAuth2 | [`LogoutService.php`](LogoutService.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `ModuleService` : dette technique documentée — méthode `getRecords` à découper en classes séparées.
- `ModuleService` : bug potentiel ligne 329 (`$this->doc_url` inexistant).
- `RelationshipService` : `_get_num_rows_in_query` est une API interne non publique de SugarBean.
- `MetaService` : `getSwaggerSchema` retourne un type différent des autres méthodes (pas de `DocumentResponse`).
