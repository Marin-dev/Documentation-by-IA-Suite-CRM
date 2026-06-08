# Menu.php

**Chemin :** `modules/Administration/Menu.php`
**Type :** PHP (configuration / menu)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit le menu de navigation superieur du module Administration. Le tableau est deliberement vide : le module Administration n'expose pas de liens dans la barre de navigation superieure standard de SuiteCRM.

## Role technique
Initialise uniquement `$module_menu = array()`. Le framework SugarCRM charge ce fichier automatiquement pour construire les menus de module.

---

## Notes
- Fichier trivial mais necessaire pour le framework (absence = erreur).
- L'Administration n'a pas de menu superieur par design : tous les liens sont dans le panneau `index.php`.
