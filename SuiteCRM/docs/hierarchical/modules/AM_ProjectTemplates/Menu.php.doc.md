# Fichier : Menu.php (configuration)

**Chemin :** `modules/AM_ProjectTemplates/Menu.php`
**Configure :** Menu du module AM_ProjectTemplates
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Declare les entrees du menu de navigation du module AM_ProjectTemplates. Trois actions conditionnelles selon les droits ACL.

---

## Parametres cles

| Action | Condition ACL | Lien |
| --- | --- | --- |
| Creer un template | `edit` | `EditView` |
| Lister les templates | `list` | `index` |
| Importer | `import` | `Import&Step1` |

---

## Impacte par / impacte

- Rendu par le framework de navigation SuiteCRM dans la barre de menu du module
- Verifie les droits via `ACLController::checkAccess()`

---

## Points d'attention

- Structure standard SuiteCRM Menu.php — RAS.
