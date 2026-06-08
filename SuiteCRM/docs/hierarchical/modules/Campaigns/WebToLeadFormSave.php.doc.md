# Fichier : WebToLeadFormSave.php

**Chemin :** `modules/Campaigns/WebToLeadFormSave.php`
**Type :** PHP - Script d'action (sauvegarde formulaire)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Traite la sauvegarde de la configuration du formulaire Web-to-Lead. Reconstruit le HTML depuis les donnees POST (notamment les zones de texte marquees `ta_replace`) et stocke la configuration.

## Role technique

Script procedural. Decode `body_html` depuis HTML entities, cherche et remplace les marqueurs `ta_replace` par des textarea HTML. Utilise `SugarTinyMCE` pour le rendu de l'editeur. Requiert `include/formbase.php` et `include/SugarTinyMCE.php`.

---

## Dependances cles

- `include/formbase.php`
- `include/SugarTinyMCE.php` — editeur WYSIWYG

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Formulaire de creation/edition du formulaire Web-to-Lead dans le wizard

## Relations cles

- **Position dans le flux :** Sauvegarde de la configuration du formulaire Web-to-Lead

---

## Points d'attention

- La boucle de remplacement `ta_replace` est fragile : depend de marqueurs textuels dans le HTML (l.58).
