# SearchForm2.php (SearchForm)

**Chemin :** `include/SearchForm/SearchForm2.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Composant de formulaire de recherche generique de SuiteCRM. Gere le rendu, le traitement et la persistance des criteres de recherche dans les vues liste de tous les modules. Supporte la recherche basique, avancee et personnalisee (onglets configurables), ainsi que les recherches sauvegardees.

## Role technique

Classe avec proprietes publiques configurables (`$module`, `$searchdefs`, `$listViewDefs`, etc.). Utilise `ListViewSmarty` pour le rendu, `TemplateHandler` pour la gestion des templates et `EditView2` pour les champs de formulaire. Integre les onglets via `include/tabs.php`.

---

## Dependances cles

- **Imports principaux :**
  - `include/tabs.php` — gestion des onglets
  - `ListViewSmarty` (`include/ListView/ListViewSmarty.php`) — rendu liste
  - `TemplateHandler` (`include/TemplateHandler/TemplateHandler.php`) — templates Smarty
  - `EditView2` (`include/EditView/EditView2.php`) — champs de formulaire

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `SearchForm` | classe | Formulaire de recherche |
| `$seed` | propriete | Bean du module concerne |
| `$module` | propriete | Nom du module |
| `$searchdefs` | propriete | Definitions des champs de recherche |
| `$displayView` | propriete | Vue active (`basic_search` par defaut) |
| `$showAdvanced / $showBasic / $showCustom` | proprietes | Onglets visibles |
| `$displaySavedSearch` | propriete | Affiche les recherches sauvegardees |

- **Consommateurs identifies :** vues `index.php` de tous les modules avec liste (INCONNU exhaustif)

## Relations cles

- **Appele par :** controllers de modules (vues liste), typiquement via `SearchForm2.php` inclus
- **Appelle :** `ListViewSmarty`, `TemplateHandler`, `EditView2`, moteur Smarty
- **Position dans le flux global :** composant UI de recherche, entre la requete utilisateur et la requete BDD

---

## Points d'attention

- La classe complete fait plus de 80 lignes de declaration — le corps complet (methodes) n'a pas ete lu dans ce contexte. Les methodes principales (process, display, etc.) sont INCONNU sans lecture complete.
- Les searchdefs sont chargeables depuis `custom/` ce qui permet la personnalisation par Studio.
