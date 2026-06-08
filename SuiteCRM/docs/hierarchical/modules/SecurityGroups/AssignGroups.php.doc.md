# 📄 AssignGroups.php

**Chemin :** `modules/SecurityGroups/AssignGroups.php`
**Type :** PHP — logic hook handler
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Handler de logic hooks pour le module SecurityGroups. Gère (1) l'assignation de groupes via popup lors de la création d'un enregistrement (`popup_select`), (2) le déclenchement automatique du popup de sélection de groupe après sauvegarde (`popup_onload`), et (3) l'affichage du formulaire de masse-assignation de groupes dans les vues liste (`mass_assign`).

## Rôle technique

Classe `AssignGroups` non héritante. Chaque méthode est conçue pour être appelée comme callback de logic hook. `mass_assign` génère dynamiquement un formulaire HTML+JavaScript inline pour les vues liste.

---

## Dépendances clés

- `modules/SecurityGroups/SecurityGroup.php` — `getSecurityModules()`, `getLinkName()`
- `$sugar_config['securitysuite_popup_select']` — activation du popup de sélection
- `$sugar_config['securitysuite_user_popup']` — popup pour la création d'utilisateurs
- `ACLAction::getUserAccessLevel()` — vérification d'accès pour la masse-assignation
- `$_REQUEST['securitygroup_list']` — liste des groupes sélectionnés dans le popup
- `$_SESSION['securitygroups_popup']` — état du popup en session

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AssignGroups` | classe | Handler de logic hooks SecurityGroups |
| `popup_select()` | méthode | Assigne le(s) groupe(s) sélectionnés dans le popup au nouvel enregistrement |
| `popup_onload()` | méthode | Déclenche le popup JS de sélection de groupe après chargement de page |
| `mass_assign()` | méthode | Injecte le formulaire HTML de masse-assignation dans la vue liste |

---

## Relations clés

- **Appelé par :** framework logic hooks SugarCRM (`after_save`, `after_render`)
- **Appelle :** `SecurityGroup::getSecurityModules()`, `SecurityGroup::getLinkName()`, `ACLAction::getUserAccessLevel()`
- **Position dans le flux global :** s'intercale après la sauvegarde d'un bean pour demander à l'utilisateur à quel groupe rattacher le nouvel enregistrement

---

## Notes

- `popup_select()` ignore les modules `Users` et `SugarFeed` (ligne 17).
- `mass_assign()` exclut les modules `Emails` et `ACLRoles` de la masse-assignation (ligne 149).
- Le formulaire `MassAssign_SecurityGroups` soumet à `index.php?module=SecurityGroups&action=MassAssign`.
- En cas de doublon détecté (`dup_checked`), un message d'erreur est stocké en session (`$_SESSION['securitysuite_error']`) et affiché au prochain chargement.
