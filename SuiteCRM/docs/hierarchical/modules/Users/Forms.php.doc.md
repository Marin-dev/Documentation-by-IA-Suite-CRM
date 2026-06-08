# Fichier : Forms.php

**Chemin :** `modules/Users/Forms.php`
**Type :** PHP — Helper (fonctions formulaire — obsoletes)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Contenait des fonctions de generation de JavaScript pour la validation des formulaires utilisateur et la configuration. Ces fonctions sont desormais obsoletes et retournent une chaine vide, la logique ayant ete migree vers `UserEditView.js`.

## Role technique

Fichier declarant trois fonctions : `user_get_validate_record_js()`, `user_get_chooser_js()`, `user_get_confsettings_js()`. Toutes retournent `''` (ou rien). Le commentaire indique explicitement `NO LONGER USED, MOVED TO UserEditView.js`.

---

## Exports / Symboles principaux

| Symbole | Type | Note |
|---|---|---|
| `user_get_validate_record_js()` | fonction | Obsolete — retourne `''` |
| `user_get_chooser_js()` | fonction | Obsolete — retourne `''` |
| `user_get_confsettings_js()` | fonction | Obsolete — retourne rien |

---

## Points d'attention

- Fichier maintenu par compatibilite ascendante uniquement. Ne pas ajouter de logique ici.
- La logique JS reelle est dans `modules/Users/UserEditView.js` (hors perimetre PHP).
