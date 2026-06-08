# 📄 Delete.php

**Chemin :** `modules/ACLRoles/Delete.php`
**Type :** PHP — action controller (procédural)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Supprime un rôle ACL par soft delete et redirige vers la liste des rôles.

## Rôle technique

Fichier procédural court. Récupère le rôle via `BeanFactory`, appelle `mark_deleted()` (qui supprime aussi les `acl_roles_actions`), puis redirige.

---

## Notes

- `mark_relationships_deleted()` est appelé automatiquement par `SugarBean::mark_deleted()`, ce qui nettoie les actions du rôle.
