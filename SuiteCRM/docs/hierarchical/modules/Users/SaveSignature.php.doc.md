# Fichier : SaveSignature.php

**Chemin :** `modules/Users/SaveSignature.php`
**Type :** PHP — Script d'action AJAX (sauvegarde signature)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Sauvegarde une signature email utilisateur (creation ou modification) et retourne un script JavaScript qui rafraichit la liste des signatures dans la fenetre parente puis ferme la popup.

## Role technique

Script procedural. Recupere ou cree un `UserSignature`. Assigne `name`, `signature` (texte brut depouille de tags HTML) et `signature_html` depuis `$_REQUEST`. Appelle `$us->save()`. Emet un bloc `<script>` appelant `window.opener.refresh_signature_list(id, name)` puis `window.close()`.

---

## Dependances principales

| Import | Role |
|---|---|
| `modules/Users/UserSignature.php` | Bean signature |
| `strip_tags()` / `br2nl()` / `from_html()` | Nettoyage texte brut |
| `create_guid()` | Generation ID pour nouvelle signature |

## Exports / Symboles principaux

Aucun. Produit du JavaScript inline.

---

## Relations cles

- **Appele par :** formulaire de `PopupSignature.php`
- **Appelle :** `UserSignature::save()`
- **Communique avec :** `window.opener` via JavaScript (`refresh_signature_list`)
