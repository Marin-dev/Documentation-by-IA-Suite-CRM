# VersionCheck.php

**Chemin :** `modules/SecurityGroups/VersionCheck.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Hook logique qui verifie que la version de SecuritySuite correspond a la version de SugarCRM/SuiteCRM. Affiche une alerte JS si les versions ne correspondent pas.

## Type
helper / logic hook

## Dependances cles
- `$sugar_config['securitysuite_version']`, `$sugar_config['sugar_version']`

## Exports / Symboles principaux
- `class VersionCheck`
- `version_check($event, $arguments)` — hook (admin only, hors PDF/ajax)

## Interactions
- **Appele par :** framework LogicHook SuiteCRM

## Notes
- Lien de mise a jour pointe vers `eggsurplus.com` (origine externe — vestige SugarCRM).
- Sortie JS inline si incompatibilite.
