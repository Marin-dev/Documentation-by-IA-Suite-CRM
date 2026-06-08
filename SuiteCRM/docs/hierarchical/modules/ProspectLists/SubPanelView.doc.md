# SubPanelView.php

**Chemin :** `modules/ProspectLists/SubPanelView.php`
**Type :** PHP - Vue (sous-panneau)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de sous-panneau pour ProspectLists. Affiche les listes de prospects dans le sous-panneau d'un autre module (typiquement Campaigns). Charge les chaînes de traduction du module ProspectLists.

## Type
view

## Dépendances clés
- `$current_language`, `$currentModule`, `$theme`, `$focus`, `$action`
- `return_module_language()` — chaînes de traduction de ProspectLists

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** sous-panneaux de modules liés (Campaigns notamment)
- **Appelle :** `return_module_language()`

## Notes
- Commentaire explicatif ligne 51 : "we don't want the parent module's string file, but rather the string file specific to this subpanel".
