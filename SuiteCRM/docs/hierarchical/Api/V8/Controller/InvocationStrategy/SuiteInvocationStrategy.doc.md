# 📄 SuiteInvocationStrategy.php

**Chemin :** `Api/V8/Controller/InvocationStrategy/SuiteInvocationStrategy.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Stratégie d'invocation personnalisée pour le framework Slim utilisée par l'API V8 de SuiteCRM. Elle permet de transmettre un quatrième argument (`params`) aux actions des contrôleurs, en plus des trois arguments standards de Slim (request, response, routeArguments).

## ⚙️ Rôle technique
Implémente `Slim\Interfaces\InvocationStrategyInterface`. Lors de l'appel d'une action, elle injecte chaque argument de route comme attribut de la requête PSR-7, puis appelle le callable avec quatre paramètres : `$request`, `$response`, `$routeArguments`, et `$request->getAttribute('params')`. Ce quatrième paramètre est alimenté par le `ParamsMiddleware`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Psr\Http\Message\ResponseInterface` — interface réponse PSR-7
  - `Psr\Http\Message\ServerRequestInterface` — interface requête PSR-7
  - `Slim\Interfaces\InvocationStrategyInterface` — interface Slim pour stratégies d'invocation

## 📤 Sorties / Exports
- `SuiteInvocationStrategy` — classe — stratégie d'invocation de contrôleurs
  - `__invoke(callable, ServerRequestInterface, ResponseInterface, array): ResponseInterface` — exécute l'action du contrôleur avec injection des paramètres
- **Consommateurs identifiés dans le repo :**
  - `Api/V8/Config/services.php`

## 🔗 Relations clés
- **Appelé par :** le routeur Slim (`Api/V8/Config/services.php` enregistre cette stratégie)
- **Appelle :** les actions de contrôleurs (`ListViewController`, `ModuleController`, etc.)
- **Position dans le flux global :** intermédiaire entre le routeur Slim et les méthodes des contrôleurs ; injecte le quatrième argument `params`

---

## 💡 Points d'attention
- Le commentaire ligne 24 signale explicitement la non-utilisation de l'opérateur splat (`...`) pour maintenir la compatibilité PHP 5.5.9, bien que cette contrainte soit probablement obsolète dans les versions récentes de SuiteCRM.
- Si `params` n'est pas défini dans la requête (attribut absent), `null` est passé comme quatrième argument ; les contrôleurs doivent gérer ce cas si le paramètre est typé.
