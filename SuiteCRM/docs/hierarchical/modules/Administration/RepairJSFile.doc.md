# RepairJSFile.php

**Chemin :** `modules/Administration/RepairJSFile.php`
**Type :** PHP (view / AJAX trigger)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Affiche une page qui declenche automatiquement (via JS inline) la reparation/reconstruction des fichiers JS. L'appel reel est asynchrone vers `callJSRepair.php`.

## Role technique
Affiche un `<div id="msgDiv">` et un bloc JS qui, apres 2 secondes (`setTimeout`), fait une requete AJAX POST vers `index.php?module=Administration&action=callJSRepair` avec les parametres `js_admin_repair` et `root_directory`.

---

## Interactions
- **Appele par :** `index.php?module=Administration&action=RepairJSFile`
- **Appelle via AJAX :** `callJSRepair.php` (action=callJSRepair)

---

## Notes
- Utilise `YAHOO.util.Connect.asyncRequest` (YUI 2) — librairie legacy.
- Le delai `setTimeout 2000ms` semble arbitraire.
