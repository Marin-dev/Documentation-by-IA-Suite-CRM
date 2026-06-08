# phpcs.xml

**Chemin :** `phpcs.xml`
**Configure :** `PHP_CodeSniffer (phpcs)`
**Dernière mise à jour doc :** 2026-05-28

---

## Ce que ce fichier configure
Définit le standard de style de code PHP appliqué au projet SuiteCRM. Il hérite du standard PSR-2 en excluant quelques règles de formatage d'appels de fonctions jugées trop contraignantes pour la base de code existante.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| Standard de base | `PSR2` | Applique toutes les règles PSR-2 par défaut |
| Exclusion `PEAR.Functions.FunctionCallSignature` | exclu | Désactive la vérification stricte de l'indentation des appels de fonctions multi-lignes |
| Exclusion `PEAR.Functions.FunctionCallSignature.SpaceAfterCloseBracket` | exclu | Désactive la vérification de l'espace après la parenthèse fermante |
| Exclusion `WordPress.CSRF.NonceVerification.NoNonceVerification` | exclu | Désactive la règle WordPress de vérification des nonces CSRF (non applicable ici) |

## Impacté par / impacte
- Consommé par l'outil `phpcs` (PHP_CodeSniffer) lors des revues de code CI/CD
- Référencé potentiellement dans `.travis.yml` ou les scripts de lint pré-commit
- La dépendance `friendsofphp/php-cs-fixer` dans `composer.json` (dev) est un outil complémentaire mais distinct

## Notes techniques
- L'exclusion de la règle WordPress CSRF suggère que phpcs a été configuré à un moment avec un standard WordPress ; cette exclusion est désormais sans effet avec PSR2 seul mais est conservée par précaution.
- PSR-2 est le standard minimal ; une migration vers PSR-12 (son successeur) n'a pas encore été effectuée.
