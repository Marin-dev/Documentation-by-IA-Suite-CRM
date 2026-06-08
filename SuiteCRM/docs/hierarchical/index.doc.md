# index.php

**Chemin :** `index.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée principal de l'application SuiteCRM. Toutes les requêtes HTTP vers l'interface utilisateur passent par ce fichier, qui orchestre le dispatch vers les contrôleurs et vues appropriés.

**Type :** entrypoint (principal)

## Rôle technique

Définit `sugarEntry`, exécute le pré-dispatch (`preDispatch.php`), charge l'environnement complet (`entryPoint.php`), instancie `SugarApplication` et appelle `startSession()` puis `execute()`. C'est la colonne vertébrale du pattern MVC de SuiteCRM.

---

## Dépendances clés

- **Imports principaux :**
  - `include/MVC/preDispatch.php` — hooks de pré-dispatch (avant chargement de l'env)
  - `include/entryPoint.php` — initialisation complète (DB, config, auth, modules…)
  - `include/MVC/SugarApplication.php` — classe principale de l'application MVC

## Sorties / Comportement

- Démarre la session utilisateur via `$app->startSession()`
- Dispatche la requête vers le contrôleur/vue approprié via `$app->execute()`
- Variable `$startTime` capturée pour mesurer le temps de réponse (ligne 46)

## Relations clés

- **Appelé par :** toutes les requêtes HTTP vers l'interface SuiteCRM (`module=...&action=...`)
- **Appelle :** `SugarApplication::startSession()`, `SugarApplication::execute()`
- **Position dans le flux :** premier fichier PHP exécuté pour toute navigation dans le CRM

---

## Points d'attention

- `preDispatch.php` est inclus **avant** `entryPoint.php` — toute logique dans ce fichier s'exécute sans environnement SuiteCRM complet.
- `ob_start()` est appelé ligne 48 mais le flush est géré dans `SugarApplication::execute()`.
- Ce fichier est le target principal de la configuration Apache/Nginx (`DirectoryIndex`).
