# SugarSpriteBuilder.php

**Chemin :** `modules/Administration/SugarSpriteBuilder.php`
**Type :** PHP (Model / service)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Construit les fichiers sprites CSS en combinant les icones de themes en une seule image (PNG) et en generant la CSS correspondante. Optimise le chargement des icones en reduisant le nombre de requetes HTTP.

## Role technique
Classe `SugarSpriteBuilder`. Utilise la librairie GD (`imagecreatetruecolor`, `imagecopyresampled`) pour combiner les images. Peut minifier la CSS generee via `cssmin.php`. Supporte les modes silencieux, upgrade et debug.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/SugarTheme/cssmin.php` | Minification CSS |
| Extension PHP GD | Manipulation images |

## Symboles principaux
- `SugarSpriteBuilder` — classe de construction des sprites
- `$isAvailable` — indique si GD est disponible
- `$fileName = 'sprites'` — nom base des fichiers generes
- `$cssMinify = true` — activation de la minification CSS

## Interactions
- **Appele par :** `AdministrationController::action_callRebuildSprites()`, `UpgradeWizard/uw_utils.php::rebuildSprites()`
