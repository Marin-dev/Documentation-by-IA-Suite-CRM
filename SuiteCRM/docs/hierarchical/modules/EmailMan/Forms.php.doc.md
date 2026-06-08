# Forms.php

**Chemin :** `modules/EmailMan/Forms.php`
**Type :** helper

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Utilitaires de formulaire pour le module EmailMan. Fournit la fonction de génération du JavaScript de validation côté client pour le formulaire de configuration du Mass Emailer.

## Type

helper

---

## Dépendances clés

- `$mod_strings` — libellés du module EmailMan
- `$app_strings` — libellés globaux

## Exports / Symboles principaux

- `get_validate_record_js()` — fonction — génère le JavaScript de validation du formulaire config Mass Emailer (vérification champs SMTP, emails par run, etc.)

## Interactions

- **Appelé par :** vues EmailMan (view.config.php)
- **Appelle :** aucun appel externe

## Notes

- Génère du JavaScript inline (heredoc). Pattern ancien SugarCRM.
