# Fichier : PopupDocuments.php

**Chemin :** `modules/Emails/PopupDocuments.php`
**Type :** PHP — Vue popup (selection de documents)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche une popup de selection de documents Sugar (non distants) a joindre a un email. Filtre les documents de type 'Sugar' uniquement (pas les documents distants Google Drive, etc.).

## Role technique

Script procedural. Utilise `DocumentPopupPicker` pour la base, ajoute un filtre `doc_type IN ('', 'Sugar')`, et affiche une vue liste via `ListView` avec XTemplate `PopupDocuments.html`.

---

## Dependances

- **Imports :** `modules/Documents/DocumentPopupPicker.php`
- **Globales :** `$theme`, `$current_mod_strings`, `$app_strings`, `$currentModule`, `$app_list_strings`
- **Utilise :** `BeanFactory::newBean('Documents')`, `ListView`, `XTemplate`

## Exports / Symboles principaux

- Aucun — script d'affichage uniquement

## Relations cles

- **Appele par :** popup de pieces jointes dans le compose view

---

## Points d'attention

- Seuls les documents `doc_type = ''` ou `doc_type = 'Sugar'` sont affichables — les documents distants sont exclus intentionnellement.
