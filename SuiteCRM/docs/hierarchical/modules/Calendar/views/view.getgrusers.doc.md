# 📄 view.getgrusers.php

**Chemin :** `modules/Calendar/views/view.getgrusers.php`
**Type :** PHP — Vue / AJAX données utilisateurs GR
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Retourne les données JavaScript GR pour une liste d'utilisateurs, afin de peupler la liste des invités dans le formulaire d'édition d'activité calendrier.

## ⚙️ Rôle technique
Reçoit une liste d'IDs utilisateurs séparés par virgule, charge chaque User bean, et génère du JavaScript assignant un tableau `users_arr` au registre global GR.

---

## 📥 Entrées / Dépendances
- `$_REQUEST['users']` — IDs séparés par virgule
- `BeanFactory::newBean('Users')` — chargement utilisateurs
- `json_config::populateBean()` — sérialisation GR

## 📤 Sorties / Exports
- `CalendarViewGetGRUsers` — JavaScript GR pour les utilisateurs

## 🔗 Relations clés
- **Appelé par :** Interface AJAX du formulaire d'édition d'activité
- **Position dans le flux global :** Peuplement liste invités existants

---

## 💡 Points d'attention
- `array_unique()` déduplique les IDs, mais les IDs vides sont ignorés séparément — robustesse correcte.
