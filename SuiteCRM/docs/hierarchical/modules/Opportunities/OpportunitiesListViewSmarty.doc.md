# Fichier : OpportunitiesListViewSmarty.php

**Chemin :** `modules/Opportunities/OpportunitiesListViewSmarty.php`
**Type :** `PHP`
**Categorie :** view (liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge de la vue liste pour les opportunites. Ajoute le lien d'export standard et le lien de cartographie jjwg_Maps dans la barre d'actions.

## Role technique

Classe `OpportunitiesListViewSmarty` heritant de `ListViewSmarty`. Surcharge uniquement `buildExportLink()` pour injecter les deux liens (Export + Map) avec un `</li><li>` HTML.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ListViewSmarty` | Classe parente |
| `formLetter` | Form Letter PDF |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `OpportunitiesListViewSmarty` | classe | Vue liste Opportunities |
| `buildExportLink($id)` | methode | Surcharge : ajoute le lien cartographique Maps |

**Consommateurs identifies dans le repo :**

- `modules/Opportunities/views/view.list.php`

## Points d'attention

- Le hack `</li><li>` entre les deux liens est fragile : dependant du rendu HTML du parent.
- Pas de methode `process()` surchargee.
