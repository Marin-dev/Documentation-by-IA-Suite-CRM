# 📄 containers.php

**Chemin :** `lib/API/core/containers.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Configure le conteneur d'injection de dépendances (DI) Slim 3 pour l'API REST. Il enregistre les handlers d'erreurs globaux (404, 405, erreurs PHP) qui renvoient des réponses JSON API conformes. Il sert également de base testable, séparé de `app.php` pour faciliter les mocks.

## ⚙️ Rôle technique
Instancie `\Slim\Container`, charge dynamiquement les fichiers de containers du dossier `lib/API/v8/container/*.php` (core + custom). Enregistre quatre handlers Slim : `notAllowedHandler` (405), `notFoundHandler` (404), `errorHandler` (exceptions), `phpErrorHandler` (erreurs PHP). Tous délèguent à `ApiController::generateJsonApiErrorResponse()`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `\Slim\Container` — conteneur PSR-11
  - `SuiteCRM\Utility\Paths` — résolution des chemins lib/custom
  - `SuiteCRM\API\v8\Controller\ApiController` — génération des réponses d'erreur JSON API
  - `SuiteCRM\API\v8\Exception\NotAllowedException` / `NotFoundException` — exceptions métier
  - Fichiers `lib/API/v8/container/*.php` (chargement dynamique)
- **Variables d'environnement utilisées :** aucune directement
- **Arguments / paramètres d'entrée :** aucun (script inclus)

## 📤 Sorties / Exports
- `$container` — instance `\Slim\Container` peuplée, exposée en `$GLOBALS['container']`
- **Consommateurs identifiés :**
  - `lib/API/core/app.php` (inclusion directe)

## 🔗 Relations clés
- **Appelé par :** `lib/API/core/app.php`
- **Appelle :** fichiers `lib/API/v8/container/*.php` (liaison dynamique)
- **Position dans le flux global :** initialisation DI avant le routage Slim

---

## 💡 Points d'attention
- Si `$GLOBALS['container']` est déjà défini (ex: en test), il n'est pas écrasé (ligne 123).
- Les handlers d'erreur capturent toutes les exceptions PHP non interceptées et les sérialisent en JSON API — attention : une erreur fatale PHP dans un container sera transformée en réponse 500 JSON.
- Le chargement dynamique via `glob` implique que l'ordre des containers est celui du système de fichiers (alphabétique).
