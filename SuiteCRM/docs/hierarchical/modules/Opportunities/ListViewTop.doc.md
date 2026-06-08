# ListViewTop.php

**Chemin :** `modules/Opportunities/ListViewTop.php`
**Type :** Vue (liste top opportunites, legacy)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Affiche le "Top 5" des opportunites ouvertes de l'utilisateur courant (hors Closed Won et Closed Lost), triees par montant decroissant. Vue legacy pour le tableau de bord.

## Role technique
Script procedural legacy. Utilise `ListView` + XTemplate `ListViewTop.html`. Filtre : `sales_stage NOT IN ('Closed Won', 'Closed Lost')` + `assigned_user_id = current_user->id`. Limite a 5 enregistrements, tries par `amount DESC`.

---

## Points d'attention
- Legacy XTemplate. Probablement remplace par les dashlets.
- Le filtre ne gere pas le soft-delete explicitement (suppose que la requete de base le fait).
