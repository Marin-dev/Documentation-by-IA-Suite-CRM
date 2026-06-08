# CliLoggerHandler.php

**Chemin :** `lib/Log/CliLoggerHandler.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Handler Monolog pour l'affichage colore des logs en ligne de commande (CLI). Ecrit sur `php://stderr`.

## Role technique
Etend `Monolog\Handler\StreamHandler`. Oriente la sortie vers `stderr`. Injecte `CliLoggerFormatter` comme formateur par defaut dans le constructeur. Niveau minimum configurable (defaut : DEBUG).

---

## Dependances cles
- `Monolog\Handler\StreamHandler` — handler de flux parent
- `Monolog\Logger` — constante `DEBUG`
- `SuiteCRM\Log\CliLoggerFormatter` — formateur couleur

## Exports / Symboles principaux
- `CliLoggerHandler` — classe handler Monolog CLI

- **Consommateurs identifies :**
  - `lib/Search/Index/AbstractIndexer.php` (ligne 309)
  - `lib/Search/Index/Documentify/SearchDefsDocumentifier.php` (ligne 77)

## Relations cles
- **Appele par :** `AbstractIndexer::setupLogger()`, `SearchDefsDocumentifier`
- **Appelle :** `CliLoggerFormatter`
- **Position dans le flux global :** handler de log pour les operations d'indexation en CLI

---

## Points d'attention
- Ecriture sur `stderr` : ne polluera pas `stdout` dans les scripts CLI.
- Necessite un contexte CLI avec `sugarEntry` defini (ligne 43).
