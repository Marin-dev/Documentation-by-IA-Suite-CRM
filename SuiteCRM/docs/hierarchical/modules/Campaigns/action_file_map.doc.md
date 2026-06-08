# action_file_map.php

**Chemin :** `modules/Campaigns/action_file_map.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Mappe l'action `subpanelviewer` (en minuscules) vers le fichier `SubPanelViewer.php` du module. Permet au framework MVC de résoudre le fichier correspondant à cette action.

## Type

`config` (mapping actions)

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `$action_file_map['subpanelviewer']` | chaîne | Chemin vers `SubPanelViewer.php` |

---

## Interactions

- **Consommé par :** Framework MVC SuiteCRM (résolution des actions)

---

## Points d'attention

- RAS.
