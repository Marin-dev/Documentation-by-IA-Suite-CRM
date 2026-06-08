# 📄 view.getgr.php

**Chemin :** `modules/Calendar/views/view.getgr.php`
**Type :** PHP — Vue / AJAX données GR
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Retourne les données JavaScript "Group Relations" (GR) pour un bean spécifique, utilisées par le formulaire d'édition du calendrier pour préremplir les champs relations.

## ⚙️ Rôle technique
Appelle `json_config::getFocusData($type, $record)` et retourne le JavaScript résultant directement (pas de JSON).

---

## 📥 Entrées / Dépendances
- `$_REQUEST['type']` — module du bean
- `$_REQUEST['record']` — ID du bean
- `json_config` (`include/json_config.php`)

## 📤 Sorties / Exports
- `CalendarViewGetGR` — sortie JavaScript GR brut

## 🔗 Relations clés
- **Appelé par :** Interface AJAX du formulaire édition calendrier
- **Position dans le flux global :** Chargement des données de relations pour un enregistrement existant

---

## 💡 Points d'attention
- Suppression temporaire du rapport d'erreurs (`error_reporting(0)`) avant `require_once('include/json_config.php')` — potentiel masquage d'erreurs.
