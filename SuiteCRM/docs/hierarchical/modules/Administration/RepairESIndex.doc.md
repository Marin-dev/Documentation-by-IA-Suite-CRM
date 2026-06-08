# RepairESIndex.php

**Chemin :** `modules/Administration/RepairESIndex.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Repare les index ElasticSearch en appelant la methode de reparation du moteur d'indexation. Affiche un message si ElasticSearch n'est pas configure.

## Role technique
Verifie `$sugar_config['search']['ElasticSearch']['enabled']`. Si active, appelle `ElasticSearchIndexer::repairElasticsearchIndex()`. Sinon affiche un message de configuration requise.

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\Search\ElasticSearch\ElasticSearchIndexer` | Service d'indexation ES |

## Symboles principaux
- Aucune classe — script d'action

## Interactions
- **Appele par :** Action d'administration (INCONNU - URL exacte, probablement `action=RepairESIndex`)
- **Appelle :** `ElasticSearchIndexer::repairElasticsearchIndex()`

---

## Notes
- Acces conditionnel : retourne silencieusement si ES desactive (pas de die ni redirect).
