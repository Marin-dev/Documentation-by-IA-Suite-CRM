# 📄 SaveSecurityGroupUserRelationship.php

**Chemin :** `modules/SecurityGroups/SaveSecurityGroupUserRelationship.php`
**Type :** PHP — action controller (procédural)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Traite la sauvegarde des propriétés d'une relation groupe-utilisateur : flag `noninheritable` (héritage bloqué) et `primary_group` (groupe principal). Un non-admin ne peut modifier que sa propre relation.

## Rôle technique

Fichier procédural. Charge la relation via `SecurityGroupUserRelationship`, mappe les champs du POST, vérifie les droits, et sauvegarde. En cas de `primary_group=1`, remet à 0 tous les autres groupes primaires de l'utilisateur via une requête SQL directe.

---

## Dépendances clés

- `modules/SecurityGroups/SecurityGroupUserRelationship.php`
- `include/utils.php` — `safe_map()`
- `DBManagerFactory` — requête SQL de dé-primarisation
- `$_REQUEST['record']`, `noninheritable`, `primary_group`

---

## Relations clés

- **Appelé par :** formulaire d'édition de la relation groupe-utilisateur (sous-panneau)
- **Position dans le flux global :** modification des propriétés d'appartenance à un groupe

---

## Notes

- La vérification d'accès non-admin est incomplète : elle compare `securitygroup_id` et `user_id` du POST aux valeurs DB — risque de manipulation si `safe_map` ne filtre pas correctement.
