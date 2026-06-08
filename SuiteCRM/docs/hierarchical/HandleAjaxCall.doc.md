# HandleAjaxCall.php

**Chemin :** `HandleAjaxCall.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée AJAX réservé aux administrateurs pour invoquer dynamiquement des méthodes du `PackageController`. Utilisé par l'interface d'administration pour les opérations de gestion des packages/modules installés.

**Type :** entrypoint

## Rôle technique

Charge l'environnement SuiteCRM et le `PackageController`, vérifie que l'utilisateur courant est administrateur, puis appelle dynamiquement la méthode demandée via `$_REQUEST['method']` par réflexion PHP (`method_exists` + appel dynamique).

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation complète de SuiteCRM
  - `ModuleInstall/PackageManager/PackageController.php` — contrôleur des packages installables
- **Paramètres d'entrée ($_REQUEST) :**
  - `method` — nom de la méthode à appeler sur `PackageController`
- **Sécurité :** vérifie `is_admin($GLOBALS['current_user'])` avant tout appel

## Sorties / Comportement

- `echo` du retour de la méthode appelée sur `PackageController`
- Si la méthode n'existe pas : affiche `'no method'`
- Aucune réponse structurée (JSON/XML) — retour brut

## Relations clés

- **Appelé par :** requêtes AJAX depuis les pages d'administration de packages (ModuleInstall)
- **Appelle :** `PackageController::{$requestedMethod}()`

---

## Points d'attention

- `sugar_cleanup()` est commenté (ligne 60) — potentielle fuite de ressources.
- L'invocation dynamique de méthode via `$_REQUEST['method']` sans whitelist est un risque de sécurité atténué uniquement par la vérification admin — toute méthode publique de `PackageController` est accessible.
- Réservé aux administrateurs uniquement (`is_admin` obligatoire, ligne 49).
