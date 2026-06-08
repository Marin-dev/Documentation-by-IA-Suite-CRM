# 📁 V8

**Chemin :** `Api/V8/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient l'implémentation complète de l'API REST V8 de SuiteCRM. Il couvre toutes les opérations CRUD sur les modules CRM, la gestion des relations inter-beans, l'authentification OAuth2, les métadonnées de l'API et les vues liste. C'est le coeur fonctionnel de l'API publique de SuiteCRM.

## ⚙️ Responsabilité technique
Architecture MVC avec couches clairement séparées : `Controller/` (HTTP), `Service/` (métier), `BeanDecorator/` (accès données), `JsonApi/` (sérialisation), `OAuth2/` (authentification), `Config/` (DI + routes), `Param/` (validation), `Factory/` et `Middleware/` (infrastructure Slim). Toutes les dépendances sont injectées via le conteneur Slim. Les réponses respectent la spec JSON:API.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Config/` | Configuration DI (9 fichiers partiels) et déclaration de toutes les routes HTTP de l'API | [→ CONTEXT](Config/CONTEXT.md) |
| `Controller/` | Contrôleurs HTTP héritant de `BaseController`, délèguent aux services | [→ CONTEXT](Controller/CONTEXT.md) |
| `Service/` | 8 services métier : CRUD modules, relations, utilisateur, métadonnées, déconnexion, vues liste | [→ CONTEXT](Service/CONTEXT.md) |
| `BeanDecorator/` | Couche d'abstraction sur `BeanFactory` SuiteCRM : `BeanManager`, fluent builder de listes | [→ CONTEXT](BeanDecorator/CONTEXT.md) |
| `JsonApi/` | Sérialisation JSON:API : DTOs réponse, helpers de construction, translation filtres/tri → SQL | [→ CONTEXT](JsonApi/CONTEXT.md) |
| `OAuth2/` | Implémentation OAuth2 : entités et repositories pour `league/oauth2-server` | [→ CONTEXT](OAuth2/CONTEXT.md) |
| `Param/` | Validation et normalisation des paramètres de requête via `OptionsResolver` Symfony | [→ CONTEXT](Param/CONTEXT.md) |
| `Factory/` | Factories `ParamsMiddlewareFactory` et `ValidatorFactory` | [→ CONTEXT](Factory/CONTEXT.md) |
| `Helper/` | Utilitaires transversaux : VarDefs, liste modules ACL, détection OS | [→ CONTEXT](Helper/CONTEXT.md) |
| `Middleware/` | `ParamsMiddleware` : résolution utilisateur OAuth2 + validation params avant contrôleur | [→ CONTEXT](Middleware/CONTEXT.md) |

### Fichiers documentés
Aucun fichier direct dans ce dossier.

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api/Core/` (bootstrap, loaders), `league/oauth2-server`, `Symfony/Validator`, `Symfony/OptionsResolver`, classes globales SuiteCRM (`BeanFactory`, `SugarBean`, `DBManager`, `ACLController`)
- **Expose :** endpoints REST JSON:API sur `/V8/*` (protégés OAuth2) et `/access_token` (émission de tokens)
- **Flux typique :** HTTP POST `/access_token` → OAuth2 grant → JWT ; HTTP GET `/V8/module/{module}/{id}` → `ResourceServerMiddleware` → `ParamsMiddleware` → `ModuleController::getModuleRecord()` → `ModuleService::getRecord()` → `BeanManager` → `DocumentResponse` JSON:API.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Trouver tous les endpoints de l'API | [`Config/routes.php`](Config/routes.php.doc.md) |
| Comprendre les opérations CRUD sur un module | [`Service/ModuleService.php`](Service/ModuleService.php.doc.md) |
| Comprendre le flux d'authentification OAuth2 | [`OAuth2/`](OAuth2/CONTEXT.md) |
| Comprendre la structure des réponses JSON:API | [`JsonApi/Response/`](JsonApi/Response/CONTEXT.md) |
| Comprendre la validation des paramètres de requête | [`Param/`](Param/CONTEXT.md) |

---

## ⚠️ Zones INCONNU
- `ModuleService` : dette technique documentée (méthode `getRecords` à refactoriser).
- `ScopeRepository` : scopes OAuth2 non implémentés.
- Tous les contrôleurs : toutes les exceptions converties en HTTP 400 sans distinction.
- Point d'entrée HTTP (`index.php` ou `entryPoint.php` de l'API) non documenté — INCONNU.
