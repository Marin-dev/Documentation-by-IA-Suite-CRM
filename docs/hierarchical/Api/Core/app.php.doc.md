# app.php

**Chemin :** `Api/Core/app.php`
**Type :** PHP (point d'entree bootstrap)
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Point d'entree principal de l'API SuiteCRM. Initialise l'environnement PHP, configure les en-tetes CORS, charge le bootstrap SuiteCRM, construit l'application Slim avec son conteneur DI et enregistre toutes les routes.

## Responsabilites

- Emettre les en-tetes CORS autorisant toutes les origines et methodes HTTP (`Access-Control-Allow-*`)
- Definir la constante `sugarEntry` requise par SuiteCRM pour autoriser l'execution
- Corriger la transmission de l'en-tete `Authorization` en environnement PHP-FPM/Apache (`REDIRECT_HTTP_AUTHORIZATION`)
- Changer le repertoire de travail courant vers la racine SuiteCRM (`chdir`)
- Charger le bootstrap SuiteCRM via `include/entryPoint.php` (qui definit `BASE_DIR` et initialise le framework)
- Construire le conteneur DI Slim via `ContainerLoader::configure()`
- Enregistrer toutes les routes via `RouteLoader::configureRoutes($app)`

## Dependances internes

- `Api\Core\Loader\ContainerLoader` — construit le conteneur Slim DI
- `Api\Core\Loader\RouteLoader` — enregistre les routes dans l'application Slim
- `include/entryPoint.php` (chemin relatif a la racine SuiteCRM) — bootstrap global SuiteCRM

## Exports / Points d'entree

- Variable `$app` — instance de `\Slim\App` configuree, exposee dans le scope global pour etre utilisee par le fichier appelant (ex: `index.php` ou equivalent)
- Ce fichier est inclus par le point d'entree HTTP (INCONNU : chemin exact du fichier qui fait `require 'app.php'`)

## Notes techniques

- CORS ouvert (`Access-Control-Allow-Origin: *`) — commentaire "Swagger needs this" (ligne 2) ; a restreindre en production.
- Le `chdir(__DIR__ . '/../../')` (ligne 20) positionne le CWD deux niveaux au-dessus de `Api/Core/`, soit la racine SuiteCRM — necessaire pour que les `require_once` relatifs de SuiteCRM fonctionnent correctement.
- `RouteLoader` est instancie (non statique) contrairement a `ContainerLoader` — coherence avec le design des deux classes.
- Le fichier ne contient pas d'appel a `$app->run()` — le fichier appelant est responsable du demarrage effectif de Slim. INCONNU : localisation du `$app->run()`.
