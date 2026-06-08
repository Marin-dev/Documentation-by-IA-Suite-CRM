# 📄 Filter.php

**Chemin :** `Api/V8/Param/Options/Filter.php`
**Type :** PHP (option de validation)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Option de validation et de transformation pour le paramètre `filter` des requêtes de liste. Transforme le tableau de filtres JSON:API en clause SQL WHERE via `FilterRepository::parseWhere`. Gère le contexte module simple et le contexte de relation (via `linkFieldName`).

**Type :** helper / validation

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BaseOption` | Classe parente |
| `Api\V8\JsonApi\Repository\Filter` | Repository de parsing des filtres JSON:API → SQL |
| `Symfony\Component\OptionsResolver\{OptionsResolver, Options}` | Résolution et normalisation |
| `Symfony\Component\Validator\Constraints\NotBlank` | Contrainte de validation |

---

## Comportement de `add(OptionsResolver $resolver)`

1. Déclare `'filter'` avec valeur par défaut : `['deleted' => ['eq' => 0]]` (exclut les soft-deleted par défaut)
2. Type attendu : `array`
3. Validation : non vide
4. Normaliseur :
   - Si l'option `'linkFieldName'` est présente dans le resolver → résout le bean via `BeanManager::getLinkedFieldBean(sourceBean, linkFieldName)`
   - Sinon → résout le bean via `BeanManager::newBeanSafe(moduleName)`
   - Instancie `FilterRepository($bean->db)` et appelle `parseWhere($bean, $values)` → retourne une chaîne SQL WHERE

---

## Interactions

- **Hérite de :** `BaseOption`
- **Consommée par :** INCONNU (probablement `GetModulesParams`, `GetRelationshipParams`)
- **Dépend du contexte :** option `'moduleName'` ou couple `('sourceBean', 'linkFieldName')` doit être disponible dans le resolver
- **Appelle :** `Api\V8\JsonApi\Repository\Filter::parseWhere` pour la transformation → SQL

---

## Notes

- Valeur par défaut `['deleted' => ['eq' => 0]]` : les enregistrements supprimés (soft-delete) sont exclus par défaut sans filtre explicite.
- Commentaire ligne 28 : "we don't support multiple level filtering. for now." — limitation connue et documentée.
- Le comportement bifurque selon la présence de `'linkFieldName'` — permet de filtrer sur les beans liés dans le contexte des relationships.
