# index.php

**Chemin :** `modules/UpgradeWizard/index.php`
**Type :** PHP - Point d'entrée du module
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Point d'entrée principal du wizard de mise à jour SuiteCRM. Vérifie les droits administrateur avant d'afficher l'interface de mise à jour.

## Type
view (entrée)

## Dépendances clés
- `is_admin($current_user)` — vérification des droits
- `$current_user`, `$app_strings` (globaux)

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** URL `?module=UpgradeWizard&action=index` (accès administrateur)
- **Appelle :** `is_admin()`, `sugar_die()` si non admin

## Notes
- Accès réservé aux administrateurs uniquement (ligne 48-50 : `sugar_die` si non admin).
