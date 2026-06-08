# 📄 view.createinvitee.php

**Chemin :** `modules/Calendar/views/view.createinvitee.php`
**Type :** PHP — Vue / Création invité AJAX
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Crée un nouveau Contact ou Lead depuis le calendrier (formulaire d'ajout d'invité) et retourne ses données en JSON pour l'ajouter immédiatement à la liste des invités.

## ⚙️ Rôle technique
Vérifie que le module est bien `Leads` ou `Contacts`, vérifie l'accès Save via ACL, populate le bean depuis le POST et le sauvegarde. Retourne les champs demandés via `$_REQUEST['fieldList']`.

---

## 📥 Entrées / Dépendances
- `SugarView` — classe parente
- `$_REQUEST['inviteeModule']` — `Leads` ou `Contacts`
- `$_REQUEST['fieldList']` — champs à retourner
- `include/formbase.php` — `populateFromPost()`
- `BeanFactory` / `$beanList` / `$beanFiles` — chargement bean

## 📤 Sorties / Exports
- `CalendarViewCreateInvitee` — vue création invité
- JSON : `{module, fields: {field: value, ...}}`

## 🔗 Relations clés
- **Appelé par :** Interface AJAX du formulaire d'édition d'activité
- **Position dans le flux global :** Création rapide d'un Contact/Lead depuis le calendrier

---

## 💡 Points d'attention
- Seuls `Leads` et `Contacts` sont autorisés — validation stricte ligne 53.
- En cas d'échec ACL, retourne `{noAccess: true}` et stoppe l'exécution.
