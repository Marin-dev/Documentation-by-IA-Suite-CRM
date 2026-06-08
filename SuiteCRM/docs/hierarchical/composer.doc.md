# composer.json (configuration)

**Chemin :** `composer.json`
**Configure :** `Gestionnaire de dépendances PHP Composer`
**Dernière mise à jour doc :** 2026-05-30

## Rôle

Fichier de définition du projet Composer pour SuiteCRM. Déclare toutes les dépendances PHP de production et de développement, les namespaces PSR-4, les scripts post-installation, et les plugins Composer utilisés.

**Type :** config

## Ce que ce fichier configure

Définit le projet `suitecrm/suitecrm` avec ses dépendances, la plateforme cible PHP 8.1, l'autoloading PSR-4 sur les namespaces `SuiteCRM\`, `SuiteCRM\Custom\`, `SuiteCRM\Modules\`, et un classmap pour `Api/`. Inclut également les extensions Composer via `wikimedia/composer-merge-plugin`.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `platform.php` | `8.1.0` | Force Composer à résoudre pour PHP 8.1 |
| `vendor-dir` | `vendor` | Répertoire d'installation des dépendances |
| `optimize-autoloader` | `true` | Génère un autoloader optimisé (classmap) |
| `minimum-stability` | `dev` | Autorise les packages en développement |
| `prefer-stable` | `true` | Préfère les versions stables malgré `dev` |

## Dépendances de production principales

| Package | Version | Rôle |
|---|---|---|
| `php` | `^8.1` | Version minimale requise |
| `elasticsearch/elasticsearch` | `^7.13` | Client Elasticsearch (recherche plein texte) |
| `ezyang/htmlpurifier` | `^4.10` | Purification HTML (sécurité XSS) |
| `google/apiclient` | `^2.18` | Intégration Google Calendar |
| `league/oauth2-server` | `^8.5` | Serveur OAuth2 (API V8) |
| `monolog/monolog` | `^3` | Journalisation |
| `onelogin/php-saml` | `^4` | Authentification SAML2 (SSO) |
| `phpmailer/phpmailer` | `^6.0` | Envoi d'emails |
| `slim/slim` | `^3.8` | Framework micro pour l'API REST |
| `smarty/smarty` | `^4` | Moteur de templates (vues) |
| `tecnickcom/tcpdf` | `^6.10` | Génération de PDF |
| `wikimedia/composer-merge-plugin` | `^2.0` | Merge de fichiers composer.ext.json et extensions custom |

## Autoloading

| Namespace | Répertoires |
|---|---|
| `SuiteCRM\` | `lib/`, `include/` |
| `SuiteCRM\Custom\` | `custom/lib` |
| `SuiteCRM\Modules\` | `modules/` |
| Classmap | `Api/` |
| Fichier chargé automatiquement | `deprecated.php` |

## Dépendances de développement principales

| Package | Rôle |
|---|---|
| `codeception/codeception ^5.2` | Framework de tests (acceptance, API, install) |
| `phpunit/phpunit ^10.5` | Tests unitaires |
| `fakerphp/faker` | Génération de données fictives pour les tests |
| `vlucas/phpdotenv` | Chargement du `.env.test` pour les tests |
| `friendsofphp/php-cs-fixer` | Formatage du code |

## Impacté par / impacte

- Le fichier `composer.ext.json` et les fichiers sous `custom/Extension/application/Ext/Composer/*/*.json` sont fusionnés via le merge-plugin
- Le script `post-install-cmd` exécute `Google\Task\Composer::cleanup` pour alléger le package Google API
- `deprecated.php` est chargé automatiquement à chaque requête (fichier de compatibilité)

## Points d'attention

- `minimum-stability: dev` peut introduire des packages instables — atténué par `prefer-stable: true`.
- L'extension `ext-imap` est suggérée mais non requise (`suggest`) ; son absence désactive le module Emails.
- `autoload.files` charge `deprecated.php` à chaque boot Composer — impact minimal sur les performances mais à connaître.
