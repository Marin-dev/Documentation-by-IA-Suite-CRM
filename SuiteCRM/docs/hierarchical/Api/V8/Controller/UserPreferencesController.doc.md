# 📄 UserPreferencesController.php

**Chemin :** `Api/V8/Controller/UserPreferencesController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrôleur de l'API V8 permettant de récupérer les préférences d'un utilisateur SuiteCRM (langue, fuseau horaire, format de dates, etc.).

## ⚙️ Rôle technique
Hérite de `BaseController`. Expose une seule action `getUserPreferences` qui délègue à `UserPreferencesService::getUserPreferences()`. L'objet `GetUserPreferencesParams` est injecté comme quatrième argument. Retourne une réponse JSON:API 200 ou 400.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Param\GetUserPreferencesParams` — paramètres de la requête (identifiant utilisateur ou préférence ciblée)
  - `Api\V8\Service\UserPreferencesService` (`Api/V8/Service/UserPreferencesService.php`) — service des préférences utilisateur
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim
- **Garde d'entrée :** vérifie `sugarEntry` (ligne 43-45)

## 📤 Sorties / Exports
- `UserPreferencesController` — classe contrôleur
  - `getUserPreferences(Request, Response, array, GetUserPreferencesParams): Response` — retourne les préférences utilisateur (JSON:API, HTTP 200)

## 🔗 Relations clés
- **Appelé par :** routeur Slim (INCONNU — route exacte non visible dans ce fichier)
- **Appelle :** `UserPreferencesService::getUserPreferences($params)`
- **Position dans le flux global :** endpoint de lecture des préférences utilisateur dans l'API V8

---

## 💡 Points d'attention
- Contrairement à `UserController`, ce contrôleur utilise un objet `Params` typé (quatrième argument), ce qui indique que l'endpoint accepte des paramètres de requête spécifiques (INCONNU — contenu exact de `GetUserPreferencesParams` non analysé ici).
