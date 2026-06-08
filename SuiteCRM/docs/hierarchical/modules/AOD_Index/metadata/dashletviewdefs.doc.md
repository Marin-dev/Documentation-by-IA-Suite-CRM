# dashletviewdefs.php

**Chemin :** `modules/AOD_Index/metadata/dashletviewdefs.php`
**Configure :** Colonnes et filtres du dashlet AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit `$dashletData['AOD_IndexDashlet']` — les colonnes et les champs de recherche du dashlet AOD_Index. Le dashlet affiche les enregistrements AOD_Index avec filtre par date et utilisateur assigne.

## Parametres cles
| Section | Contenu |
|---|---|
| `searchFields` | `date_entered`, `date_modified`, `assigned_user_id` (defaut : utilisateur courant) |
| Colonne `name` | largeur 40%, lien, active par defaut |
| Colonne `date_entered` | largeur 15%, active par defaut |
| Colonne `date_modified` | largeur 15%, non active par defaut |
| Colonne `created_by` | largeur 8%, non active par defaut |
| Colonne `assigned_user_name` | largeur 8%, non active par defaut |

## Impacte par / impacte
- Utilise `$current_user` global pour le defaut du filtre utilisateur
- Charge par le framework SugarCRM lors de l'affichage du dashlet

## Points d'attention
- Utilise `$current_user` directement en scope global au chargement — valeur evaluee a la definition, pas a l'affichage.
