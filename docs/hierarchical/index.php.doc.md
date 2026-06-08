# index.php

**Chemin :** `index.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée principal de l'application SuiteCRM. Toutes les requêtes HTTP de l'interface utilisateur passent par ce fichier, qui instancie et exécute l'application MVC.

## Responsabilités
- Inclure `include/MVC/preDispatch.php` pour les traitements pré-dispatch (redirections, maintenance)
- Mesurer le temps de démarrage (`$startTime`)
- Charger l'environnement complet via `include/entryPoint.php`
- Instancier `SugarApplication` et démarrer la session
- Appeler `$app->execute()` qui dispatche la requête vers le bon contrôleur/vue

## Dépendances internes
- `include/MVC/preDispatch.php` — logique exécutée avant le dispatch (vérifications rapides)
- `include/entryPoint.php` — bootstrap global (config, DB, session, autoload)
- `include/MVC/SugarApplication.php` — classe principale de l'application (dispatch MVC)

## Exports / Points d'entrée
- **Point d'entrée HTTP principal :** `GET|POST /index.php?module=...&action=...`
- Variable globale `$startTime` disponible pour le profiling

## Notes techniques
- `ob_start()` est appelé après le chargement de l'entryPoint pour bufferiser la sortie et permettre l'envoi d'en-têtes tardifs.
- `SugarApplication::execute()` orchestre le routage MVC complet : authentification, contrôleur, vue, layout.
- Ce fichier est le seul vrai dispatcher web de SuiteCRM 7 ; tout URL publique aboutit ici (via `.htaccess` ou configuration Apache/IIS).
