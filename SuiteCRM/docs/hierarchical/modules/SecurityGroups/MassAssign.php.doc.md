# 📄 MassAssign.php

**Chemin :** `modules/SecurityGroups/MassAssign.php`
**Type :** PHP — action controller (procédural)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Traitement de la masse-assignation ou du retrait en masse d'un groupe de sécurité sur une sélection d'enregistrements depuis une vue liste. Appelé par le formulaire `MassAssign_SecurityGroups` généré par `AssignGroups::mass_assign()`.

## Rôle technique

Fichier procédural (pas de classe). Identifie les enregistrements cibles (sélection manuelle, page entière, ou liste complète via `export_where`). Itère sur les IDs et ajoute ou retire la relation groupe via `load_relationship` + `add/delete`. Redirige vers la vue liste d'origine.

---

## Dépendances clés

- `modules/SecurityGroups/SecurityGroup.php` — `getLinkName()`
- `include/formbase.php` — utilitaires formulaire
- `BeanFactory::newBean('SecurityGroups')` — chargement du groupe cible
- `$_REQUEST['massassign_group']` — ID du groupe sélectionné
- `$_REQUEST['uid']` / `$_REQUEST['entire']` — liste des enregistrements
- `$_SESSION['export_where']` — filtre de la liste complète
- `$_POST['Delete']` — flag suppression/ajout

---

## Relations clés

- **Appelé par :** `index.php?module=SecurityGroups&action=MassAssign` (formulaire de `AssignGroups`)
- **Appelle :** `SecurityGroup::getLinkName()`, `SugarBean::load_relationship()`, lien `add()`/`delete()`
- **Position dans le flux global :** action de masse sur les groupes de sécurité depuis les vues liste

---

## Notes

- Vérification anti-tamper sur `export_where_md5` pour le mode "toute la liste" (ligne 51-53).
- Les ACL Access sont commentées (lignes 73, 93) — aucune vérification d'autorisation sur l'opération individuelle.
- Redirige vers `return_action` / `return_module` après traitement.
