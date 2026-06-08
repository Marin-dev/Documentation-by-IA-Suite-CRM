# AjaxCompose.php

**Chemin :** `modules/ModuleBuilder/MB/AjaxCompose.php`
**Type :** PHP (helper / UI)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Composeur de réponses AJAX pour l'interface ModuleBuilder/Studio. Assemble les sections de l'UI (west, center, east, east2) avec leur titre, breadcrumb et contenu, puis les encode en JSON pour le frontend JavaScript.

## Type
helper

## Dépendances clés
- `getJSONobj()` (fonction globale Sugar) — encodage JSON

## Exports/Symboles principaux
- `AjaxCompose` — classe
  - `addSection($name, $title, $content, $action)` — ajoute une section UI (west/center/east/east2)
  - `getJavascript()` — encode toutes les sections en JSON (ferme automatiquement east/east2 si non remplis)
  - `addCrumb($name, $action)` — ajoute un élément au fil d'Ariane
  - `getBreadCrumb()` — génère le HTML du breadcrumb avec liens JS
  - `echoErrorStatus($labelName)` — écho JSON d'erreur `{failure:true, failMsg:...}`

## Interactions
- **Appelé par :** `ModuleBuilderController::action_ViewTree()` et toutes les vues ModuleBuilder/Studio qui produisent du contenu AJAX
- **Appelle :** `getJSONobj()`

## Notes
- Le breadcrumb pré-initialise un lien "Home" vers `ModuleBuilder.main("Home")` (JavaScript côté client). Ligne 45.
- `getJavascript()` désactive automatiquement les panneaux east/east2 si aucune section n'a été ajoutée pour eux. Lignes 58-63.
