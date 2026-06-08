# SubPanelView.php

**Chemin :** `modules/Opportunities/SubPanelView.php`
**Type :** Vue (sous-panneau legacy)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Rendu legacy du sous-panneau "Opportunites" dans les vues de detail des modules Accounts et Contacts. Affiche les boutons "Nouvelle" et "Selectionner" (popup de selection) adaptes selon le module parent.

## Role technique
Script procedural legacy. Detecte le module courant (`$currentModule`) pour pre-remplir les champs `account_id`/`contact_id` dans le formulaire de creation. Utilise `ListView` + `SubPanelView.html`.

---

## Points d'attention
- Logique differenciee selon `$currentModule == 'Accounts'` ou `'Contacts'` pour le pre-remplissage des champs.
- Fichier legacy, probablement superpose par les sous-panneaux MVC.
