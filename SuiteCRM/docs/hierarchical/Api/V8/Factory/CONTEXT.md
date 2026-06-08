# 📁 Factory

**Chemin :** `Api/V8/Factory/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les factories de l'API V8. Elles créent dynamiquement les objets nécessaires à la validation des paramètres de route : middleware de validation lié à un objet de paramètres spécifique, et closures de validation Symfony.

## ⚙️ Responsabilité technique
Deux classes factory injectables, enregistrées dans le DI via `factories.php`. `ParamsMiddlewareFactory` implémente un pattern factory+closure pour associer dynamiquement une classe `Param\*` à une route Slim. `ValidatorFactory` crée des closures de validation Symfony réutilisables par les classes `Param\Options\*`.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ParamsMiddlewareFactory.php` | Factory créant des middlewares Slim de validation liés à une classe `Param\*` spécifique | [→ fiche](ParamsMiddlewareFactory.doc.md) |
| `ValidatorFactory.php` | Factory créant des closures de validation Symfony réutilisées par les options de paramètres | [→ fiche](ValidatorFactory.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Psr\Container\ContainerInterface`, `Api\V8\Middleware\ParamsMiddleware`, `Symfony\Component\Validator`
- **Expose :** `ParamsMiddlewareFactory::bind()` consommé dans `Api/V8/Config/routes.php` ; `ValidatorFactory` consommé par toutes les `Param\Options\*`
- **Flux typique :** à la définition des routes, `$paramsMiddlewareFactory->bind(GetModulesParams::class)` retourne une closure → attachée comme middleware à la route Slim → exécutée à chaque requête pour valider les params.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment les middlewares de paramètres sont attachés aux routes | [`ParamsMiddlewareFactory.php`](ParamsMiddlewareFactory.doc.md) |
| Comprendre la validation Symfony des paramètres | [`ValidatorFactory.php`](ValidatorFactory.doc.md) |

---

## ⚠️ Zones INCONNU
- `ParamsMiddlewareFactory` : erreur de configuration d'un `$containerId` invalide produit une exception à l'exécution seulement — pas de vérification au bootstrap.
