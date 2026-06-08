# 📁 Middleware

**Chemin :** `Api/V8/Middleware/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les middlewares de l'API V8. Le middleware central résout l'utilisateur courant à partir du token OAuth2 et valide/hydrate les paramètres de la requête avant l'exécution du contrôleur.

## ⚙️ Responsabilité technique
Classe Slim middleware invocable (`__invoke`) instanciée par `ParamsMiddlewareFactory`. Positionne `$GLOBALS['current_user']` (effet de bord global) et l'objet `params` comme attribut PSR-7 de la requête. Lié aux routes via `ParamsMiddlewareFactory::bind()` dans `routes.php`.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ParamsMiddleware.php` | Middleware résolvant l'utilisateur courant OAuth2 et validant/hydratant les paramètres de route | [→ fiche](ParamsMiddleware.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\V8\BeanDecorator\BeanManager`, `Api\V8\Param\BaseParam`, `oauth_access_token_id` (attribut PSR-7 positionné par `league/oauth2-server`)
- **Expose :** attribut `params` (objet `BaseParam` hydraté) sur la requête PSR-7 — consommé par `SuiteInvocationStrategy` comme 4ème argument des contrôleurs
- **Flux typique :** requête → `ResourceServerMiddleware` (OAuth2) → `ParamsMiddleware` (résolution user + validation params) → `SuiteInvocationStrategy` → action du contrôleur.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment l'utilisateur courant est résolu | [`ParamsMiddleware.php`](ParamsMiddleware.doc.md) |
| Comprendre comment les paramètres sont fusionnés et validés | [`ParamsMiddleware.php`](ParamsMiddleware.doc.md) |

---

## ⚠️ Zones INCONNU
- Les paramètres de body peuvent écraser les paramètres de route du même nom — risque de sécurité potentiel.
- Les erreurs sont loguées en niveau `fatal` avec traces complètes — informations potentiellement sensibles dans les logs.
