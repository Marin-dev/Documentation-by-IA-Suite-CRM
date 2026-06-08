# CliLoggerFormatter.php

**Chemin :** `lib/Log/CliLoggerFormatter.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Formateur Monolog specialise pour la sortie en couleurs dans un terminal. Colore les lignes de log selon leur niveau de severite et formate l'heure, le code de niveau et le message.

## Role technique
Implementer `Monolog\Formatter\FormatterInterface`. Utilise les sequences d'echappement ANSI pour colorer la sortie (`\e[Nm`). Format de sortie : `[BOLD][code][/BOLD][HH:MM:SS] message`. Chaque niveau Monolog (DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL, EMERGENCY) a sa propre couleur et son symbole (`@`, `=`, `?`, `*`, `!`, `!`, `!`).

---

## Dependances cles
- `Monolog\Formatter\FormatterInterface` — interface a implementer
- `Monolog\Logger` — constantes de niveau (DEBUG=100, INFO=200, etc.)
- `Monolog\LogRecord` — objet de record depuis Monolog 3

## Exports / Symboles principaux
- `CliLoggerFormatter` — classe formatter
  - `format(array|LogRecord $record): mixed`
  - `formatBatch(array $records): mixed`

- **Consommateurs identifies :**
  - `lib/Log/CliLoggerHandler.php` (ligne 67 : `new CliLoggerFormatter()`)

## Relations cles
- **Appele par :** `CliLoggerHandler`
- **Appelle :** rien d'externe
- **Position dans le flux global :** couche de presentation du log CLI

---

## Points d'attention
- Requiert un terminal ANSI compatible. Les couleurs ne s'affichent pas dans un contexte non-TTY.
- `$alwaysColourLine = true` (ligne 63) : toutes les lignes sont colorees, meme en-dessous de WARNING.
- `formatBatch()` retourne le dernier record formate seulement (ligne 98) — comportement potentiellement incorrect pour les batchs.
