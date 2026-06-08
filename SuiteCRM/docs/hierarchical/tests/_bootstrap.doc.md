# _bootstrap.php (bootstrap)

**Chemin :** `tests/_bootstrap.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Point d'entree racine du bootstrap global des suites Codeception. Il initialise l'environnement PHP necessaire a tous les tests en chargeant l'autoloader Composer, les variables d'environnement optionnelles et la verification de version PHP.

## Role technique

Charge `vendor/autoload.php`, definit la constante `sugarEntry` (requise par SuiteCRM pour eviter les acces directs), charge Dotenv depuis `.env.test` si le fichier existe, puis inclut `php_version.php`.

---

## Entrees / Dependances

- **Imports principaux :**
  - `vendor/autoload.php` — autoloader Composer
  - `Dotenv\Dotenv` — chargement conditionnel des variables d'environnement depuis `.env.test`
  - `php_version.php` — verification de la version PHP
- **Variables d'environnement utilisees :** lues depuis `.env.test` si present

## Sorties / Exports

- Aucun export PHP — effet de bord : constante `sugarEntry` definie, autoloader charge
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/_bootstrap.php` (ligne 4)

## Relations cles

- **Appele par :** Codeception au demarrage de n'importe quelle suite
- **Appelle :** `vendor/autoload.php`, `php_version.php`, eventuellement `Dotenv`
- **Position dans le flux global :** premier fichier charge avant tout test

---

## Points d'attention

- La constante `sugarEntry` est requise par SuiteCRM pour distinguer les acces directs des appels legitimes.
- L'objet `$dotenv` est cree mais `load()` n'est jamais appele explicitement dans ce fichier (comportement potentiellement incomplet).
