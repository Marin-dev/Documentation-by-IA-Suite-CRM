# codacy.yml (configuration)

**Chemin :** `codacy.yml`
**Configure :** `Codacy — service d'analyse statique de code`
**Dernière mise à jour doc :** 2026-05-30

## Rôle

Fichier de configuration Codacy définissant les chemins exclus de l'analyse statique de code. Permet de concentrer l'analyse sur le code applicatif SuiteCRM en ignorant les bibliothèques tierces et le code legacy.

**Type :** config (qualité de code)

## Ce que ce fichier configure

Déclare une liste de chemins exclus (`exclude_paths`) pour que Codacy ne les analyse pas lors des checks de qualité.

## Chemins exclus

Identiques à `.codecov.yml` — bibliothèques tierces incluses directement dans le dépôt :

- `include/timezone/**`, `include/SuiteGraphs/**`, `include/social/**`
- `include/Smarty/**`, `include/reCaptcha/**`, `include/phpmailer/**`
- `include/Pear/**`, `include/pclzip/**`, `include/nusoap/**`
- `include/HTTP_WebDAV_Server/**`, `include/HTMLPurifier/**`, `include/ytree/**`
- `include/php-sql-parser.php`, `include/parsecsv.lib.php`
- `modules/AOS_PDF_Templates/PDF_Lib/**`
- `Zend/**`
- `modules/AOD_Index/Lib/**`
- `modules/Users/authentication/SAML2Authenticate/lib/**`
- `install/demoData.en_us.php`
- `include/tcpdf/**`
- `modules/AOR_Charts/lib/**`

## Impacté par / impacte

- Consommé par le service Codacy lors des analyses de PR/push
- Résultats visibles sur `codacy.com` dans le dashboard du projet

## Points d'attention

- Les chemins exclus sont identiques à ceux de `.codecov.yml` — cohérence entre les deux outils.
- Les bibliothèques exclues sont des copies vendorisées localement (pré-Composer legacy) — les nouvelles dépendances sont dans `vendor/` et exclues implicitement.
