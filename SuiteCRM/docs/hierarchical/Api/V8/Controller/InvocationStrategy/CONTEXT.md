# 📁 InvocationStrategy

**Chemin :** `Api/V8/Controller/InvocationStrategy/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient la stratégie d'invocation personnalisée des contrôleurs de l'API V8 SuiteCRM. Il étend le mécanisme standard de Slim pour permettre l'injection d'un quatrième argument (`params`) issu du middleware de validation des paramètres de route.

## ⚙️ Responsabilité technique
Implémente `Slim\Interfaces\InvocationStrategyInterface` en surchargeant la façon dont Slim appelle les actions de contrôleurs. Injecte les paramètres de route comme attributs PSR-7 et ajoute un quatrième paramètre `$params` (alimenté par `ParamsMiddleware`) aux callables invoqués.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SuiteInvocationStrategy.php` | Stratégie d'invocation Slim injectant un quatrième argument `params` dans les actions des contrôleurs | [→ fiche](SuiteInvocationStrategy.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ParamsMiddleware` (fournit les `params` via attributs PSR-7), `Slim\Interfaces\InvocationStrategyInterface`
- **Expose :** `SuiteInvocationStrategy` — enregistrée comme `foundHandler` dans `Api/V8/Config/services.php`
- **Flux typique :** Slim reçoit une requête → `SuiteInvocationStrategy::__invoke()` est appelé → injecte les paramètres de route puis appelle le contrôleur avec `($request, $response, $routeArgs, $params)`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment les contrôleurs reçoivent leurs paramètres | [`SuiteInvocationStrategy.php`](SuiteInvocationStrategy.doc.md) |
| Modifier la signature des actions de contrôleur | [`SuiteInvocationStrategy.php`](SuiteInvocationStrategy.doc.md) |

---

## ⚠️ Zones INCONNU
- Compatibilité PHP 5.5.9 mentionnée dans le code (probablement obsolète) — à vérifier si la contrainte est toujours active.
