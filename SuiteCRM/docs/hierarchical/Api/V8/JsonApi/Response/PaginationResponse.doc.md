# Fichier : PaginationResponse.php

**Chemin :** `Api/V8/JsonApi/Response/PaginationResponse.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Objet de valeur représentant les liens de navigation de pagination JSON:API (`first`, `prev`, `next`, `last`). Étend `LinksResponse` en y ajoutant ces quatre propriétés de pagination et en surchargeant la sérialisation.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\JsonApi\Response\LinksResponse` | Classe parente (fournit `self` et `related`) |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `PaginationResponse` | classe | DTO pour les liens de pagination JSON:API |
| `setFirst(string)` / `getFirst()` | méthodes publiques | Lien vers la première page |
| `setPrev(string)` / `getPrev()` | méthodes publiques | Lien vers la page précédente |
| `setNext(string)` / `getNext()` | méthodes publiques | Lien vers la page suivante |
| `setLast(string)` / `getLast()` | méthodes publiques | Lien vers la dernière page |
| `jsonSerialize()` | méthode publique | Retourne le tableau `{first, prev, next, last}` (valeurs nulles incluses) |

---

## Interactions

**Instancié par :**
- `Api/V8/JsonApi/Helper/PaginationObjectHelper.php` — `getPaginationLinks()` (ligne 33)

**Utilisé comme type dans :**
- `Api/V8/JsonApi/Helper/PaginationObjectHelper.php` — type de retour de `getPaginationLinks()`

---

## Notes

- Contrairement à `LinksResponse::jsonSerialize()` qui filtre les nulls via `array_filter()`, `PaginationResponse::jsonSerialize()` retourne toujours les 4 clés, y compris avec valeur `null` (ligne 95-100). Les liens non définis apparaîtront donc en JSON comme `null`.
- `PaginationObjectHelper::getPaginationLinks()` ne renseigne `first`/`prev` que si page > 1 et `next`/`last` que si une page suivante existe — donc en pratique, certaines clés seront `null` dans la réponse.
