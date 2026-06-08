# php_version.php

**Chemin :** `php_version.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Fichier de configuration définissant les constantes de version PHP requises pour SuiteCRM. Utilisé par l'installateur et potentiellement par d'autres vérifications système.

## Responsabilités
- Définir la constante `SUITECRM_PHP_MIN_VERSION` (version PHP minimale absolue : `8.1.0`)
- Définir la constante `SUITECRM_PHP_REC_VERSION` (version PHP recommandée : `8.2.0`)

## Dépendances internes
- Aucune (fichier autonome, pas de `require`)

## Exports / Points d'entrée
- Constante `SUITECRM_PHP_MIN_VERSION` — `'8.1.0'`
- Constante `SUITECRM_PHP_REC_VERSION` — `'8.2.0'`
- Consommateurs identifiés : `install.php` (via `check_php_version()` qui compare à ces constantes)

## Notes techniques
- La garde `sugarEntry` est absente de ce fichier (contrairement à la plupart des fichiers PHP du projet) — il peut donc être inclus tôt dans le processus d'installation avant que `sugarEntry` soit défini.
- Lors d'une mise à jour de version PHP supportée, c'est l'unique fichier à modifier pour ces seuils.
