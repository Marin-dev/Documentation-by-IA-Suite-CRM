# index.php

**Chemin :** `modules/Administration/index.php`
**Type :** PHP (View / page principale)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Point d'entree visuel du module Administration. Affiche la page d'accueil du panneau d'administration avec toutes les sections et liens de navigation (groupes de parametres, icones, descriptions). C'est la page que voit l'administrateur lorsqu'il accede a `index.php?module=Administration&action=index`.

## Role technique
Script PHP procedral qui lit les metadonnees de navigation depuis `metadata/adminpaneldefs.php` (variable `$admin_group_header`), structure les donnees en tableaux (labels, URLs, icones, descriptions, colonnes), puis les passe a un template Smarty `index.tpl` pour rendu HTML. Filtre les liens selon `$GLOBALS['admin_access_control_links']` pour le controle d'acces granulaire.

---

## Dependances cles
| Import | Role |
|---|---|
| `modules/Administration/metadata/adminpaneldefs.php` | Definition de toutes les sections d'administration |
| `Sugar_Smarty` | Moteur de template |
| `getClassicModuleTitle()` | Affichage du titre de page |
| `translate()` | Internationalisation des labels |
| `$GLOBALS['admin_access_control_links']` | Liste des liens d'acces restreint |

## Symboles principaux
- Aucune classe ni fonction exportee — script procedral de rendu

## Interactions
- **Appele par :** Framework SugarCRM (`action=index` par defaut)
- **Appelle :** `metadata/adminpaneldefs.php`, template `modules/Administration/index.tpl`
- **Acces controle :** `is_admin()` ou `is_admin_for_any_module()` requis (lignes 52-54)

---

## Notes
- La logique de mise en colonne (2 colonnes, `$tab[]`) est calculee directement dans ce script via `$colnum % 2`.
- Si `$values[3]` contient plusieurs modules, leurs liens sont fusionnes en un seul tableau `$return_array`.
- Les liens presents dans `$GLOBALS['admin_access_control_links']` sont silencieusement supprimes sans message d'erreur.
