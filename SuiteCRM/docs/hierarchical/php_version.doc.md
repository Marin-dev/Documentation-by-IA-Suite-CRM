# php_version.php

**Chemin :** `php_version.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Déclare les constantes de version PHP minimale et recommandée requises pour SuiteCRM. Ces constantes sont utilisées lors de l'installation et dans les vérifications de compatibilité.

**Type :** config / helper

## Rôle technique

Définit deux constantes PHP utilisées pour valider la version PHP de l'environnement hôte. Requiert que `sugarEntry` soit défini (protection contre l'appel direct).

---

## Dépendances clés

- **Aucune dépendance**
- **Sécurité :** bloque si `sugarEntry` non défini (ligne 2)

## Exports / Constantes définies

| Constante | Valeur | Rôle |
|---|---|---|
| `SUITECRM_PHP_MIN_VERSION` | `'8.1.0'` | Version PHP absolument minimale pour l'installation |
| `SUITECRM_PHP_REC_VERSION` | `'8.2.0'` | Version PHP recommandée |

## Relations clés

- **Appelé par :** `install.php` (ligne 84 : `require_once('sugar_version.php')` puis `require_once('suitecrm_version.php')`) — INCONNU si chargé directement ailleurs
- **Consommé par :** `check_php_version()` dans `install/install_utils.php` qui compare `PHP_VERSION` avec ces constantes

---

## Points d'attention

- La valeur `8.1.0` est la version minimale absolue supportée (PHP 8.1 étant requis dans `composer.json`).
- Ce fichier devra être mis à jour lors de chaque changement de version PHP supportée.
