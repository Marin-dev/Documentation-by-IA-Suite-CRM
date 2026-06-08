# OperatingSystem.php

**Chemin :** `lib/Utility/OperatingSystem.php`
**Type :** PHP — Service utilitaire
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Service utilitaire de detection du systeme d'exploitation et de conversion des chemins. Permet aux commandes Robo d'etre portables entre Linux, macOS, Windows, BSD, Solaris.

## Role technique
Detection via `php_uname('s')` avec `stristr()`. Methode `toOsPath()` normalise les separateurs de chemin (`/` vs `\`), gere les espaces echappes et les tabulations.

---

## Dependances cles
- PHP natif (`php_uname()`, `DIRECTORY_SEPARATOR`)

## Exports / Symboles principaux
- `OperatingSystem` — classe
  - `isOsLinux/isOsMacOSX/isOsWindows/isOsBSD/isOsSolaris/isOsUnknown(): bool`
  - `toOsPath(string $path, string $ds = DIRECTORY_SEPARATOR): string`

- **Consommateurs identifies :**
  - `lib/Robo/Plugin/Commands/BuildCommands.php`
  - `lib/Robo/Plugin/Commands/CodeCoverageCommands.php`
  - `lib/Robo/Plugin/Commands/TestEnvironmentCommands.php`

---

## Points d'attention
- `isOsUnknown()` verifie l'egalite exacte avec `'Unknown'` (ligne 83) — peu robuste.
- `toOsPath()` sur Unix ajoute `\ ` (backslash-espace) pour les chemins avec espaces.
