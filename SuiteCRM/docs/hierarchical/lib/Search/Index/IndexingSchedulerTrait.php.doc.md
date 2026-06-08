# IndexingSchedulerTrait.php

**Chemin :** `lib/Search/Index/IndexingSchedulerTrait.php`
**Type :** PHP — Trait
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Trait ajoutant une methode statique `schedulerJob()` aux indexeurs. Permet d'integrer l'indexeur dans le systeme de taches planifiees de SuiteCRM.

## Role technique
Methode statique `schedulerJob($options)` : instancie l'indexeur (`new self()`), configure l'indexation differentielle (defaut: true = differentielle), et appelle `index()`. Retourne `true` si succes, `false` si erreur.

---

## Dependances cles
- `AbstractIndexer` (attendu via `$this`)

## Exports / Symboles principaux
- `IndexingSchedulerTrait` — trait
  - `static schedulerJob(array $options = []): bool`
    - option `partial` (bool, defaut true) — differentiel si true

- **Consommateurs :** `ElasticSearchIndexer`

---

## Points d'attention
- Appelle `self::isEnabled()` — la classe implementant le trait doit definir cette methode statique.
- En cas d'exception, logge l'erreur et retourne `false` sans propager.
