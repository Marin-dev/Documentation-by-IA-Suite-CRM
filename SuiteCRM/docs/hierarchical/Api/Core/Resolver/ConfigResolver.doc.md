# 📄 ConfigResolver.php

**Chemin :** `Api/Core/Resolver/ConfigResolver.php`
**Type :** `PHP`
**Catégorie :** helper / resolver
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel

Utilitaire bas niveau chargé de résoudre et charger les fichiers de configuration PHP. Il prend une liste de chemins relatifs, les préfixe avec `$GLOBALS['BASE_DIR']`, vérifie leur existence, les inclut et fusionne leurs tableaux retournés en un seul tableau. Il joue également le rôle de gardien : toute tentative d'accès à un fichier manquant ou illisible lève une exception.

## ⚙️ Rôle technique

Classe statique avec deux méthodes :
- `loadFiles(array $files)` : boucle sur les chemins, préfixe avec `$GLOBALS['BASE_DIR']`, appelle `isFileExist()`, charge avec `require`, valide que le résultat est un tableau, puis fusionne tout via `array_reduce` + `array_merge`.
- `isFileExist(string $file)` : vérifie `file_exists()` ET `is_readable()`, lève `\RuntimeException` sinon.

Dépendance importante : utilise `$GLOBALS['BASE_DIR']` pour résoudre les chemins — cette variable globale doit être initialisée avant tout appel (elle l'est dans `entryPoint.php`).

---

## 📥 Entrées / Dépendances

- **Imports principaux :** aucun import externe (PHP natif uniquement)
- **Variables globales utilisées :** `$GLOBALS['BASE_DIR']` — chemin absolu de la racine de SuiteCRM, défini dans `include/entryPoint.php`
- **Arguments / paramètres d'entrée :** tableau de chemins relatifs (strings)

## 📤 Sorties / Exports

| Symbole | Type | Rôle |
|---|---|---|
| `loadFiles(array $files)` | méthode statique | Charge et fusionne des fichiers PHP retournant des tableaux |
| `isFileExist(string $file)` | méthode statique | Vérifie existence + lisibilité d'un fichier, lève RuntimeException sinon |

**Consommateurs identifiés dans le repo :**
- `Api/Core/Loader/ContainerLoader.php` — appelle `loadFiles()` pour settings Slim et services
- `Api/Core/Loader/RouteLoader.php` — appelle `isFileExist()` pour chaque fichier de routes

## 🔗 Relations clés

- **Appelé par :** `ContainerLoader`, `RouteLoader`
- **Appelle :** `file_exists()`, `is_readable()`, `require`, `array_reduce`, `array_merge`
- **Position dans le flux global :** couche d'accès aux fichiers de configuration, utilisée durant le bootstrap avant toute requête

---

## 💡 Points d'attention

- **Bug potentiel (ligne 27-28) :** si aucun fichier n'est trouvé dans la boucle, `$config` peut ne jamais être assignée, puis `is_array($config)` retournera `false` sur une variable non définie et une notice PHP sera levée. La vérification `if (!is_array($config))` est hors du bloc `if (self::isFileExist($file))`, ce qui est incohérent.
- `isFileExist()` lève `\RuntimeException` pour tout fichier absent — comportement fail-fast intentionnel, à distinguer de `CustomLoader` qui gère silencieusement les fichiers optionnels.
- La fusion utilise `array_merge` (pas de fusion profonde) — les clés dupliquées au même niveau sont écrasées par le dernier fichier.
- Commentaire ligne 34 : `// since we support 5.5.9, we can't use splat op here` — explique l'usage de `array_reduce` à la place de `array_merge(...$configs)`.
