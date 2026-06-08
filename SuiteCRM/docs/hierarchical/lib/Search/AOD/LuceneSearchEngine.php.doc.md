# LuceneSearchEngine.php

**Chemin :** `lib/Search/AOD/LuceneSearchEngine.php`
**Type :** PHP — Service (moteur de recherche)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Moteur de recherche base sur l'index AOD Lucene de SuiteCRM. Utilise l'index Lucene genere par le module `AOD_Index` pour effectuer des recherches textuelles rapides avec mise en cache des resultats.

## Role technique
Etend `SearchEngine`. La methode `search()` interroge l'index Lucene via `$index->find()`. Filtre les resultats selon les ACL et SecurityGroups. Met en cache les resultats dans `cache/modules/AOD_Index/QueryCache/` avec une TTL de 5 minutes. Groupe les resultats par module avec pagination.

---

## Dependances cles
- `SuiteCRM\Search\SearchEngine` — classe abstraite parente
- `SuiteCRM\Search\SearchQuery` / `SearchResults`
- `BeanFactory`, `ACLController`, `SecurityGroup`
- `SugarBean`
- `SuiteCRM\Exception\Exception`

## Exports / Symboles principaux
- `LuceneSearchEngine` — classe moteur de recherche
  - `search(SearchQuery $query): SearchResults`

## Relations cles
- **Appele par :** `lib/Search/SearchWrapper.php` (via `fetchEngine('LuceneSearchEngine')`)
- **Appelle :** `AOD_Index` bean, `BeanFactory`, `ACLController`, `SecurityGroup`
- **Position dans le flux global :** un des trois moteurs de recherche disponibles (legacy AOD)

---

## Points d'attention
- Cache Lucene : expire apres 5 minutes (`time() - 5*60`, ligne 115).
- Filtre ACL : verifie `ACLController::checkAccess()` et `SecurityGroup::groupHasAccess()` (lignes 165-171).
- Resultat cache invalide si la structure n'est pas un array de `stdClass` avec `record_module` et `record_id`.
