# SearchFormView.php

**Chemin :** `lib/Search/UI/SearchFormView.php`
**Type :** PHP — View MVC
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Vue du formulaire de recherche. Construit les options de pagination, de moteur et de modules pour le template Smarty du formulaire de recherche.

## Role technique
Etend `View`. Template : `lib/Search/UI/templates/search.form.tpl`. Calcule les tailles de page depuis `$sugar_config['search']['pagination']` (min/step/max). Masque l'engine selector si le moteur est Basic ou Elasticsearch. Utilise `StringUtils::camelToTranslation()` pour traduire les noms de moteurs.

---

## Dependances cles
- `SuiteCRM\Search\SearchWrapper`
- `SuiteCRM\Utility\StringUtils`
- `$sugar_config` global — cles `search.pagination.min/step/max`, `search.ElasticSearch.enabled`

## Exports / Symboles principaux
- `SearchFormView` — vue
  - `display(): void`

- **Consommateurs :** `SearchFormController`

---

## Points d'attention
- Defaut de pagination si config absente : min=10, step=10, max=50 (ligne 122).
- Si `search.ElasticSearch.enabled === false`, le moteur ES est retire des options (ligne 74).
