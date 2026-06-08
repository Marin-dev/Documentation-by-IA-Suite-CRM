# Fichier : acldefs.php

**Chemin :** `modules/Accounts/metadata/acldefs.php`
**Type :** `PHP`
**Categorie :** configuration (ACL)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les permissions specifiques au module Accounts pour le systeme ACL (Access Control List). Peut specifier des actions et des champs avec des niveaux d'acces personnalises.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$aclFields` ou equivalent | Permissions au niveau des champs |
| Actions definies | Typiquement : view, edit, delete, import, export |

## Impacte par / impacte

- Consomme par `ACLController` lors des verifications d'acces
- Complement du systeme ACL global

## Points d'attention

- Fichier de configuration pur. Les permissions sont evaluees en combinaison avec les roles utilisateur.
