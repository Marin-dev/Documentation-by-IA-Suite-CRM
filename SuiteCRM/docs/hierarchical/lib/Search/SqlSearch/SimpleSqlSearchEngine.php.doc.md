# SimpleSqlSearchEngine.php

**Chemin :** `lib/Search/SqlSearch/SimpleSqlSearchEngine.php`
**Type :** PHP — Service (moteur de recherche)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Moteur de recherche SQL naif utilisant des requetes LIKE sur les champs varchar/text de chaque table de module. Principalement fourni comme preuve de concept.

## Role technique
Etend `SearchEngine`. Pour chaque module, inspecte la structure de la table via `DBManager::getTableDescription()`, filtre les champs varchar/text, et construit une requete SQL `SELECT id FROM table WHERE field LIKE '...' OR ...`. Utilise `addslashes()` pour l'echappement.

---

## Dependances cles
- `SuiteCRM\Search\{SearchEngine, SearchQuery, SearchResults, SearchWrapper}`
- `DBManagerFactory`, `BeanFactory`
- `SuiteCRM\Exception\InvalidArgumentException`

## Exports / Symboles principaux
- `SimpleSqlSearchEngine` — classe moteur de recherche
  - `search(SearchQuery $query): SearchResults`

## Relations cles
- **Appele par :** `SearchWrapper` (si configure)
- **Position dans le flux global :** moteur de preuve de concept, non recommande en production

---

## Points d'attention
- Utilise `addslashes()` a la place d'un echappement BDD natif — risque d'injection SQL si mal utilise.
- Tres inefficace sur de grandes bases (LIKE sans index).
- Non visible dans l'UI par defaut (pas enregistre dans `SearchWrapper::$engines`).
