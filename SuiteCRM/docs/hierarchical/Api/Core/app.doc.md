# 📄 app.php

**Chemin :** `Api/Core/app.php`
**Type :** `PHP`
**Catégorie :** entrypoint
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel

Point d'entrée bootstrap de l'API SuiteCRM. Ce fichier initialise l'environnement HTTP (headers CORS), charge le noyau SuiteCRM (`entryPoint.php`), instancie l'application Slim avec son conteneur DI configuré, et enregistre toutes les routes. Il constitue la séquence d'amorçage complète de l'API REST.

## ⚙️ Rôle technique

Script d'initialisation séquentiel (non une classe) :
1. Positionne les headers CORS permissifs (`Access-Control-Allow-Origin: *`, méthodes, headers).
2. Définit la constante `sugarEntry` nécessaire à SuiteCRM.
3. Gère la compatibilité php-fpm : recopie `REDIRECT_HTTP_AUTHORIZATION` vers `HTTP_AUTHORIZATION` si nécessaire.
4. Change le répertoire courant vers la racine SuiteCRM via `chdir(__DIR__ . '/../../')`.
5. Inclut `include/entryPoint.php` (bootstrap SuiteCRM, définit `$GLOBALS['BASE_DIR']`).
6. Instancie `\Slim\App` en passant le conteneur créé par `ContainerLoader::configure()`.
7. Instancie `RouteLoader` et appelle `configureRoutes($app)`.

---

## 📥 Entrées / Dépendances

- **Imports principaux :**
  - `include/entryPoint.php` — bootstrap SuiteCRM, définit BASE_DIR, autoloader, DB, etc.
  - `Api\Core\Loader\ContainerLoader` — configure le conteneur DI Slim
  - `Api\Core\Loader\RouteLoader` — enregistre les routes dans Slim
  - `Slim\App` — framework HTTP
- **Variables d'environnement / serveur utilisées :**
  - `$_SERVER['HTTP_AUTHORIZATION']` — token d'authentification HTTP
  - `$_SERVER['REDIRECT_HTTP_AUTHORIZATION']` — valeur alternative pour php-fpm

## 📤 Sorties / Exports

Ce fichier ne déclare aucun symbole exportable. Il produit l'effet de bord de configurer l'application Slim prête à traiter les requêtes. La variable `$app` est disponible dans le scope global après inclusion.

**Consommateurs identifiés dans le repo :**
- INCONNU — ce fichier est probablement inclus par un point d'entrée HTTP (`index.php` ou équivalent dans `Api/`) non analysé ici.

## 🔗 Relations clés

- **Appelé par :** INCONNU (probablement un `index.php` ou `entryPoint.php` de l'API V8)
- **Appelle :** `ContainerLoader::configure()`, `RouteLoader::configureRoutes()`, `include/entryPoint.php`
- **Position dans le flux global :** premier fichier exécuté lors d'une requête API, orchestre toute la séquence de bootstrap

---

## 💡 Points d'attention

- **CORS permissif :** `Access-Control-Allow-Origin: *` est configuré en dur — dangereux en production, autorise toute origine.
- Le commentaire `// Swagger needs this, but should remove - CORS` indique que ce header est un vestige temporaire non encore supprimé.
- `chdir(__DIR__ . '/../../')` modifie le répertoire de travail globalement — tous les chemins relatifs utilisés ensuite (notamment dans `CustomLoader`) seront relatifs à la racine SuiteCRM.
- La constante `sugarEntry` doit être définie avant d'inclure `entryPoint.php` pour éviter des erreurs d'accès direct.
- La gestion `REDIRECT_HTTP_AUTHORIZATION` est spécifique à Apache + php-fpm avec règles `.htaccess` de réécriture.
