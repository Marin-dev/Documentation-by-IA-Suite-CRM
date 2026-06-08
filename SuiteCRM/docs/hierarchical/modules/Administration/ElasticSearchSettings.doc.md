# ElasticSearchSettings.php

**Chemin :** `modules/Administration/ElasticSearchSettings.php`
**Type :** PHP (point d'entree / delegation)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Point d'entree pour la page de configuration d'ElasticSearch (moteur de recherche full-text). Delegue au controleur dedie du sous-module Search/ElasticSearch.

## Role technique
Instancie `SuiteCRM\Modules\Administration\Search\ElasticSearch\Controller` et appelle `handle()`.

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\Modules\Administration\Search\ElasticSearch\Controller` | Controleur ElasticSearch |

## Interactions
- **Appele par :** `index.php?module=Administration&action=ElasticSearchSettings`
- **Delegue vers :** `modules/Administration/Search/ElasticSearch/Controller.php`

---

## Notes
- Acces restreint : `is_admin($current_user)`.
