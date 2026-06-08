# Locale.php

**Chemin :** `modules/Administration/Locale.php`
**Type :** PHP (view / page parametres)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page d'administration des parametres de localisation : formats de date, heure, nombres, encodage d'export, format des noms (civilite, ordre), collation BDD. Gere la lecture et la sauvegarde de ces parametres via `Configurator`.

## Role technique
Script procedral. Si `$_REQUEST['process'] == 'true'`, appelle `$cfg->populateFromPost()` puis `$cfg->handleOverride()` pour persister dans `config_override.php`. Reconnecte la BDD si la collation change. Passe au template Smarty `Locale.tpl` les options de langues, charsets, formats de noms, et messages d'erreur de migration de format.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Configurator/Configurator.php` | Persistance `config_override.php` |
| `DBManagerFactory::getInstance()` | Reconnexion BDD si collation changee |
| `$locale` (global SuiteCRM) | Options de format de nom, charsets |
| `Sugar_Smarty` | Rendu template |
| `get_languages()` | Liste des langues disponibles |

## Symboles principaux
- Aucune classe ni fonction — script procedral de vue

## Interactions
- **Appele par :** `index.php?module=Administration&action=Locale`
- **Appelle :** `Configurator`, `DBManagerFactory`, `$locale->getUsableLocaleNameOptions()`, `$locale->getCharsetSelect()`
- **Template :** `modules/Administration/Locale.tpl`

---

## Notes
- Acces restreint : `is_admin($current_user)` en ligne 45.
- La collation BDD est modifiee uniquement si la valeur change par rapport a `$sugar_config['dbconfigoption']['collation']` (ligne 70-76) — protege contre les reconnexions inutiles.
- Detecte si le format de nom est invalide suite a une mise a jour (`$locale->invalidLocaleNameFormatUpgrade()`).
