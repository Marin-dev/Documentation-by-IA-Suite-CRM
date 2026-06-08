# 📄 MetaController.php

**Chemin :** `Api/V8/Controller/MetaController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrôleur de l'API V8 exposant les métadonnées de l'application SuiteCRM : liste des modules accessibles, liste des champs d'un module, et schéma Swagger de l'API.

## ⚙️ Rôle technique
Hérite de `BaseController`. Délègue entièrement à `MetaService` pour les trois actions. Chaque action suit le patron try/catch et retourne une réponse JSON:API 200 ou 400. Le paramètre `GetFieldListParams` est injecté comme quatrième argument par la `SuiteInvocationStrategy`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Param\GetFieldListParams` — paramètres de la requête getFieldList (module cible)
  - `Api\V8\Service\MetaService` (`Api/V8/Service/MetaService.php`) — service fournissant les métadonnées
  - `Api\V8\Service\UserService` — importé mais non utilisé directement (présent ligne 49, probablement résidu)
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim
- **Garde d'entrée :** vérifie `sugarEntry` (ligne 43-45)

## 📤 Sorties / Exports
- `MetaController` — classe contrôleur
  - `getModuleList(Request, Response, array): Response` — retourne la liste des modules accessibles
  - `getFieldList(Request, Response, array, GetFieldListParams): Response` — retourne les champs d'un module
  - `getSwaggerSchema(Request, Response): Response` — retourne le schéma Swagger de l'API

## 🔗 Relations clés
- **Appelé par :** routeur Slim (INCONNU — routes exactes non visibles dans ce fichier)
- **Appelle :** `MetaService::getModuleList()`, `MetaService::getFieldList()`, `MetaService::getSwaggerSchema()`
- **Position dans le flux global :** endpoints de découverte/introspection de l'API V8

---

## 💡 Points d'attention
- Le champ `$metaService` est typé `UserService` dans le docblock (ligne 62) mais est en réalité de type `MetaService` — incohérence dans le code source.
- `UserService` est importé (ligne 49) mais jamais utilisé dans la classe — import orphelin.
- `getSwaggerSchema` ne prend pas de paramètres spéciaux, suggérant que le schéma est statique ou généré globalement.
