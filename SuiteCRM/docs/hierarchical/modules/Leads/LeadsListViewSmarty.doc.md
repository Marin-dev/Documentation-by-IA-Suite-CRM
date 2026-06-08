# Fichier : LeadsListViewSmarty.php

**Chemin :** `modules/Leads/LeadsListViewSmarty.php`
**Type :** `PHP`
**Categorie :** view (liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge de la vue liste pour le module Leads. Ajoute le lien Form Letter PDF, le bouton "Confirm Opt-In" (si active) et le lien de cartographie jjwg_Maps dans la barre d'actions.

## Role technique

Classe `LeadsListViewSmarty` heritant de `ListViewSmarty`. Meme pattern que `AccountsListViewSmarty` : surcharge `process()` et `buildExportLink()`. Pas de logique de "target list" specifique (contrairement aux Accounts).

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ListViewSmarty` | Classe parente |
| `formLetter` | Lien Form Letter PDF |
| `Configurator` | Verifie si Confirm Opt-In est active |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadsListViewSmarty` | classe | Vue liste Leads |
| `process($file, $data, $htmlVar)` | methode | Surcharge : ajoute Confirm Opt-In si active |
| `buildExportLink($id)` | methode | Surcharge : ajoute le lien cartographique Maps |

**Consommateurs identifies dans le repo :**

- `modules/Leads/views/view.list.php`

## Points d'attention

- Identique dans sa structure a `AccountsListViewSmarty` mais sans le bouton "Ajouter a la liste de prospects".
