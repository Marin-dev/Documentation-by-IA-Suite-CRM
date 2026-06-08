# 📄 Sort.php

**Chemin :** `Api/V8/Param/Options/Sort.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation pour le paramètre `sort` des requêtes de liste. Valide le format du tri et le transforme en clause SQL ORDER BY via `SortRepository::parseOrderBy`. Gère le contexte module simple et le contexte de relation (via `linkFieldName`).

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente |
| `Api\V8\JsonApi\Repository\Sort` | Repository de parsing du tri JSON:API → SQL ORDER BY |
| `Symfony\Component\OptionsResolver\{OptionsResolver, Options}` | Résolution et normalisation |
| `Symfony\Component\Validator\Constraints\{NotBlank, Regex}` | Contraintes de validation |

---

## Constantes

| Constante | Valeur | Description |
|---|---|---|
| `REGEX_SORT_PATTERN` | `/[^\w\-]/` | Accepte uniquement `\w` et `-` (conventions JSON:API : `-field` pour DESC) |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'sort'` comme option définie (non requise)
2. Type attendu : `string`
3. Validation : non vide + regex `REGEX_SORT_PATTERN`
4. Normaliseur :
   - Si `'linkFieldName'` présent → `BeanManager::getLinkedFieldBean(sourceBean, linkFieldName)`
   - Sinon → `BeanManager::newBeanSafe(moduleName)`
   - Appelle `SortRepository::parseOrderBy($bean, $value)` → retourne une chaîne SQL ORDER BY

---

## Interactions

- **Hérite de :** `BaseOption`
- **Consommée par :** INCONNU — probablement `GetModulesParams`, `GetRelationshipParams`
- **Même bifurcation** que `Filter.php` selon la présence de `'linkFieldName'`

---

## Notes

- Le préfixe `-` dans la valeur de tri est la convention JSON:API pour le tri descendant (ex: `sort=-date_entered`).
- `SortRepository::parseOrderBy` gère probablement ce préfixe `-` pour générer `DESC` en SQL — INCONNU sans lire le fichier.
- Troisième paramètre `true` dans `createClosure` (par rapport à `Filter`) — INCONNU la différence de comportement exacte sans lire `ValidatorFactory`.
