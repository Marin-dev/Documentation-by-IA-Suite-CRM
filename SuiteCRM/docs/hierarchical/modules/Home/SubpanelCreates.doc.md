# SubpanelCreates.php

**Chemin :** `modules/Home/SubpanelCreates.php`
**Type :** PHP - Helper (action AJAX)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Charge et affiche le formulaire de création rapide (QuickCreate) d'un enregistrement depuis un sous-panneau, via AJAX. Détermine si un override `{Module}QuickCreate.php` existe, sinon utilise `EditViewQuickCreate` ou `SubpanelQuickCreate` selon le type de vue du module cible.

## Type
helper

## Dépendances clés
- `include/EditView/EditViewQuickCreate.php` — formulaire de création rapide legacy
- `include/EditView/SubpanelQuickCreate.php` — formulaire standard de création en sous-panneau
- `$_REQUEST['target_module']`, `$_REQUEST['tpl']`, `$_REQUEST['target_view']`
- `isAllowedModuleName()` — validation du module cible

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** requêtes AJAX depuis les sous-panneaux de n'importe quel module
- **Appelle :** `EditViewQuickCreate`, `SubpanelQuickCreate`, ou classe custom `{Module}SubpanelQuickCreate`

## Notes
- Validation du `target_module` via `isAllowedModuleName()` (ligne 47), lève `InvalidArgumentException` si invalide.
- Supporte les overrides custom via `custom/modules/{Module}/views/view.subpanelquickcreate.php`.
