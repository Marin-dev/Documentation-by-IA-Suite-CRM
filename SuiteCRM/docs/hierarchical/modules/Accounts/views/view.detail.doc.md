# Fichier : view.detail.php

**Chemin :** `modules/Accounts/views/view.detail.php`
**Type :** `PHP`
**Categorie :** view (detail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue de detail d'un compte. Enrichit la vue standard en ajoutant des boutons "Pousser l'adresse" permettant de copier l'adresse de facturation ou de livraison du compte vers des contacts selectionnes dans un popup.

## Role technique

Classe `AccountsViewDetail` heritant de `ViewDetail`. Surcharge `display()` pour injecter les variables Smarty `custom_code_billing` et `custom_code_shipping` avec le HTML des boutons de copie d'adresse. Integre aussi la popup "Form Letter" PDF via `formLetter::DVPopupHtml()`.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ViewDetail` | Classe parente (framework) |
| `formLetter::DVPopupHtml()` | Injecte le HTML de popup Form Letter |
| `ACLController::checkAccess('Contacts', 'edit')` | Conditionne l'affichage des boutons de copie |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `AccountsViewDetail` | classe | Vue detail Account |
| `display()` | methode | Surcharge : ajoute les boutons de copie d'adresse |
| `generatePushCode($param)` | methode | Genere le HTML du bouton "Pousser l'adresse" vers les contacts |

## Relations cles

- **Appele par :** Framework SuiteCRM (routing action=DetailView, module=Accounts)
- **Variables Smarty assignees :** `custom_code_billing`, `custom_code_shipping` (consommees par `Address/DetailView.tpl`)

---

## Points d'attention

- `generatePushCode` construit une URL avec tous les champs d'adresse URL-encodes pour pre-remplir le popup contact.
- Double verification `empty($this->bean->id)` dans `display()` (lignes 63 et 84) : la seconde est redondante.
- Les sauts de ligne dans les adresses sont convertis en `<br>` dans l'URL generee.
