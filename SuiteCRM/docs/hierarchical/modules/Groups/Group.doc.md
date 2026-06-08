# Group.php

**Chemin :** `modules/Groups/Group.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant un groupe d'utilisateurs dans SuiteCRM. Hérite de `User` avec les propriétés `status = 'Group'` et `password = ''` pour empêcher toute connexion directe. Utilisé pour les affectations de groupes et la gestion des équipes.

## Type
model

## Dépendances clés
- `User` (classe parente)

## Exports / Symboles principaux
- `Group` (classe) — étend `User`
  - `$status = 'Group'` — empêche le login
  - `$password = ''` — pas de mot de passe
  - `$importable = false`

## Interactions
- **Appelé par :** administration des groupes, SecurityGroups
- **Appelle :** logique `User`

## Notes
- Un groupe est stocké dans la même table `users` avec `status = 'Group'`.
