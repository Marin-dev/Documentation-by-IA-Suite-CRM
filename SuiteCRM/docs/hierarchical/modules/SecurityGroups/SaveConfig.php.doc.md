# ⚙️ SaveConfig.php (configuration)

**Chemin :** `modules/SecurityGroups/SaveConfig.php`
**Configure :** Paramètres SecuritySuite dans `config.php` de SuiteCRM
**Dernière mise à jour doc :** 2026-06-02

---

## Ce que ce fichier configure

Fichier procédural gérant la sauvegarde des options de configuration SecuritySuite depuis le panneau d'administration. Peut aussi ajouter/supprimer des groupes par défaut.

## Paramètres clés sauvegardés

| Paramètre | Effet |
|---|---|
| `securitysuite_additive` | Mode additif : accès le plus permissif gagne |
| `securitysuite_strict_rights` | Droits stricts : vérification rôle du groupe |
| `securitysuite_filter_user_list` | Filtre la liste d'utilisateurs par groupe |
| `securitysuite_user_role_precedence` | Rôle utilisateur prime sur rôle de groupe |
| `securitysuite_user_popup` | Popup de sélection de groupe à la création utilisateur |
| `securitysuite_popup_select` | Popup de sélection de groupe à la création d'enregistrement |
| `securitysuite_inherit_creator` | Hérite les groupes du créateur |
| `securitysuite_inherit_parent` | Hérite les groupes du parent |
| `securitysuite_inherit_assigned` | Hérite les groupes du responsable assigné |
| `securitysuite_inbound_email` | Gestion des groupes sur les e-mails entrants |

## Impacté par / impacte

- Consommé par `SecurityGroup.php` et `ACLAction.php` via `$sugar_config`
- Utilise `Configurator::handleOverride()` pour persister dans `config_override.php`
- Ajoute `SecurityGroups` à `addAjaxBannedModules`

---

## Notes

- L'action de suppression de groupe par défaut (`remove_default_id`) est traitée en premier, avant les autres paramètres.
