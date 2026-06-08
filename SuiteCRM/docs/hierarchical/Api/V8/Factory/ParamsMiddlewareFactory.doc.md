# 📄 ParamsMiddlewareFactory.php

**Chemin :** `Api/V8/Factory/ParamsMiddlewareFactory.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Factory permettant de créer à la volée des instances de `ParamsMiddleware` liées à un objet `Params` spécifique (identifié par un ID de container). Utilisée dans la configuration des routes pour associer dynamiquement le bon objet de paramètres à chaque route.

## ⚙️ Rôle technique
Reçoit le container d'injection de dépendances (PSR-11) à la construction. La méthode `bind($containerId)` retourne une closure Slim-compatible (`Request, Response, callable $next`) qui, à l'exécution, résout l'objet `BaseParam` et le `BeanManager` depuis le container, instancie un `ParamsMiddleware`, et l'invoque. Pattern Factory + Closure pour un middleware contextuel.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Middleware\ParamsMiddleware` — middleware instancié par la factory
  - `Psr\Container\ContainerInterface` — container DI PSR-11
  - `Api\V8\BeanDecorator\BeanManager` — gestionnaire de beans SuiteCRM
  - `Slim\Http\Request` / `Slim\Http\Response` — utilisés dans la closure retournée

## 📤 Sorties / Exports
- `ParamsMiddlewareFactory` — classe factory
  - `bind(string $containerId): callable` — retourne une closure middleware Slim liant un `BaseParam` spécifique
- **Consommateurs identifiés dans le repo :**
  - `Api/V8/Config/services/factories.php`
  - `Api/V8/Config/routes.php`

## 🔗 Relations clés
- **Appelé par :** `Api/V8/Config/routes.php` (ajout de middleware sur les routes), `Api/V8/Config/services/factories.php`
- **Appelle :** `ParamsMiddleware` (instanciation), `Container::get()`
- **Position dans le flux global :** couche de configuration — lie les routes aux objets de paramètres corrects avant l'exécution des contrôleurs

---

## 💡 Points d'attention
- La factory crée une nouvelle instance de `ParamsMiddleware` à chaque invocation de la closure (pas de singleton par route) — comportement normal pour un middleware par requête.
- `#[\AllowDynamicProperties]` présent pour compatibilité PHP 8.2+.
- Le `$containerId` doit correspondre à un service enregistré dans le container retournant un objet `BaseParam` ; une erreur de configuration produit une exception à l'exécution, pas à la compilation.
