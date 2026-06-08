# Menu.php

**Chemin :** `modules/MailMerge/Menu.php`
**Type :** PHP - Configuration (menu)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le menu du module MailMerge avec 2 entrées : Nouvelle fusion et Télécharger un template.

## Type
config

## Dépendances clés
- `$mod_strings` — LNK_NEW_MAILMERGE, LNK_UPLOAD_TEMPLATE

## Exports / Symboles principaux
- `$module_menu` — 2 entrées
  - "Nouvelle fusion" → `index.php?module=MailMerge&action=index&reset=true`
  - "Télécharger template" → `index.php?module=Documents&action=EditView&return_module=MailMerge`

## Interactions
- **Appelé par :** framework SugarCRM
- **Appelle :** rien

## Notes
- L'upload de template redirige vers le module Documents.
