# Fichier : AccountsListViewSmarty.php

**Chemin :** `modules/Accounts/AccountsListViewSmarty.php`
**Type :** `PHP`
**Categorie :** view (liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge de la vue liste generique pour le module Accounts. Ajoute dans le menu d'actions la possibilite d'ajouter des comptes a une liste de prospects (target list), le lien "Form Letter" PDF, le bouton "Confirm Opt-In" si la configuration le permet, et le lien de cartographie jjwg_Maps.

## Role technique

Classe `AccountsListViewSmarty` heritant de `ListViewSmarty`. Surcharge `process()` pour injecter des elements dans `$this->actionsMenuExtraItems`, surcharge `buildActionsLink()` pour reordonner les boutons, et surcharge `buildExportLink()` pour ajouter le lien cartographique.

---

## Dependances cles

| Dependance | Chemin | Role |
|---|---|---|
| `ListViewSmarty` | `include/ListView/ListViewSmarty.php` | Classe parente de la vue liste |
| `formLetter` | `modules/AOS_PDF_Templates/formLetter.php` | Lien Form Letter dans la liste |
| `ACLController` | framework | Verification des droits export |
| `Configurator` | framework | Verifie si Confirm Opt-In est active |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `AccountsListViewSmarty` | classe | Vue liste specifique Accounts |
| `process($file, $data, $htmlVar)` | methode | Surcharge : ajoute les actions supplementaires |
| `buildActionsLink($id, $location)` | methode | Surcharge : reordonne les boutons (swap indices 6/7) |
| `buildExportLink($id)` | methode | Surcharge : ajoute le lien carte jjwg_Maps |
| `buildAddAccountContactsToTargetList()` | methode protegee | Genere le lien JS pour ajout a une prospect list |

**Consommateurs identifies dans le repo :**

- `modules/Accounts/views/view.list.php` (instancie dans `preDisplay()`)

## Relations cles

- **Appele par :** `AccountsViewList::preDisplay()`
- **Appelle :** `ListViewSmarty::process()`, `formLetter::LVSmarty()`, jjwg_Maps via entryPoint URL
- **Position dans le flux :** rendu de la liste des comptes avec actions enrichies

---

## Points d'attention

- Le JS genere dans `buildAddAccountContactsToTargetList()` construit dynamiquement un formulaire DOM pour envoyer les UIDs selectionnes vers l'action `TargetListUpdate`.
- Le swap de boutons dans `buildActionsLink()` (indices 6 et 7 codes en dur) est fragile : toute modification de l'ordre des boutons parents peut casser l'UI.
- `$this->targetList = true` active dans le constructeur indique que la selection de liste de prospects est activee par defaut.
