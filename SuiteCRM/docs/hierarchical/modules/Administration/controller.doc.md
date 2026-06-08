# controller.php

**Chemin :** `modules/Administration/controller.php`
**Type :** PHP (Controller MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Controleur principal du module Administration. Gere les actions HTTP specifiques : sauvegarde des onglets actifs, sauvegarde des langues activees, sauvegarde des parametres de recherche globale, mise a jour de l'interface Ajax, et reconstruction des sprites CSS.

## Role technique
Etend `SugarController` (framework MVC SugarCRM). Chaque methode publique `action_*` correspond a une action URL (`action=savetabs`, `action=savelanguages`, etc.). Utilise `Configurator` pour persister les changements dans `config_override.php`, `TabController` pour les onglets, `UnifiedSearchAdvanced` pour la recherche globale, et `rebuildSprites()` pour les icones CSS.

---

## Dependances cles
| Import | Role |
|---|---|
| `SugarController` (parent, auto-charge) | Framework controleur |
| `include/SubPanel/SubPanelDefinitions.php` | Gestion sous-panneaux |
| `modules/MySettings/TabController.php` | Gestion onglets systeme |
| `modules/Home/UnifiedSearchAdvanced.php` | Parametres recherche globale |
| `modules/Configurator/Configurator.php` | Persistance config_override.php |
| `modules/UpgradeWizard/uw_utils.php` | Fonction rebuildSprites() |

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `AdministrationController` | Classe | Controleur du module |
| `action_savetabs()` | Methode | Sauvegarde onglets actifs/masques + sous-panneaux |
| `action_savelanguages()` | Methode | Sauvegarde langues activees/desactivees |
| `action_saveglobalsearchsettings()` | Methode | Sauvegarde modules de recherche globale (JSON) |
| `action_UpdateAjaxUI()` | Methode | Maj liste modules bannis pour Ajax |
| `action_callRebuildSprites()` | Methode | Reconstruit les sprites CSS via GD |
| `mergeFtsConfig($type, $newConfig)` | Methode | Fusionne config FTS (ElasticSearch) existante avec nouvelles valeurs |

## Interactions
- **Appele par :** Le framework SugarCRM via `index.php?module=Administration&action=*`
- **Appelle :** `TabController`, `SubPanelDefinitions`, `UnifiedSearchAdvanced`, `Configurator`, `rebuildSprites()`
- **Redirige vers :** `index.php?module=Administration&action=ConfigureTabs`, `Languages`, `configureajaxui`

---

## Notes
- `action_callRebuildSprites()` verifie la presence de `imagecreatetruecolor` (extension GD) avant d'executer — retourne un message si GD absent.
- `mergeFtsConfig()` protege les parametres ElasticSearch non exposes en UI (ex: auth curl) d'un ecrasement.
- Toutes les actions verifient `is_admin($current_user)` avant execution.
