# 📄 UserController.php

**Chemin :** `Api/V8/Controller/UserController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrôleur de l'API V8 permettant à un utilisateur authentifié de récupérer les informations de son propre compte (profil de l'utilisateur courant).

## ⚙️ Rôle technique
Hérite de `BaseController`. Expose une seule action `getCurrentUser` qui délègue à `UserService::getCurrentUser()` en lui passant la requête HTTP. Retourne une réponse JSON:API 200 ou 400.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Service\UserService` (`Api/V8/Service/UserService.php`) — service de données utilisateur
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim
- **Garde d'entrée :** vérifie `sugarEntry` (ligne 43-45)

## 📤 Sorties / Exports
- `UserController` — classe contrôleur
  - `getCurrentUser(Request, Response, array): Response` — retourne le profil de l'utilisateur courant (JSON:API, HTTP 200)

## 🔗 Relations clés
- **Appelé par :** routeur Slim (INCONNU — route exacte non visible dans ce fichier)
- **Appelle :** `UserService::getCurrentUser($request)`
- **Position dans le flux global :** endpoint de profil personnel de l'API V8 ; l'utilisateur courant est résolu par le `ParamsMiddleware` via le token OAuth2

---

## 💡 Points d'attention
- Le service reçoit l'objet `$request` complet ; l'identification de l'utilisateur courant est probablement résolue via `$GLOBALS['current_user']` positionné par le `ParamsMiddleware`.
- Pas de paramètre de type `BaseParam` injecté (pas de quatrième argument) — action sans paramètres supplémentaires.
