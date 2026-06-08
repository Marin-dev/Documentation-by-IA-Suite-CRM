# 📄 Save.php

**Chemin :** `modules/ACLRoles/Save.php`
**Type :** PHP — action controller (procédural)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Traite la sauvegarde d'un rôle ACL : création/modification du rôle avec son nom et sa description, gestion de la duplication (copie des actions), ou mise à jour AJAX des niveaux d'accès des actions individuelles.

## Rôle technique

Fichier procédural. Deux chemins : (1) si `$_REQUEST['name']` présent → sauvegarde le rôle et optionnellement duplique les actions d'un autre rôle ; (2) sinon → traitement AJAX des actions via `act_guid_*` POST parameters, retourne JSON minimal.

---

## Dépendances clés

- `BeanFactory::newBean('ACLRoles')` — instanciation du rôle
- `ACLRole::getRoleActions()` — duplication d'actions
- `ACLRole::setAction()` — mise à jour des niveaux d'accès
- `$_POST['act_guid_{action_id}']` — valeur d'accès par action (AJAX)

---

## Relations clés

- **Appelé par :** formulaires `EditView` et `EditRole` du module ACLRoles, appels AJAX de la matrice de rôles
- **Position dans le flux global :** persistance des permissions de rôles ACL

---

## Notes

- Le mode AJAX retourne `result = {role_id:'...', module:'All'}` et appelle `sugar_cleanup(true)`.
- La duplication copie toutes les actions d'un rôle existant.
