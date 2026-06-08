# SubPanelViewProjects.php

**Chemin :** `modules/Opportunities/SubPanelViewProjects.php`
**Type :** Vue (sous-panneau legacy - projets)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Rendu legacy du sous-panneau "Opportunites lies aux Projets". Affiche uniquement le bouton "Selectionner" (pas de creation directe). Utilise le template `SubPanelViewProjects.html`.

## Role technique
Script procedural legacy similaire a `SubPanelView.php` mais sans le bouton "Nouveau" et avec un template different. Inclut un lien "Supprimer" (`delete_inline`).

---

## Points d'attention
- Contrairement a `SubPanelView.php`, pas de creation directe d'opportunite depuis ce sous-panneau.
- Fichier legacy.
