# EditView.php

**Chemin :** `modules/EmailTemplates/EditView.php`
**Type :** vue

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Vue d'édition d'un gabarit email. Permet de créer ou modifier un template avec l'éditeur HTML, les macros de variables et la gestion des pièces jointes.

## Type

vue

---

## Dépendances clés

- `EmailTemplate` (modèle)
- `EmailTemplateFormBase` — gestion des pièces jointes
- `$mod_strings`

## Exports / Symboles principaux

- Aucun — script de rendu de vue

## Interactions

- **Appelé par :** dispatcher MVC (action EditView)

## Notes

- Intègre un éditeur HTML riche (TinyMCE probable).
