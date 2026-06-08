# action_view_map.php

**Chemin :** `modules/ModuleBuilder/action_view_map.php`
**Type :** `PHP` — configuration de routage
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Définit la table de correspondance entre les noms d'actions HTTP et les noms de vues du module ModuleBuilder/Studio. Utilisé par le framework SugarCRM pour router chaque action vers la vue appropriée.

## Rôle technique
Déclare et peuple le tableau `$action_view_map` (format `'action_name' => 'view_name'`). Ce tableau est lu par le dispatcher principal de SugarCRM lors du traitement d'une requête vers le module ModuleBuilder.

---

## Exports / Symboles principaux
- `$action_view_map` — tableau (variable globale) — table de routage action → vue

## Correspondances clés

| Action | Vue |
|---|---|
| `index` | `main` |
| `module` | `module` |
| `modulefields` | `modulefields` |
| `modulelabels` | `modulelabels` |
| `relationships` | `relationships` |
| `relationship` | `relationship` |
| `resetmodule` | `resetmodule` |
| `modulefield` | `modulefield` |
| `displaydeploy` | `displaydeploy` |
| `package` | `package` |
| `dropdown` | `dropdown` |
| `dropdowns` | `dropdowns` |
| `exportcustomizations` | `exportcustomizations` |
| `home` | `home` |

## Notes
Les entrées `dc`, `dcajax`, `quick`, `quickcreate`, `spot`, `inlinefield`, `inlinefieldsave`, `pluginlist`, `downloadplugin` sont ajoutées depuis la carte globale — elles correspondent à des vues standard SugarCRM non spécifiques à ModuleBuilder.
