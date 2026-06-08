# AttachFiles.php

**Chemin :** `modules/EmailTemplates/AttachFiles.php`
**Type :** helper (AJAX)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Point d'entrée pour l'attachement de fichiers à un gabarit email. Appelle dynamiquement une fonction dans `TreeData.php` du module spécifié pour récupérer les données de l'arborescence de fichiers/documents.

## Type

helper (script AJAX/procédural)

---

## Dépendances clés

- `include/JSON.php` — sérialisation JSON
- `$_REQUEST['Module']` — module cible (ex. Documents)
- `$_REQUEST['Function']` — fonction à appeler dans `TreeData.php`
- `$_REQUEST['PARAM_*']` — paramètres passés à la fonction

## Exports / Symboles principaux

- Aucun — script procédural, retourne JSON

## Interactions

- **Appelé par :** éditeur de template email (frontend, sélection de pièces jointes)
- **Appelle :** `TreeData.php` du module cible (statiquement)

## Notes

- Dispatch générique vers n'importe quel module ayant un `TreeData.php`. Point d'attention sécurité : vérifier la validation de `$_REQUEST['Module']` et `$_REQUEST['Function']`.
