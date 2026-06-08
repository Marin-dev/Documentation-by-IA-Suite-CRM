# Fichier : ChangeGroupTab.php

**Chemin :** `modules/Users/ChangeGroupTab.php`
**Type :** PHP — Script d'action (changement onglet groupe menu)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Met a jour la preference de groupe de theme pour la navigation par onglets du menu, puis invalide le cache ETag du menu principal pour forcer son rechargement.

## Role technique

Script procedural tres court. Lit `$_REQUEST['newGroup']`, ecrit dans la preference `theme_current_group` de l'utilisateur courant, et appelle `$current_user->incrementETag('mainMenuETag')` pour invalider le cache client du menu.

---

## Exports / Symboles principaux

Aucun.

---

## Relations cles

- **Appele par :** INCONNU — probablement appel AJAX depuis le menu principal lors du changement d'onglet de groupe
- **Appelle :** `$current_user->setPreference()`, `$current_user->incrementETag()`

---

## Points d'attention

- `incrementETag` invalide le cache HTTP du menu principal — important pour la coherence visuelle apres changement.
