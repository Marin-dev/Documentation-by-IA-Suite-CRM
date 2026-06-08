# composer.json (configuration)

**Chemin :** `composer.json`
**Configure :** `Composer — gestionnaire de dépendances PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Ce que ce fichier configure
Manifeste Composer du projet SuiteCRM. Déclare toutes les dépendances PHP (production et développement), la stratégie d'autoloading PSR-4, les scripts post-installation, et la configuration de fusion des extensions via `wikimedia/composer-merge-plugin`.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `name` | `suitecrm/suitecrm` | Identifiant Packagist |
| `type` | `project` | Type projet (pas une librairie) |
| `license` | `GPL-3.0` | Licence |
| `config.vendor-dir` | `vendor` | Répertoire des dépendances |
| `config.platform.php` | `8.1.0` | Version PHP cible pour la résolution des dépendances |
| `config.optimize-autoloader` | `true` | Génère un autoloader optimisé en production |
| `minimum-stability` | `dev` | Accepte les paquets dev si nécessaire |

**Dépendances de production notables :**

| Paquet | Version | Usage |
|---|---|---|
| `php` | `^8.1` | Version PHP minimale |
| `elasticsearch/elasticsearch` | `^7.13` | Recherche full-text (AOD) |
| `league/oauth2-server` | `^8.5` | Serveur OAuth2 API V8 |
| `onelogin/php-saml` | `^4` | Authentification SAML2 SSO |
| `phpmailer/phpmailer` | `^6.0` | Envoi d'emails |
| `slim/slim` | `^3.8` | Framework HTTP pour API V8 |
| `smarty/smarty` | `^4` | Moteur de templates |
| `tecnickcom/tcpdf` | `^6.10` | Génération PDF |
| `tinymce/tinymce` | `^8` | Éditeur WYSIWYG |
| `monolog/monolog` | `^3` | Logging |
| `symfony/validator` | `^6.4` | Validation |
| `zbateson/mail-mime-parser` | `^2.4` | Parsing des emails MIME |
| `zf1s/zend-oauth` | `^1.15` | OAuth legacy (Zend) |

**Dépendances de développement notables :**

| Paquet | Usage |
|---|---|
| `codeception/codeception` `^5.2` | Tests fonctionnels et acceptance |
| `phpunit/phpunit` `^10.5` | Tests unitaires |
| `fakerphp/faker` | Génération de données de test |
| `mockery/mockery` | Mocks PHPUnit |
| `vlucas/phpdotenv` | Chargement `.env.test` |

**Autoloading :**
- `autoload.files` : `deprecated.php` — chargé automatiquement à chaque bootstrap
- `autoload.psr-4` :
  - `SuiteCRM\` → `lib/` et `include/`
  - `SuiteCRM\Custom\` → `custom/lib`
  - `SuiteCRM\Modules\` → `modules/`
  - `classmap` → `Api/`

## Impacté par / impacte
- `wikimedia/composer-merge-plugin` fusionne `composer.ext.json` et `custom/Extension/application/Ext/Composer/*/*.json` pour les extensions
- `Google\Task\Composer::cleanup` s'exécute post-install pour nettoyer les services Google inutilisés (seul `Calendar` est conservé)
- Impacte directement `deprecated.php` (chargé via `autoload.files`)

## Notes techniques
- La combinaison `minimum-stability: dev` + `prefer-stable: true` permet d'installer des paquets stables tout en débloquant les paquets dev si nécessaire.
- La dépendance `ext-imap` est seulement suggérée (`suggest`) — non obligatoire mais nécessaire pour le module Emails.
- L'extension `javanile/php-imap2` est un wrapper IMAP alternatif à l'extension native.
