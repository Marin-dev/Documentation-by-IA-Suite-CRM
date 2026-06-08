# OsHelper.php

## Rôle
Utilitaire statique permettant de détecter le système d'exploitation courant (Windows, Linux, macOS) à partir de la constante PHP `PHP_OS`.

## Responsabilités
- Exposer trois constantes OS : `OS_WINDOWS`, `OS_LINUX`, `OS_OSX`
- Fournir `getOS()` qui retourne l'une de ces constantes selon `PHP_OS`
- Lever une `\RuntimeException` si l'OS ne peut pas être déterminé

## Dépendances internes
Aucune dépendance interne au projet.

## Exports / Points d'entrée
- `OsHelper` (classe statique) — utilitaire
- `OS_WINDOWS`, `OS_LINUX`, `OS_OSX` (constantes publiques)
- `getOS(): string` (méthode statique) — retourne l'une des trois constantes

## Notes techniques
- `#[\AllowDynamicProperties]`
- Détection basée sur `stristr(PHP_OS, ...)` : recherche insensible à la casse des chaînes `'DAR'` (Darwin/macOS), `'WIN'`, `'LINUX'`
- Usage dans le projet : INCONNU — probablement utilisé pour des chemins de fichiers ou des commandes spécifiques à l'OS dans le contexte de l'API V8
