# 📄 BaseController.php

**Chemin :** `Api/V8/Controller/BaseController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Classe abstraite servant de base commune à tous les contrôleurs de l'API V8 de SuiteCRM. Elle centralise la logique de sérialisation des réponses JSON:API et la gestion uniforme des erreurs HTTP.

## ⚙️ Rôle technique
Fournit deux méthodes protégées (`generateResponse` et `generateErrorResponse`) utilisées par chaque contrôleur enfant pour construire les réponses HTTP. Impose le Content-Type `application/vnd.api+json` et encode le corps en JSON avec les options `JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\JsonApi\Response\ErrorResponse` (`Api/V8/JsonApi/Response/ErrorResponse.php`) — objet de réponse d'erreur JSON:API
  - `Slim\Http\Response` — objet réponse HTTP de Slim

## 📤 Sorties / Exports
- `BaseController` — classe abstraite — classe parente de tous les contrôleurs V8
  - `generateResponse(HttpResponse, mixed, int): HttpResponse` — construit une réponse HTTP avec corps JSON et statut
  - `generateErrorResponse(HttpResponse, \Exception, int): HttpResponse` — construit une réponse d'erreur JSON:API
  - `MEDIA_TYPE` — constante — valeur `application/vnd.api+json`
- **Consommateurs identifiés dans le repo :**
  - `Api/V8/Controller/ListViewController.php`
  - `Api/V8/Controller/ListViewSearchController.php`
  - `Api/V8/Controller/LogoutController.php`
  - `Api/V8/Controller/MetaController.php`
  - `Api/V8/Controller/ModuleController.php`
  - `Api/V8/Controller/RelationshipController.php`
  - `Api/V8/Controller/UserController.php`
  - `Api/V8/Controller/UserPreferencesController.php`

## 🔗 Relations clés
- **Appelé par :** tous les contrôleurs `Api/V8/Controller/*.php` via héritage
- **Appelle :** `ErrorResponse` (instanciation directe dans `generateErrorResponse`)
- **Position dans le flux global :** socle de la couche contrôleur de l'API V8 ; toutes les réponses sortantes passent par ses méthodes

---

## 💡 Points d'attention
- La constante `MEDIA_TYPE` est définie `public` et peut être surchargée par les enfants via `static::MEDIA_TYPE` (late static binding).
- L'attribut `#[\AllowDynamicProperties]` est présent pour compatibilité PHP 8.2+, ce qui suggère que des propriétés dynamiques peuvent être ajoutées dans des sous-classes.
- La classe est `abstract` : elle ne peut pas être instanciée directement.
