# Fichier : ShowDuplicates.php

**Chemin :** `modules/Contacts/ShowDuplicates.php`
**Type :** PHP - Script de vue (detection de doublons)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la page de confirmation des doublons detectes lors de la creation d'un contact. Permet a l'utilisateur de choisir entre creer quand meme le contact ou utiliser un enregistrement existant.

## Role technique

Script procedural. Verifie la presence de `$_SESSION['SHOW_DUPLICATES']` (sinon die). Restitue les valeurs POST depuis la session (contournement des limites de longueur des URLs GET). Affiche la liste des doublons potentiels.

---

## Dependances cles

- `$_SESSION['SHOW_DUPLICATES']` — donnees POST serialisees par `ContactFormBase`
- `ContactFormBase::checkForDuplicates()` — detecte les doublons (appele avant ce script)

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Flux de sauvegarde de contact : `ContactFormBase` -> `ShowDuplicates.php`

## Relations cles

- **Position dans le flux :** Etape intermediaire entre la soumission et la sauvegarde si doublon detecte
- **Apres confirmation :** redirection vers `Save.php` avec `dup_checked=1`

---

## Points d'attention

- Die si `$_SESSION['SHOW_DUPLICATES']` absent — protection contre l'acces direct.
- Les donnees POST transitent via la session pour contourner les limites de longueur des URLs (l.48).
