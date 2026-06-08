# TabController.php

**Chemin :** `modules/MySettings/TabController.php`
**Type :** PHP - Controller / Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gère la configuration des onglets de navigation visibles pour les utilisateurs et les groupes dans SuiteCRM. Détermine si les onglets système sont stockés en base de données, gère un cache de validation, et impose le module Home comme requis.

## Type
controller / service

## Dépendances clés
- `BeanFactory` (Administration) — lecture des paramètres MySettings

## Exports / Symboles principaux
- `TabController` (classe)
  - `$required_modules = ['Home']` — modules toujours visibles
  - `$isCacheValid` (static bool) — état du cache
  - `is_system_tabs_in_db()` — vérifie si les onglets sont en base

## Interactions
- **Appelé par :** gestion des préférences utilisateur et profils de navigation
- **Appelle :** `BeanFactory::newBean('Administration')`
