# SugarMin.php

**Chemin :** `jssource/SugarMin.php`
**Type :** `PHP (utilitaire build JS)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fournit la classe `SugarMin`, wrapper de minification JavaScript. Elle délègue la minification à la bibliothèque JShrink (`JShrink\Minifier`). Point d'entrée unique pour tous les appels de minification JS dans le pipeline de build SuiteCRM.

**Type :** build

---

## Dépendances clés
- `JShrink\Minifier` — bibliothèque Composer de minification JS (import `use JShrink\Minifier`)

## Exports / Symboles principaux
- `SugarMin` — classe (statique)
  - `SugarMin::minify(string $js, string $compression = 'light') : string` — minifie le code JS passé en paramètre. Lève une exception en cas d'erreur.

## Interactions
- **Appelé par :**
  - `jssource/minify_utils.php` — `CompressFiles()` (ligne 334) et `ConcatenateFiles()` (ligne 172)
- **Appelle :** `JShrink\Minifier::minify()`
- **Position dans le flux global :** invoqué lors du build JS, avant l'écriture des fichiers concaténés dans `cache/`

---

## Notes
- Le constructeur est privé (`private function __construct`) : la classe est utilisée uniquement via `SugarMin::minify()`.
- Le paramètre `$compression` (`light` ou `deep`) est transmis au constructeur mais non utilisé dans `jsParser()` — seul JShrink est effectivement appelé.
- `#[\AllowDynamicProperties]` indique une migration PHP 8.2+ en cours.
