# SearchSettings.php

**Chemin :** `modules/Administration/SearchSettings.php`
**Type :** PHP (point d'entree / delegation)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Point d'entree pour la page de configuration des parametres de recherche globale de SuiteCRM. Delegue au controleur dedie du sous-module Search.

## Role technique
Instancie `SuiteCRM\Modules\Administration\Search\Controller` et appelle `handle()`.

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\Modules\Administration\Search\Controller` | Controleur Search |

## Interactions
- **Appele par :** `index.php?module=Administration&action=SearchSettings`
- **Delegue vers :** `modules/Administration/Search/Controller.php`

---

## Notes
- Acces restreint : `is_admin($current_user)`.
