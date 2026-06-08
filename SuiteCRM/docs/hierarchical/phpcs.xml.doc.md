# phpcs.xml (configuration)

**Chemin :** `phpcs.xml`
**Configure :** `PHP_CodeSniffer (phpcs) — analyse statique de style de code`
**Dernière mise à jour doc :** 2026-05-30

## Rôle

Fichier de configuration de PHP_CodeSniffer définissant les règles de style de code appliquées au projet SuiteCRM. Utilisé en développement et dans le CI pour vérifier la conformité au standard PSR-2.

**Type :** config (outillage développeur)

## Ce que ce fichier configure

Applique le ruleset PSR-2 avec trois exclusions spécifiques liées à la signature des appels de fonctions.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| Ruleset de base | `PSR2` | Standard PHP PSR-2 complet |
| Exclusion 1 | `PEAR.Functions.FunctionCallSignature` | Désactive la vérification de signature des appels |
| Exclusion 2 | `PEAR.Functions.FunctionCallSignature.SpaceAfterCloseBracket` | Désactive la vérification d'espace après `)` |
| Exclusion 3 | `WordPress.CSRF.NonceVerification.NoNonceVerification` | Désactive la vérification CSRF (règle WordPress non applicable) |

## Impacté par / impacte

- Utilisé par `vendor/bin/phpcs` en ligne de commande
- Référencé potentiellement dans les hooks git pre-commit
- Complété par `friendsofphp/php-cs-fixer` (configuré séparément dans `.php-cs-fixer.php` — INCONNU si présent)

## Points d'attention

- La présence de la règle `WordPress.CSRF` suggère qu'un ancien sniff WordPress était installé — peut être une règle obsolète.
- Les exclusions sur `FunctionCallSignature` sont probablement là pour tolérer le style de code legacy du codebase SugarCRM.
