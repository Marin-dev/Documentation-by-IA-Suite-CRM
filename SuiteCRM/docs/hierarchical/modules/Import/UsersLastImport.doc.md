# UsersLastImport.php

**Chemin :** `modules/Import/UsersLastImport.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean SuiteCRM représentant la table `users_last_import`. Enregistre les beans importés par utilisateur pour permettre l'annulation (undo) d'un import récent.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)
- `modules/Import/Forms.php`

## Exports / Symboles principaux
- `UsersLastImport` (classe) — étend `SugarBean`
  - `$id` — et autres champs de la table (INCONNU — lecture partielle)

## Interactions
- **Appelé par :** `Importer`, vue `view.undo.php`

## Notes
- Permet la fonctionnalité "annuler le dernier import" en traçant les enregistrements créés.
