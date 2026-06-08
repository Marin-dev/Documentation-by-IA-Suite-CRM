# TimeDateTest.php (unit-test)

**Chemin :** `tests/unit/phpunit/includes/TimeDateTest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests unitaires de la classe `TimeDate` couvrant la lecture des préférences utilisateur pour les formats de date/heure et les utilitaires de manipulation de dates.

## Type
unit-test

## Dependances cles
- `SuitePHPUnitFrameworkTestCase` — classe de base
- `TimeDate` — classe testée
- `BeanFactory`, `UserPreference`
- Framework : PHPUnit
- Namespace : `SuiteCRM\Tests\Unit\includes`

## Scenarios couverts
- `testget_date_format` : lecture du format date depuis les préférences utilisateur (`datef`)
- `testget_time_format` : lecture du format heure (`timef`)
- `testget_date_time_format` : combinaison date+heure
- `testget_first_day_of_week` : premier jour de semaine depuis les préférences (`fdow`)
- `testget_first_day_of_week_defaultResponse` : défaut = 0 (dimanche) sans utilisateur
- `testmerge_date_time` : concaténation avec espace
- `testsplit_date_time` : découpage en tableau `[date, heure]`
- `testhttpTime` : formatage RFC 2616 d'un timestamp Unix
- `testto_db_time` : extraction de l'heure seule depuis une chaîne date+heure
- `testto_db_date_time` : retour tableau `[date, heure]`
- `testsplitTime` / `testsplitTimeWith24HourDateTime` / `testsplitTimeWithPM` : décomposition d'une chaîne temps

## Notes
- `testto_db_date_time` contient un commentaire indiquant que les préférences utilisateur ne sont pas prises en compte — bug potentiel signalé dans le code.
- Tous les tests créent un utilisateur avec `BeanFactory::newBean('Users')->retrieve('1')` — dépend de l'existence de l'utilisateur avec ID `1` en base.
