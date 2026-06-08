# RebuildDashlets.php

**Chemin :** `modules/Administration/RebuildDashlets.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Reconstruit le cache des dashlets disponibles. Supprime le cache existant (`cache/dashlets/dashlets.php`) et regenere via `DashletCacheBuilder`.

## Role technique
Script procedral. Supporte un mode silencieux (`$_REQUEST['silent']`). Instancie `DashletCacheBuilder::buildCache()`.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/Dashlets/DashletCacheBuilder.php` | Construction du cache dashlets |

## Interactions
- **Appele par :** Action d'administration / `RepairAndClear::clearDashlets()` (indirectement)
