# Fichier : Error.php

**Chemin :** `modules/Users/Error.php`
**Type :** PHP — Vue (affichage d'erreur)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche une page d'erreur generique pour le module Users. Gere deux cas : erreur d'import (parametre `ie_error=true`) ou message d'erreur passe dans la requete (`error_string`).

## Role technique

Script procedural court. Utilise `LoggerManager::getLogger()->warn()` pour signaler que le passage de `error_string` en parametre de requete est deprecie. Affiche le message via `getAppString()` ou depuis `$request['error_string']`.

---

## Dependances principales

| Import | Role |
|---|---|
| `include/utils.php` | Fonctions utilitaires |
| `$app_strings` | Chaines applicatives |
| `LoggerManager` | Logging deprecation warning |

## Exports / Symboles principaux

Aucun. Produit du HTML brut.

---

## Points d'attention

- Le mecanisme de passage d'`error_string` par URL est marque deprecie (lignes 57, 61) — a remplacer par `SugarApplication::appendErrorMessage()`.
