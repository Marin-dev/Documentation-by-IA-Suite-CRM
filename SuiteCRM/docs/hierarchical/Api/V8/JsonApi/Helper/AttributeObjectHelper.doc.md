# Fichier : AttributeObjectHelper.php

**Chemin :** `Api/V8/JsonApi/Helper/AttributeObjectHelper.php`
**Type :** helper
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Convertit les champs d'un `SugarBean` en objet `AttributeResponse` conforme à la spec JSON:API. Applique les filtres de visibilité (`sensitive`, `api-visible`), un sous-ensemble optionnel de champs, et la normalisation des dates au format ISO 8601 (ATOM).

---

## Type

helper

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Injecté dans le constructeur, non utilisé directement ici mais disponible comme dépendance |
| `Api\V8\JsonApi\Response\AttributeResponse` | Objet de retour encapsulant les attributs filtrés |
| `\SugarBean` (global SuiteCRM) | Bean source dont les champs sont extraits via `toArray()` et `field_defs` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AttributeObjectHelper` | classe | Helper injectable pour la construction d'attributs JSON:API |
| `getAttributes(\SugarBean $bean, array\|null $fields)` | méthode publique | Retourne un `AttributeResponse` à partir d'un bean, en filtrant les champs sensibles/non-visibles et en convertissant les dates |

---

## Interactions

**Appelé par :**
- `Api/V8/Service/ModuleService.php`
- `Api/V8/Service/UserService.php`
- `Api/V8/Service/ListViewService.php`
- `Api/V8/Service/ListViewSearchService.php`
- `Api/V8/Service/RelationshipService.php`

**Appelle :**
- `\SugarBean::fixUpFormatting()` — normalise les valeurs du bean avant extraction
- `\SugarBean::toArray()` — sérialise le bean en tableau
- `Api\V8\JsonApi\Response\AttributeResponse` — constructeur

**Enregistré comme service dans :**
- `Api/V8/Config/services/helpers.php`
- `Api/V8/Config/services/services.php`

---

## Notes

- Les champs marqués `sensitive = true` ou `api-visible = false` dans `field_defs` sont exclus (lignes 41-48).
- La clé `id` est systématiquement supprimée des attributs retournés (ligne 64), car elle appartient au niveau racine de l'objet JSON:API.
- La conversion de date ne s'applique qu'aux chaînes correspondant au format `Y-m-d H:i:s` ; les autres valeurs string sont retournées telles quelles (lignes 52-57).
- Si `$fields` est nul, tous les champs du bean sont pris en compte (`array_keys($bean->field_defs)`).
