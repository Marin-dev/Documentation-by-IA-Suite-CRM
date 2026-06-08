# ElasticSearchHooks.php

**Chemin :** `lib/Search/ElasticSearch/ElasticSearchHooks.php`
**Type :** PHP — Hook SuiteCRM
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Hooks SuiteCRM qui maintiennent l'index Elasticsearch synchronise avec la base de donnees. Declenches apres chaque sauvegarde ou suppression d'un bean.

## Role technique
Deux callbacks : `beanSaved()` et `beanDeleted()`. Verifient si ES est active avant d'agir. Utilisent `ElasticSearchIndexer` pour indexer ou supprimer le bean. Gestion d'erreurs avec catch multi-niveaux (`SearchException`, `Exception`, `Throwable`).

---

## Dependances cles
- `SuiteCRM\Search\ElasticSearch\ElasticSearchIndexer`
- `SuiteCRM\Utility\SuiteLogger`
- `SugarBean`

## Exports / Symboles principaux
- `ElasticSearchHooks` — classe hook
  - `beanSaved(SugarBean $bean, $event, $arguments): void`
  - `beanDeleted(SugarBean $bean, $event, $arguments): void`

## Relations cles
- **Appele par :** systeme de hooks SuiteCRM (after_save, after_delete)
- **Appelle :** `ElasticSearchIndexer::indexBean()`, `ElasticSearchIndexer::removeBean()`
- **Position dans le flux global :** synchronisation ES en temps reel

---

## Points d'attention
- Les modules blacklistes (non dans `getModulesToIndex()`) sont silencieusement ignores avec un warning.
- Si `$bean->indexer` est defini sur le bean, il est utilise a la place d'une nouvelle instance (injection pour tests, ligne 153).
- Si `$bean->deleted === true`, l'action est forcement 'remove' (ligne 170).
