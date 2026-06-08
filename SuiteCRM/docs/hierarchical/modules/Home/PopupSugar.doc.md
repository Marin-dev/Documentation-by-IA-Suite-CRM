# PopupSugar.php

**Chemin :** `modules/Home/PopupSugar.php`
**Type :** PHP - Vue popup (easter egg)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche une fenêtre popup animée présentant le générique de l'équipe SugarCRM (fondateurs + développeurs) sous forme de défilement vertical. Supporte différents styles d'affichage via le paramètre `$_REQUEST['style']` (reverse, random, decreasing, sort, rsort).

## Type
view

## Dépendances clés
- `insert_popup_header($theme)` — fonction globale pour l'en-tête popup

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural + HTML/JS embarqué.

## Interactions
- **Appelé par :** INCONNU (action déclenchée manuellement ou via URL directe)
- **Appelle :** `insert_popup_header()`

## Notes
- Easter egg hérité de SugarCRM CE. Contient une liste fixe de noms codés en dur.
- La protection `sugarEntry` est placée à l'intérieur de la balise `<body>`, ce qui est inhabituel.
- Utilise `setTimeout` JavaScript pour l'animation de défilement.
