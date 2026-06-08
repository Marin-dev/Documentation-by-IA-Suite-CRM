# SubpanelEdits.php

**Chemin :** `modules/Home/SubpanelEdits.php`
**Type :** PHP - Helper (action AJAX)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Charge et affiche le formulaire d'édition rapide (QuickEdit) d'un enregistrement existant depuis un sous-panneau, via AJAX. Logique similaire à `SubpanelCreates.php` mais pour la modification (vue `QuickEdit`).

## Type
helper

## Dépendances clés
- `include/EditView/EditViewQuickCreate.php` — formulaire d'édition rapide legacy
- `include/EditView/SubpanelQuickEdit.php` — formulaire standard d'édition en sous-panneau
- `$_REQUEST['target_module']`, `$_REQUEST['tpl']`, `$_REQUEST['target_view']`

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** requêtes AJAX depuis les sous-panneaux pour l'édition inline
- **Appelle :** `EditViewQuickCreate`, `SubpanelQuickEdit`, ou classe custom `Custom{Module}SubpanelQuickEdit`

## Notes
- Pas de validation `isAllowedModuleName()` contrairement à `SubpanelCreates.php` — risque de sécurité potentiel.
- Supporte les overrides custom via `custom/modules/{Module}/views/view.subpanelquickedit.php`.
