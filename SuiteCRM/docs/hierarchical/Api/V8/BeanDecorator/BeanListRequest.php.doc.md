# 📄 BeanListRequest.php

**Chemin :** `Api/V8/BeanDecorator/BeanListRequest.php`
**Type :** PHP (model / builder)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Encapsule et construit une requête de liste sur un `SugarBean`. Implémente le pattern Fluent Builder : chaque méthode de configuration retourne `$this`, permettant le chaînage. L'appel final `fetch()` délègue à `SugarBean::get_list()` et retourne un `BeanListResponse`.

**Type :** model

---

## Dépendances clés

| Dépendance | Rôle |
|---|---|
| `\SugarBean` | Bean SuiteCRM sur lequel la requête est exécutée |
| `BeanManager` | Fournit les constantes `DEFAULT_OFFSET` et `DEFAULT_ALL_RECORDS` |
| `BeanListResponse` | Objet de réponse construit par `fetch()` |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\BeanDecorator\BeanListRequest`

| Méthode | Signature | Description |
|---|---|---|
| `__construct` | `(\SugarBean $bean)` | Initialise avec le bean cible |
| `orderBy` | `(string $orderBy): self` | Clause ORDER BY |
| `where` | `(string $where): self` | Clause WHERE SQL |
| `offset` | `(int $offset): self` | Décalage de pagination (défaut : 0) |
| `limit` | `(int $limit): self` | Nombre maximum de lignes (défaut : -1 = illimité) |
| `max` | `(int $max): self` | Limite maximale globale (défaut : -99 = tous) |
| `deleted` | `(int $deleted): self` | Inclure les enregistrements supprimés (0 = non) |
| `singleSelect` | `(bool $singleSelect): self` | Mode single select SQL (défaut : true) |
| `fields` | `(array $fields): self` | Liste de champs à sélectionner |
| `fetch` | `(): BeanListResponse` | Exécute la requête via `$bean->get_list()` |

**Valeurs par défaut :**

| Propriété | Valeur |
|---|---|
| `$orderBy` | `''` |
| `$where` | `''` |
| `$offset` | `BeanManager::DEFAULT_OFFSET` (0) |
| `$limit` | `-1` |
| `$max` | `BeanManager::DEFAULT_ALL_RECORDS` (-99) |
| `$deleted` | `0` |
| `$singleSelect` | `true` |
| `$fields` | `[]` |

---

## Interactions

- **Créé par :** `BeanManager::getList($module)` (ligne 116)
- **Appelé par :** `ModuleService::getRecords()` via `$this->beanManager->getList($module)->orderBy(...)->fetch()`
- **Appelle :** `SugarBean::get_list()` (API SuiteCRM native)

---

## Notes

- Le décorateur isole la logique de construction de requête de liste du code des services, rendant les services plus lisibles.
- `#[\AllowDynamicProperties]` est nécessaire pour compatibilité PHP 8.2+ (bean SuiteCRM utilise des propriétés dynamiques).
- La valeur `-99` pour `$max` correspond à `BeanManager::DEFAULT_ALL_RECORDS` — convention SuiteCRM pour "tous les enregistrements".
