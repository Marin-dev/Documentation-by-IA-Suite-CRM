# WebToLeadFormSave.php

**Chemin :** `modules/Campaigns/WebToLeadFormSave.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de sauvegarde et génération du formulaire Web-to-Lead. Traite le corps HTML du formulaire (reçu du POST) en remplaçant les balises `ta_replace` par des balises textarea réelles (pré-traitement TinyMCE), puis génère le code HTML final du formulaire à intégrer sur un site externe.

**Type :** action (script de sauvegarde/génération)

---

## Dépendances clés

- `include/formbase.php`
- `include/SugarTinyMCE.php` — prétraitement du corps HTML
- `$mod_strings`, `$app_strings`
- `$_REQUEST['body_html']` — corps HTML du formulaire soumis

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

---

## Interactions

**Appelle :**
- `html_entity_decode()` sur `$_REQUEST['body_html']`
- Remplacement des balises `ta_replace` par des `<textarea>`

**Appelée par :** Soumission du formulaire depuis `WebToLeadCreation.php`.

**Position dans le flux global :** Dernière étape de la création du formulaire Web-to-Lead — produit le code HTML à copier-coller.

---

## Notes

- La boucle de remplacement `ta_replace` (ligne 58+) est une technique spécifique pour gérer la compatibilité entre TinyMCE et les textareas dans les formulaires web.
- Le résultat est le HTML complet du formulaire avec CSS inline, prêt pour intégration externe.
