# Fichier : SugarMin.php

**Chemin :** `jssource/SugarMin.php`
**Type :** build (minificateur JS)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Fournit le point d'entree PHP pour la minification de code JavaScript. Il s'agit d'un adaptateur sur la librairie tierce `JShrink\Minifier` qui realise la compression effective.

## Role technique
Classe `SugarMin` avec constructeur prive et methode statique `minify()` (patron Singleton partiel). La methode `jsParser()` delegue directement a `JShrink\Minifier::minify()`. L'attribut `#[\AllowDynamicProperties]` indique une adaptation PHP 8.2+.

---

## Dependances cles
- **Imports principaux :**
  - `JShrink\Minifier` (via Composer) — librairie de minification JS tierce
- **Variables d'environnement :** aucune
- **Arguments :**
  - `$js` (string) — code JavaScript source
  - `$compression` (string) — niveau de compression : `'light'` (defaut) ou `'deep'`

## Exports / Symboles principaux
- `SugarMin::minify(string $js, string $compression)` — methode statique — retourne le JS minifie

## Interactions
- **Appele par :**
  - `jssource/minify_utils.php` — `ConcatenateFiles()` (ligne 172) et `CompressFiles()` (ligne 334)
- **Appelle :**
  - `JShrink\Minifier::minify()`

---

## Notes
- Le constructeur est prive : la classe ne peut pas etre instanciee directement depuis l'exterieur.
- Les exceptions sont propagees (non swallees) : `throw $e` ligne 46.
- Le parametre `$compression` est accepte mais non transmis a JShrink — seule la valeur par defaut de JShrink est appliquee.
