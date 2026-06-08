# UpgradeAccess.php

**Chemin :** `modules/Administration/UpgradeAccess.php`
**Type :** PHP (action / securite)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Repare et s'assure que le fichier `.htaccess` du repertoire `upload/` contient la directive `Deny from all`. Protege le dossier d'upload contre l'acces direct HTTP. Appele pendant la mise a jour et comme outil de reparation.

## Role technique
Appelle `handleHtaccess()` (depuis `install/install_utils.php`), puis verifie/cree `upload://.htaccess` avec la directive `Order Deny,Allow / Deny from all`.

---

## Dependances cles
| Element | Role |
|---|---|
| `install/install_utils.php` | `handleHtaccess()` — gestion htaccess global |

## Interactions
- **Appele par :** Processus d'upgrade ET `index.php?module=Administration&action=UpgradeAccess`
- **Modifie :** `upload://.htaccess`
