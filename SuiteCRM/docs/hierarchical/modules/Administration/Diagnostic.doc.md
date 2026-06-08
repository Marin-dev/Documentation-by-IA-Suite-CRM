# Diagnostic.php

**Chemin :** `modules/Administration/Diagnostic.php`
**Type :** PHP (view / page)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Affiche la page d'entree de l'outil de diagnostic SuiteCRM. Presente un formulaire permettant de selectionner les informations a collecter (config, custom dir, phpinfo, schema BDD, logs, vardefs, md5). L'execution est deleguee a `DiagnosticRun.php`.

## Role technique
Script procedral de rendu. Recupere une instance DBManager, passe les variables Smarty necessaires (strings, DB name, print URL, images de recherche), et affiche le template `Diagnostic.tpl`.

---

## Dependances cles
| Element | Role |
|---|---|
| `DBManagerFactory::getInstance()` | Instance BDD pour afficher le nom |
| `Sugar_Smarty` | Template |
| `SugarThemeRegistry::current()` | Images de filtre recherche |
| `$GLOBALS['sugar_config']['hide_admin_diagnostics']` | Variable de config pour masquer l'outil |

## Symboles principaux
- Aucune classe ni fonction — script procedral de vue

## Interactions
- **Appele par :** `index.php?module=Administration&action=Diagnostic`
- **Appelle :** Template `modules/Administration/Diagnostic.tpl`
- **Lie a :** `DiagnosticRun.php` (execution), `DiagnosticDownload.php` (telechargement), `DiagnosticDelete.php` (suppression)

---

## Notes
- Double protection d'acces : `is_admin()` ET `$sugar_config['hide_admin_diagnostics']` (lignes 55-60).
- `$db` est instancie deux fois (lignes 62-65) — code defensif/redondant.
