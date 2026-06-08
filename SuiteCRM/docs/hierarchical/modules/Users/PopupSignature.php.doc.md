# Fichier : PopupSignature.php

**Chemin :** `modules/Users/PopupSignature.php`
**Type :** PHP — Vue (popup edition signature)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche une fenetre popup permettant de creer ou modifier une signature email utilisateur. Utilise un editeur TinyMCE pour la saisie en HTML.

## Role technique

Script procedural. Charge `UserSignature`, instancie le bean et recupere l'enregistrement si `record` est passe. Affiche le formulaire via `XTemplate` (`UserSignatureEditView.html`) avec integration de `SugarTinyMCE`. Le bouton Annuler ferme la fenetre (`window.close()`).

---

## Dependances principales

| Import | Role |
|---|---|
| `include/SugarTinyMCE.php` | Editeur WYSIWYG |
| `modules/Users/UserSignature.php` | Bean signature |
| `XTemplate` | Moteur de templates HTML |

## Exports / Symboles principaux

Aucun. Produit HTML popup.

---

## Relations cles

- **Appele par :** JavaScript `open_email_signature_form()` depuis la vue utilisateur (INCONNU exact)
- **Sauvegarde via :** `SaveSignature.php` (action de soumission du formulaire)
