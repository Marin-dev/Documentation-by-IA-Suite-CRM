# 📄 view.edit.php (CalendarAccount)

**Chemin :** `modules/CalendarAccount/views/view.edit.php`
**Type :** PHP — Vue (EditView)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Vue d'édition d'un compte calendrier. Affiche le formulaire de création/modification avec les champs d'authentification selon la source sélectionnée (OAuth2, Basic Auth, API Key).

## ⚙️ Rôle technique
Surcharge de `ViewEdit`. Logique exacte INCONNU (non lu). Interagit probablement avec le JS pour afficher dynamiquement les champs selon la méthode d'auth (via `action_getProviderAuthMethod` du contrôleur).

---

## 🔗 Relations clés
- **Appelé par :** `CalendarAccountController::action_EditView()`
