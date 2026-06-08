# config.php (Robo)

**Chemin :** `lib/Robo/config.php`
**Configure :** Bootstrap de la configuration SuiteCRM pour les taches Robo
**Derniere mise a jour doc :** 2026-05-30

---

## Ce que ce fichier configure
Charge la configuration SuiteCRM (`config.php` et `config_override.php`) depuis la racine du projet et initialise `$GLOBALS['sugar_config']`. Definit `sugarEntry` si absent. Inclut `SugarConfig.php` pour finaliser l'initialisation.

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `sugarEntry` | `true` | Active les points d'entree SuiteCRM |
| `$GLOBALS['sugar_config']` | depuis config.php | Config globale disponible dans toutes les taches |

## Impacte par / impacte
- Inclus par : `lib/Robo/Traits/RoboTrait.php` (ligne 42)
- Charge : `config.php`, `config_override.php`, `include/SugarObjects/SugarConfig.php`

## Points d'attention
- Ce fichier est inclus via `require_once` dans `RoboTrait` — ne pas inclure deux fois.
