# AOW_WorkFlow_Hook.php

**Chemin :** `custom/Extension/application/Ext/LogicHooks/AOW_WorkFlow_Hook.php`
**Type :** PHP — Hook de logique applicative (Logic Hook)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Enregistre le hook global `after_save` qui déclenche le moteur de workflows AOW (Advanced OpenWorkflow) sur tous les beans de l'application. Ce fichier est chargé automatiquement par le système d'extensions de SuiteCRM lors du rebuild des extensions.

---

## Type

Hook de logique applicative (Logic Hook) — extension du framework SuiteCRM.

---

## Dépendances clés

| Dépendance | Chemin | Rôle |
|---|---|---|
| `AOW_WorkFlow` (classe) | `modules/AOW_WorkFlow/AOW_WorkFlow.php` | Classe principale du moteur de workflows |
| `$hook_array` (variable globale) | Fournie par le framework | Tableau des hooks enregistrés par niveau d'événement |

---

## Exports / Symboles principaux

- **Variable modifiée :** `$hook_array['after_save']` — tableau PHP global étendu avec l'entrée du hook AOW.
- **Hook enregistré :** priorité `99`, événement `after_save`, appelle `AOW_WorkFlow::run_bean_flows()`.

---

## Interactions

- **Appelé par :** Le framework SuiteCRM lors du chargement des extensions (merge des fichiers `Ext/LogicHooks/`). Déclenché à chaque `after_save` sur n'importe quel bean.
- **Appelle :** `AOW_WorkFlow::run_bean_flows()` (`modules/AOW_WorkFlow/AOW_WorkFlow.php`) — méthode qui évalue et exécute les workflows correspondant au bean sauvegardé.

---

## Notes

- La priorité `99` signifie que ce hook s'exécute tardivement dans la chaîne `after_save`, après la plupart des autres hooks.
- Ce fichier est placé dans `custom/Extension/` : il ne doit pas être modifié directement ; une mise à jour SuiteCRM peut nécessiter un `Repair > Quick Repair and Rebuild` pour recompiler les extensions.
- Si `$hook_array` n'est pas encore initialisé, le fichier le crée (lignes 28-30), ce qui est la pratique standard des extensions SuiteCRM.
