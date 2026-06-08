# codeception.dist.yml (configuration)

**Chemin :** `codeception.dist.yml`
**Configure :** `Codeception — framework de tests automatisés`
**Dernière mise à jour doc :** 2026-05-28

---

## Ce que ce fichier configure
Configuration principale de Codeception pour SuiteCRM. Définit les répertoires de tests, les paramètres de couverture de code et les exclusions de bibliothèques tierces.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `actor` | `Tester` | Nom de la classe acteur générée |
| `paths.tests` | `tests` | Répertoire racine des tests |
| `paths.log` | `tests/_output` | Logs et rapports |
| `paths.data` | `tests/_data` | Fixtures et données de test |
| `paths.support` | `tests/_support` | Helpers et page objects |
| `settings.bootstrap` | `_bootstrap.php` | Fichier de démarrage des suites |
| `settings.memory_limit` | `16000M` | Limite mémoire PHP pendant les tests (16 Go) |
| `extensions.enabled` | `RunFailed` | Rejoue automatiquement les tests échoués |
| `coverage.enabled` | `true` | Active la génération de couverture |
| `coverage.low_limit` | `50` | Seuil bas (affichage rouge) |
| `coverage.high_limit` | `90` | Seuil haut (affichage vert) |
| `params` | `env`, `.env.test` | Sources des variables d'environnement |

**Répertoires inclus dans la couverture :**
`ModuleInstall/`, `data/`, `include/`, `install/`, `jssource/`, `lib/`, `metadata/`, `modules/`, `service/`, `soap/`, `themes/`

**Répertoires exclus de la couverture :**
Bibliothèques tierces embarquées (Smarty, nusoap, HTMLPurifier, tcpdf, etc.) — mêmes exclusions que `.codecov.yml`

## Impacté par / impacte
- Consommé par `./vendor/bin/codecept` lors des commandes `run`, `build`, `coverage`
- Lit les variables d'environnement depuis `.env.test` (copié depuis `.env.dist`)
- Référencé dans `.travis.yml` pour les commandes `codecept build` et `codecept run`

## Notes techniques
- La limite mémoire de 16 Go est très élevée — reflète la complexité des tests d'intégration SuiteCRM.
- `coverage.remote: false` signifie que la couverture est calculée localement (pas via xdebug distant).
