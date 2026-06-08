# Fichier : view.detailnonimported.php

**Chemin :** `modules/Emails/views/view.detailnonimported.php`
**Type :** PHP — Vue (detail email non-importe)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue detail d'un email present sur le serveur IMAP mais non encore importe dans SuiteCRM. Permet de le visualiser et d'agir dessus (importer, lier, etc.).

## Role technique

Herite de `ViewDetail`. Utilise `EmailsNonImportedDetailView`. `display()` appelle `process()` puis `display()` sur la detail view. Extrait les champs de la metadata detailviewdefs pour peupler le bean.

---

## Dependances

- **Herite de :** `ViewDetail`
- **Imports :** `modules/Emails/include/DetailView/EmailsNonImportedDetailView.php`

## Exports / Symboles principaux

- `EmailsViewDetailNonImported` — classe vue
  - `preDisplay()` — parse les viewdefs, prepare `EmailsNonImportedDetailView`
  - `display()` — rendu via `dv->process()` et `dv->display()`
  - `getFieldsInViewDefinitions(string $metadataFile)` — extrait les champs des panels (prive)

## Relations cles

- **Appele par :** `EmailsController::action_DisplayDetailView()`

---

## Points d'attention

- `getFieldsInViewDefinitions()` retourne `false` si les panels ne sont pas trouvees — a gerer dans `populateBean()`.
