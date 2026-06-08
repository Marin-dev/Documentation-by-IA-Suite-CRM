# RebuildConfig.php

**Chemin :** `modules/Administration/RebuildConfig.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Reconstruit le fichier `config.php` en le regenerant depuis la configuration "propre" (sans la fusion de `config_override.php`). Utile apres une corruption ou migration.

## Role technique
Verifie que `config.php` est accessible en ecriture. En POST (`perform_rebuild`), appelle `loadCleanConfig()` puis `rebuildConfigFile($clean_config, $sugar_version)`. Affiche le statut via template Smarty `templates/RebuildConfig.tpl`.

---

## Dependances cles
| Element | Role |
|---|---|
| `loadCleanConfig()` | Charge config.php sans config_override |
| `rebuildConfigFile()` | Ecrit le fichier config.php |
| `Sugar_Smarty` | Template |

## Interactions
- **Inclus/appele par :** Action d'administration via Quick Repair ou URL directe
- **Template :** `modules/Administration/templates/RebuildConfig.tpl`

---

## Notes
- Le bouton de reconstruction est desactive si `config.php` n'est pas en ecriture.
- Evite la fusion avec `config_override.php` (bug #54403 mentionne en commentaire ligne 69).
