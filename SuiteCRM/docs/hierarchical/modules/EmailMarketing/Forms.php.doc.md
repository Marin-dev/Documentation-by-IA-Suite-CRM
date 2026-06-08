# Forms.php

**Chemin :** `modules/EmailMarketing/Forms.php`
**Type :** helper

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Utilitaires de formulaire pour le module EmailMarketing. Fournit la fonction de validation JavaScript côté client pour les formulaires de message marketing (champs requis : nom, message, etc.).

## Type

helper

---

## Dépendances clés

- `$mod_strings`
- `$app_strings`

## Exports / Symboles principaux

- `get_validate_record_js()` — fonction — génère le JavaScript de validation du formulaire EmailMarketing

## Interactions

- **Appelé par :** vues EmailMarketing (EditView, DetailView)

## Notes

- Pattern identique à `EmailMan/Forms.php`.
