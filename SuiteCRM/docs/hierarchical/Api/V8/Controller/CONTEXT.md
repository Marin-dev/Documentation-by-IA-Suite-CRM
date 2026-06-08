# 📁 Controller

**Chemin :** `Api/V8/Controller/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe tous les contrôleurs de l'API V8 SuiteCRM. Les contrôleurs reçoivent les requêtes HTTP validées, délèguent la logique métier aux services correspondants et retournent des réponses JSON:API formatées. Ils couvrent les modules CRM, les relations, l'utilisateur courant, les préférences, les vues liste et les métadonnées.

## ⚙️ Responsabilité technique
Toutes les classes héritent de `BaseController` qui fournit `generateResponse()` et `generateErrorResponse()`. Chaque contrôleur reçoit un service injecté et expose des actions suivant la convention Slim (`$request, $response, $args, $params`). Les erreurs sont toutes converties en HTTP 400.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `InvocationStrategy/` | Stratégie d'invocation Slim injectant un 4ème argument `params` dans les contrôleurs | [→ CONTEXT](InvocationStrategy/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `BaseController.php` | Classe abstraite de base : sérialisation JSON:API et gestion uniforme des erreurs HTTP | [→ fiche](BaseController.doc.md) |
| `ModuleController.php` | Contrôleur CRUD principal (GET, POST, PATCH, DELETE) sur les modules SuiteCRM | [→ fiche](ModuleController.doc.md) |
| `RelationshipController.php` | Contrôleur des opérations sur les relations inter-beans | [→ fiche](RelationshipController.doc.md) |
| `UserController.php` | Contrôleur de l'utilisateur courant (`GET /V8/current-user`) | [→ fiche](UserController.doc.md) |
| `UserPreferencesController.php` | Contrôleur des préférences utilisateur | [→ fiche](UserPreferencesController.doc.md) |
| `MetaController.php` | Contrôleur des métadonnées API (modules, champs vardefs, swagger) | [→ fiche](MetaController.doc.md) |
| `ListViewController.php` | Contrôleur des colonnes de vues liste | [→ fiche](ListViewController.doc.md) |
| `ListViewSearchController.php` | Contrôleur des définitions de recherche de vues liste | [→ fiche](ListViewSearchController.doc.md) |
| `LogoutController.php` | Contrôleur de déconnexion OAuth2 | [→ fiche](LogoutController.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api/V8/Service/*` (délégation de la logique), `Slim\Http\Request/Response`
- **Expose :** actions HTTP invoquées par le routeur Slim via `Api/V8/Config/routes.php`
- **Flux typique :** requête HTTP → `SuiteInvocationStrategy` → action du contrôleur → service → `DocumentResponse` → `BaseController::generateResponse()` → réponse JSON:API.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le point d'entrée de toutes les réponses JSON:API | [`BaseController.php`](BaseController.doc.md) |
| Trouver les opérations CRUD sur les modules | [`ModuleController.php`](ModuleController.doc.md) |
| Comprendre comment les paramètres arrivent dans les contrôleurs | [`InvocationStrategy/`](InvocationStrategy/CONTEXT.md) |

---

## ⚠️ Zones INCONNU
- `ModuleController` : retourne HTTP 201 pour PATCH (mise à jour) — non conforme REST standard.
- Tous les contrôleurs : toutes les exceptions converties en 400, sans distinction 404/422/500.
