# codacy.yml (configuration)

**Chemin :** `codacy.yml`
**Configure :** Codacy (plateforme d'analyse statique de code)
**Dernière mise à jour doc :** 2026-05-28

## Ce que ce fichier configure
Définit les chemins à exclure de l'analyse statique Codacy. Il liste les bibliothèques tierces embarquées dans le dépôt afin qu'elles ne soient pas analysées et ne faussent pas les métriques de qualité du code SuiteCRM.

## Paramètres clés
| Paramètre | Valeur | Effet | Preuve |
|---|---|---|---|
| `exclude_paths` | Liste de globs | Exclut les répertoires tiers de l'analyse | lignes 1-22 |

## Chemins exclus (bibliothèques tierces)
- `include/timezone/**`, `include/SuiteGraphs/**`, `include/social/**`
- `include/Smarty/**`, `include/reCaptcha/**`, `include/phpmailer/**`
- `include/Pear/**`, `include/pclzip/**`, `include/nusoap/**`
- `include/HTTP_WebDAV_Server/**`, `include/HTMLPurifier/**`, `include/ytree/**`
- `include/php-sql-parser.php*`, `include/parsecsv.lib.php*`
- `modules/AOS_PDF_Templates/PDF_Lib/**`, `Zend/**`
- `modules/AOD_Index/Lib/**`
- `modules/Users/authentication/SAML2Authenticate/lib/**`
- `install/demoData.en_us.php*`
- `include/tcpdf/**`, `modules/AOR_Charts/lib/**`

## Impacté par / impacte
- Consommé par la plateforme Codacy lors des analyses CI/CD
- La liste est cohérente avec les exclusions de `codeception.dist.yml` et `.codecov.yml`

## Points d'attention
Les exclusions sont alignées entre les trois fichiers de configuration CI (`codacy.yml`, `.codecov.yml`, `codeception.dist.yml`) — toute nouvelle bibliothèque tierce embarquée devrait être ajoutée dans les trois fichiers.
