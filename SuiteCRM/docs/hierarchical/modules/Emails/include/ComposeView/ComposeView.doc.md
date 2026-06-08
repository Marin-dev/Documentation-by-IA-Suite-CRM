# Fichier : ComposeView.php

**Chemin :** `modules/Emails/include/ComposeView/ComposeView.php`
**Type :** PHP — Helper vue compose
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe d'edition specialisee pour le formulaire de composition d'email. Surcharge `EditView` avec le template compose specifique.

## Role technique

Herite de `EditView` (`include/EditView/EditView2.php`). Override `setup()` avec le template par defaut `ComposeView.tpl`. `$this->view = get_class($this)` dans le constructeur.

---

## Dependances

- **Herite de :** `EditView` (`include/EditView/EditView2.php`)
- **Template :** `modules/Emails/include/ComposeView/ComposeView.tpl`

## Exports / Symboles principaux

- `ComposeView` — classe editview compose
  - `setup($module, $focus, $metadataFile, $tpl = 'ComposeView.tpl', ...)` — initialise la vue

- **Consommateurs :**
  - `modules/Emails/views/view.compose.php`

## Relations cles

- **Appele par :** `EmailsViewCompose::getEditView()`

---

## Points d'attention

- Corps `setup()` partiellement lu — logique additionnelle INCONNUE.
