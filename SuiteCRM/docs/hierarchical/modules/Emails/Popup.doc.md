# Fichier : Popup.php

**Chemin :** `modules/Emails/Popup.php`
**Type :** PHP — Script d'action (popup)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree du popup de selection d'emails. Si le mode est `show_raw`, affiche la source brute de l'email. Sinon, utilise le Popup_Picker standard.

## Role technique

Script procedural court. Branchement conditionnel selon `$_REQUEST['mode']`.

---

## Dependances

- **Utilise :** `BeanFactory::newBean('Emails')`, `include/Popups/Popup_picker.php`, `Popup_Picker`

## Exports / Symboles principaux

- Aucun — script de routage uniquement

## Relations cles

- **Appele par :** vue popup SuiteCRM

---

## Points d'attention

- Le mode `show_raw` affiche `$email->raw_source` avec `nl2br()` — potentielle fuite HTML si le raw_source n'est pas assaini.
