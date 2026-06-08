# Fichier : view.import.php

**Chemin :** `modules/Emails/views/view.import.php`
**Type :** PHP — Vue (import email depuis IMAP)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue permettant d'editer les metadonnees d'un email non-importe avant de l'importer dans SuiteCRM (liaison CRM, categorie, etc.).

## Role technique

Herite de `ViewEdit`. Cache les elements standard de l'interface (titre, header, footer, JS). Utilise le template `importviewdefs.php` et `ImportView.tpl`.

---

## Dependances

- **Herite de :** `ViewEdit`

## Exports / Symboles principaux

- `EmailsViewImport` — classe vue
  - `preDisplay()` — configure l'editview pour l'import non-importe

## Relations cles

- **Appele par :** `EmailsController::action_ImportView()`

---

## Points d'attention

- `formName = 'EditNonImported'` pour eviter les conflits de cache avec la vue edit standard.
- UI minimale (pas de header/footer/JS Sugar standard).
