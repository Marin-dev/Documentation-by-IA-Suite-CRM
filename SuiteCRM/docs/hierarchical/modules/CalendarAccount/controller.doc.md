# 📄 controller.php

**Chemin :** `modules/CalendarAccount/controller.php`
**Type :** PHP — Contrôleur MVC
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Contrôleur du module CalendarAccount. Gère les actions AJAX/HTTP : édition, sauvegarde, récupération de la méthode d'auth d'un fournisseur, test de connexion et déclenchement manuel de synchronisation.

## ⚙️ Rôle technique
Étend `SugarController`. Utilise `CalendarSync::getInstance()` comme façade vers les fournisseurs. Toutes les réponses AJAX sont JSON via `sendJsonResponse()`. La gestion d'exceptions est centralisée dans `handleApiException()` qui mappe les types d'exception vers des codes HTTP et codes d'erreur structurés.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SugarController` — classe parente
  - `CalendarSync` (`include/CalendarSync/CalendarSync.php`) — façade sync
  - `BeanFactory` — chargement beans
  - `SugarApplication` — redirections et messages d'erreur
- **Paramètres d'entrée :** `$_REQUEST['source']`, `$_REQUEST['record']`, `$_REQUEST['oauth_connection_id']`, `$_REQUEST['username/password/server_url/api_key/api_endpoint']`

## 📤 Sorties / Exports
- `CalendarAccountController` — contrôleur
- Actions : `EditView`, `save`, `getProviderAuthMethod`, `testConnection`, `syncCalendarAccount`
- JSON standardisé : `{status, data, message?, error_code?}`

## 🔗 Relations clés
- **Appelé par :** Framework MVC SuiteCRM + appels AJAX frontend
- **Appelle :** `CalendarSync::getProviderAuthMethodWithValidation()`, `CalendarSync::testProviderConnectionWithValidation()`, `CalendarSync::syncAllMeetingsOfCalendarAccount()`
- **Position dans le flux global :** Orchestrateur des opérations de synchronisation calendrier externe

---

## 💡 Points d'attention
- `action_save()` attrape `Throwable` (pas seulement `Exception`) — robustesse maximale.
- `handleApiException()` utilise `match` PHP 8 — incompatible PHP 7.
- `testConnection` détecte les doublons de calendrier externe (`findDuplicateCalendarAccount()`).
- `setupCalendarAccountFromRequest()` ne sauvegarde pas le compte — utilisé uniquement pour le test de connexion.
