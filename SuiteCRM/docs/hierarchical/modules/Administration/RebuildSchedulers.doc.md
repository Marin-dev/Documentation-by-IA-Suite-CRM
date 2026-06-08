# RebuildSchedulers.php

**Chemin :** `modules/Administration/RebuildSchedulers.php`
**Type :** PHP (view + action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Reinsere les planificateurs (schedulers) par defaut de SuiteCRM. Utile apres une migration ou si les schedulers ont ete supprimes accidentellement.

## Role technique
Affiche un formulaire de confirmation. En POST (`perform_rebuild=true`), appelle `Schedulers::rebuildDefaultSchedulers()` via `BeanFactory::newBean('Schedulers')`.

---

## Dependances cles
| Element | Role |
|---|---|
| `install/install_utils.php` | Utilitaires d'installation |
| `BeanFactory::newBean('Schedulers')` | Bean planificateurs |

## Interactions
- **Appele par :** `index.php?module=Administration&action=RebuildSchedulers`
- **Lie vers :** `index.php?module=Administration&action=Upgrade` (retour)
