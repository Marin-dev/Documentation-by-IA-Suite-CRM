# UpgradeIISAccess.php

**Chemin :** `modules/Administration/UpgradeIISAccess.php`
**Type :** PHP (action / securite)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Repare et configure le fichier `web.config` d'IIS (Internet Information Services) pour restreindre les acces au dossier upload sur Windows. Equivalent de `UpgradeAccess.php` pour IIS.

## Role technique
Appelle `handleWebConfig()` depuis `install/install_utils.php`.

---

## Dependances cles
| Element | Role |
|---|---|
| `install/install_utils.php` | `handleWebConfig()` |

## Interactions
- **Appele par :** Processus d'upgrade sur IIS (INCONNU - contexte exact)

## Notes
- Specifique a Windows/IIS — inutile sur Apache/Nginx.
