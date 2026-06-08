# Fichier : ListViewSmartyEmails.php

**Chemin :** `modules/Emails/include/ListView/ListViewSmartyEmails.php`
**Type :** PHP — Helper liste (rendu)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue liste Smarty specialisee pour les emails. Remplace la vue liste standard par une version adaptee au module Emails, utilisant `ListViewDataEmails` pour les donnees.

## Role technique

Herite de `ListViewSmarty`. Constructeur injecte `ListViewDataEmails` comme fournisseur de donnees (`$this->lvd`). `$this->searchColumns = []` desactive les colonnes de recherche standard.

---

## Dependances

- **Herite de :** `ListViewSmarty` (`include/ListView/ListViewSmarty.php`)
- **Imports :** `ListViewDataEmails.php`
- **Instancie :** `Sugar_Smarty`, `ListViewDataEmails`

## Exports / Symboles principaux

- `ListViewSmartyEmails` — classe vue liste
  - Constructeur : configure lvd = ListViewDataEmails, searchColumns = []

- **Consommateurs :**
  - `modules/Emails/views/view.list.php`

## Relations cles

- **Appele par :** `EmailsViewList::preDisplay()`

---

## Points d'attention

- RAS
