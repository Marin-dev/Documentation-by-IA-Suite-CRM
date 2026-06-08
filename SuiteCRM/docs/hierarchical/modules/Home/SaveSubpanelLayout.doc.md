# SaveSubpanelLayout.php

**Chemin :** `modules/Home/SaveSubpanelLayout.php`
**Type :** PHP - Script d'action
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Sauvegarde l'ordre des sous-panneaux (subpanels) d'un module dans les préférences utilisateur. Reçoit la liste ordonnée via `$_REQUEST['layout']` et le module cible via `$_REQUEST['layoutModule']`.

## Type
action / helper

## Dépendances clés
- `$current_user->setPreference()` (global)

## Exports / Symboles principaux
Aucun.

## Interactions
- **Appelé par :** JavaScript de réordonnancement des subpanels (AJAX)

## Notes
- Supporte le paramètre optionnel `layoutGroup` pour filtrer par groupe d'onglets.
