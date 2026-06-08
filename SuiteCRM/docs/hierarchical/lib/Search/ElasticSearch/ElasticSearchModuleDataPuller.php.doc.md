# ElasticSearchModuleDataPuller.php

**Chemin :** `lib/Search/ElasticSearch/ElasticSearchModuleDataPuller.php`
**Type :** PHP — Service (extraction de donnees)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Extracteur de SugarBeans par lots depuis la base de donnees pour l'indexation Elasticsearch. Supporte la pagination, le mode differentiel (filtrage par `date_modified`/`date_entered`), et l'inclusion des enregistrements supprimes.

## Role technique
Utilise `SugarBean::get_list()` avec pagination (offset + batchSize). En mode differentiel, ajoute une clause WHERE sur `date_modified > lastIndexTime OR date_entered > lastIndexTime`. Methode `pullNextBatch()` retourne null quand il n'y a plus de resultats.

---

## Dependances cles
- `BeanFactory` — creation du bean seed
- `SugarBean` — bean de reference pour la requete

## Exports / Symboles principaux
- `ElasticSearchModuleDataPuller` — classe
  - `pullNextBatch(): array|null`
  - `setLastIndexTime(string): $this`
  - `setShowDeleted(int): $this` — -1 inclut les supprimes
  - `setDifferential(bool): $this`
  - `recordsPulled: int` (acces via `__get()`)

- **Consommateurs identifies :**
  - `lib/Search/ElasticSearch/ElasticSearchIndexer.php` (ligne 204)

## Relations cles
- **Appele par :** `ElasticSearchIndexer::indexModule()`
- **Appelle :** `SugarBean::get_list()`

---

## Points d'attention
- `__get()` magique expose toutes les proprietes protegees (ligne 202).
- En mode differentiel sans `lastIndexTime`, leve une `RuntimeException` (ligne 184).
