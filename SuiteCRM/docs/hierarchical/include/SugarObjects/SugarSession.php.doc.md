# 📄 SugarSession.php

**Chemin :** `include/SugarObjects/SugarSession.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Gestionnaire de session applicative SuiteCRM. Encapsule la gestion du cycle de vie de la session PHP (démarrage, ID de session) avec la logique spécifique à l'application (compatibilité `session.auto_start`).

## ⚙️ Rôle technique
Singleton via `$_instance` statique. La méthode `start()` vérifie si une session est déjà active (compatibilité avec `session.auto_start = 1`) avant d'appeler `session_start()`. `setSessionId()` permet de forcer un ID de session. Expose `$sessionId` statique.

---

## 📥 Entrées / Dépendances
- **Imports principaux :** aucun
- **Fonctions PHP utilisées :** `session_id()`, `session_start()`

## 📤 Sorties / Exports
- `SugarSession` — classe (singleton/session)
  - `start()` — démarrage sécurisé de la session
  - `setSessionId($sessionId)` — forçage de l'ID de session
  - `$sessionId` — ID de session courant (statique)

## 🔗 Relations clés
- **Appelé par :** bootstrap de l'application (`index.php`, `entry_point_registry`)
- **Appelle :** fonctions PHP natives de session
- **Position dans le flux global :** première étape du bootstrap, avant l'authentification

---

## 💡 Points d'attention
- La gestion de `session.auto_start = 1` (commentaire ligne 55) est importante pour les environnements PHP partagés où la session démarre automatiquement.
- Singleton — une seule instance de session par requête.
