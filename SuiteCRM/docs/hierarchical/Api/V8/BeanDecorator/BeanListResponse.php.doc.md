# 📄 BeanListResponse.php

**Chemin :** `Api/V8/BeanDecorator/BeanListResponse.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Encapsule le résultat brut retourné par `SugarBean::get_list()`. Normalise l'accès à la liste de beans et au nombre de lignes via des getters typés.

**Type :** model

---

## Dépendances clés

| Dépendance | Rôle |
|---|---|
| `\SugarBean` | Type des éléments dans le tableau `$beans` |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\BeanDecorator\BeanListResponse`

| Méthode | Signature | Description |
|---|---|---|
| `__construct` | `(array $result = [])` | Extrait `'list'` et `'row_count'` du tableau résultat SuiteCRM |
| `getBeans` | `(): \SugarBean[]` | Retourne le tableau de beans |
| `getRowCount` | `(): int` | Retourne le nombre de lignes total |

**Structure attendue du `$result` :**
```
[
  'list'      => \SugarBean[],  // tableau de beans
  'row_count' => int            // nombre total de lignes
]
```

---

## Interactions

- **Créé par :** `BeanListRequest::fetch()` (ligne 161)
- **Créé aussi par :** `ModuleService::getRecords()` directement (`new BeanListResponse($beanResult)`) pour le cas email
- **Consommé par :** `ModuleService::getRecords()` via `getBeans()` et boucle d'itération

---

## Notes

- Objet Value Object simple : pas de logique métier, uniquement extraction et exposition typée du résultat `get_list()`.
- `#[\AllowDynamicProperties]` inclus par cohérence avec le reste du namespace.
- `getRowCount()` caste explicitement en `int` la valeur brute qui peut être une string retournée par la DB.
