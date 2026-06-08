# CaseUpdatesHook.php

**Chemin :** `modules/AOP_Case_Updates/CaseUpdatesHook.php`
**Type :** PHP - Hook
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Hook gérant les mises à jour des cas support dans le portail AOP. Gère l'affectation automatique d'un utilisateur (via `AOPAssignManager`), la réorganisation des fichiers uploadés, et le traitement des mises à jour soumises depuis le portail ou l'interface interne.

## Type
hook

## Dépendances clés
- `util.php` — utilitaires AOP
- `modules/AOP_Case_Updates/AOPAssignManager.php` — gestion des affectations

## Exports / Symboles principaux
- `CaseUpdatesHook` (classe)
  - `$slug_size = 50` — taille du slug pour les mises à jour
  - `getAssignToUser()` — (private) récupère le prochain utilisateur assigné
  - `arrangeFilesArray()` — (private) réorganise `$_FILES` pour les fichiers joints

## Interactions
- **Appelé par :** hook after_save du module Cases / portail AOP
- **Appelle :** `AOPAssignManager`

## Notes
- Gère l'upload de fichiers joints aux mises à jour de cas.
