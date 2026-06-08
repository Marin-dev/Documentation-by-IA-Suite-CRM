# Paths.php

**Chemin :** `lib/Utility/Paths.php`
**Type :** PHP — Service utilitaire
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Centralise les chemins standards de l'application : chemin de la librairie, du projet, de la librairie custom, et du fichier de conteneurs DI de l'API.

## Role technique
Utilise `dirname(__DIR__)` pour remonter depuis `lib/Utility/` vers `lib/`, puis `realpath()` pour les chemins absolus. Le chemin custom remplace la portion projet par `projet/custom`.

---

## Dependances cles
- PHP natif (`dirname`, `realpath`)

## Exports / Symboles principaux
- `Paths` — classe
  - `getProjectPath(): string` — racine du projet
  - `getLibraryPath(): string` — `{project}/lib`
  - `getCustomLibraryPath(): string` — `{project}/custom/lib`
  - `getContainersFilePath(): string` — `{lib}/API/core/containers.php`

- **Consommateurs identifies :**
  - `lib/Robo/Plugin/Commands/CodingStandardCommands.php`
  - `lib/Robo/Plugin/Commands/TestEnvironmentCommands.php`

---

## Points d'attention
- `getCustomLibraryPath()` utilise `realpath()` — retourne `false` si le dossier `custom/lib` n'existe pas.
