# Fichier : RelationshipResponse.php

**Chemin :** `Api/V8/JsonApi/Response/RelationshipResponse.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Objet de valeur représentant le noeud `relationships` d'une ressource JSON:API. Classe vide étendant `MetaResponse` — hérite de la gestion des propriétés dynamiques et de la sérialisation JSON. Sert de type distinct pour les relations afin de les différencier sémantiquement des attributs et des méta-données.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\JsonApi\Response\MetaResponse` | Classe parente fournissant le stockage dynamique et `jsonSerialize()` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `RelationshipResponse` | classe | Conteneur des relations JSON:API (propriétés dynamiques) |

Aucune méthode propre — tout est hérité de `MetaResponse`.

---

## Interactions

**Instancié par :**
- `Api/V8/JsonApi/Helper/RelationshipObjectHelper.php` — `getRelationships()` (ligne 45)

**Utilisé comme type dans :**
- `Api/V8/JsonApi/Response/DataResponse.php` — propriété `$relationships`

---

## Notes

- Fichier quasi-vide (5 lignes hors namespace) : son rôle est purement sémantique / typage fort.
- La logique de construction des relations est entièrement dans `RelationshipObjectHelper::getRelationships()`.
