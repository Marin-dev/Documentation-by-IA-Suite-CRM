# codeception.dist.yml (configuration)

**Chemin :** `codeception.dist.yml`
**Configure :** `Codeception — framework de tests automatisés`
**Dernière mise à jour doc :** 2026-05-30

## Rôle

Fichier de configuration principal de Codeception pour SuiteCRM. Définit la structure des répertoires de tests, les paramètres d'exécution, la couverture de code, et les chemins inclus/exclus de l'analyse.

**Type :** config (tests)

## Ce que ce fichier configure

Configure Codeception avec les chemins des suites de tests, la mémoire maximale, le bootstrap, la couverture de code, et les sources de paramètres d'environnement.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `actor` | `Tester` | Nom de l'acteur de test généré |
| `paths.tests` | `tests` | Répertoire racine des tests |
| `paths.log` | `tests/_output` | Répertoire de sortie (rapports, captures) |
| `paths.data` | `tests/_data` | Fixtures et données SQL |
| `paths.support` | `tests/_support` | Helpers et modules custom |
| `paths.envs` | `tests/_envs` | Configurations par environnement |
| `settings.bootstrap` | `_bootstrap.php` | Fichier de bootstrap exécuté avant les tests |
| `settings.memory_limit` | `16000M` | 16 Go de mémoire pour les tests |
| `coverage.enabled` | `true` | Couverture de code activée |
| `coverage.low_limit` | `50` | Seuil bas de couverture : 50% |
| `coverage.high_limit` | `90` | Seuil haut de couverture : 90% |

## Sources de paramètres

| Source | Rôle |
|---|---|
| `env` | Variables d'environnement du système |
| `.env.test` | Fichier `.env.test` (copie locale de `.env.dist`) |

## Chemins inclus dans la couverture

`ModuleInstall/*.php`, `data/*.php`, `include/*.php`, `install/*.php`, `jssource/*.php`, `lib/*.php`, `metadata/*.php`, `modules/*.php`, `service/*.php`, `soap/*.php`, `themes/*.php`

## Chemins exclus de la couverture

Identiques à `.codecov.yml` — bibliothèques tierces vendorisées localement.

## Extension activée

`Codeception\Extension\RunFailed` — relance automatiquement les tests échoués.

## Impacté par / impacte

- Consommé par `vendor/bin/codecept run` (CLI)
- Utilise `.env.test` comme source de configuration (copie de `.env.dist`)
- Génère les rapports dans `tests/_output/` (dont `coverage.xml` pour Codecov)

## Points d'attention

- La limite mémoire de `16000M` (16 Go) est très élevée — nécessite un environnement robuste pour les tests d'acceptance complets.
- La présence de `RunFailed` comme extension par défaut peut masquer des tests systématiquement en échec.
- Les fichiers `.env.test` ne sont pas versionnés (`.gitignore`) — leur absence bloquera les tests nécessitant des paramètres d'environnement.
