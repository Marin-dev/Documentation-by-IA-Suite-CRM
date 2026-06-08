# ⚙️ actiondefs.php (configuration)

**Chemin :** `modules/ACLActions/actiondefs.php`
**Configure :** Constantes ACL et définitions des actions par type
**Dernière mise à jour doc :** 2026-06-02

---

## Ce que ce fichier configure

Définit les constantes numériques des niveaux d'accès ACL (`ACL_ALLOW_*`), les métadonnées de rendu (`$GLOBALS['ACLActionAccessLevels']`), et la liste des actions disponibles par type (`$GLOBALS['ACLActions']`). Peut être surchargé par `actiondefs.override.php`.

## Paramètres clés

| Constante | Valeur | Signification |
|---|---|---|
| `ACL_ALLOW_ADMIN_DEV` | 100 | Admin+Dev |
| `ACL_ALLOW_ADMIN` | 99 | Admin uniquement |
| `ACL_ALLOW_ALL` | 90 | Tous les utilisateurs |
| `ACL_ALLOW_ENABLED` | 89 | Module activé |
| `ACL_ALLOW_DEV` | 95 | Développeurs |
| `ACL_ALLOW_OWNER` | 75 | Propriétaire uniquement |
| `ACL_ALLOW_NORMAL` | 1 | Standard |
| `ACL_ALLOW_DEFAULT` | 0 | Valeur par défaut |
| `ACL_ALLOW_DISABLED` | -98 | Module désactivé |
| `ACL_ALLOW_NONE` | -99 | Accès interdit |

## Impacté par / impacte

- Chargé par `ACLController.php` et `ACLAction.php` au démarrage
- Peut être surchargé par `actiondefs.override.php` (SecurityGroups)
- Consommé par `ACLAction::getUserActions()`, `ACLAction::setupCategoriesMatrix()`

## Notes

- `$GLOBALS['ACLActions']` définit pour chaque type (`module`, `field`) les actions disponibles avec leurs niveaux d'accès possibles — source de vérité pour la UI des rôles ACL.
- Les couleurs associées aux niveaux sont utilisées dans la vue d'édition des rôles ACLRoles.
