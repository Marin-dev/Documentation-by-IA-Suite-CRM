# callJSRepair.php

**Chemin :** `modules/Administration/callJSRepair.php`
**Type :** PHP (handler AJAX)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Endpoint AJAX pour la reparation/reconstruction des fichiers JavaScript. Execute les operations de minification, concatenation ou remplacement des fichiers JS selon le mode demande.

## Role technique
Dispatche sur `$_REQUEST['js_admin_repair']` :
- `concat` : rebuilds les groupes JS concatenes
- `replace` : remplace les JS compresses par les sources
- `mini` : remplace par sources puis re-minifie
- `repair` : compresse les JS existants sans ecraser les sources

Utilise les fonctions de `jssource/minify.php` (`reverseScripts`, `BackUpAndCompressScriptFiles`, `ConcatenateFiles`). `max_execution_time` passe temporairement a 600s.

---

## Dependances cles
| Element | Role |
|---|---|
| `jssource/minify.php` | Fonctions de minification JS |

## Symboles principaux
- Aucune classe ni fonction — script handler

## Interactions
- **Appele par :** JS dans `RepairJSFile.php` (AJAX POST vers `action=callJSRepair`)

---

## Notes
- `root_directory` provient de `$_REQUEST` non nettoye — potentiel risque de path traversal si mal filtre en amont.
- `max_execution_time = 600` (10 min) pour les operations longues.
