# index.php

**Chemin :** `modules/MailMerge/index.php`
**Type :** PHP - Point d'entrée du module
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Point d'entrée principal du module MailMerge. Dispatche vers les différentes étapes du wizard de fusion selon `$_REQUEST['step']`.

## Type
view (entrée)

## Dépendances clés
- `$theme`, `$mod_strings`, `$current_language` (globaux)
- `$_REQUEST['step']`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** `DetailView.php`, `EditView.php`, actions MailMerge
- **Appelle :** scripts Step1-Step5 selon l'étape

## Notes
- Centrale de dispatch : tous les fichiers *View.php délèguent vers index.php.
