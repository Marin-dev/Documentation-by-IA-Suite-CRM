# Fichier : AttributeResponse.php

**Chemin :** `Api/V8/JsonApi/Response/AttributeResponse.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Objet de valeur représentant le noeud `attributes` d'une ressource JSON:API. Étend `MetaResponse` (conteneur de propriétés dynamiques) en y ajoutant une validation interdisant les clés réservées `relationships` et `links`.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\JsonApi\Response\MetaResponse` | Classe parente fournissant le stockage dynamique et la sérialisation JSON |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AttributeResponse` | classe | Conteneur d'attributs JSON:API avec validation des clés interdites |
| `__construct($properties)` | méthode publique | Appelle le parent et valide l'absence des clés `relationships` et `links` |

---

## Interactions

**Appelé par :**
- `Api/V8/JsonApi/Helper/AttributeObjectHelper.php` — instanciation du résultat de `getAttributes()`
- `Api/V8/JsonApi/Response/DataResponse.php` — utilisé comme type de la propriété `$attributes`

**Appelle :**
- `MetaResponse::__construct()` — stockage des propriétés

---

## Notes

- Conforme à la spec JSON:API : [http://jsonapi.org/format/#document-resource-object-attributes](http://jsonapi.org/format/#document-resource-object-attributes) (ligne 9).
- Les clés interdites sont `['relationships', 'links']` (ligne 11). Lève `\InvalidArgumentException` si présentes.
- Hérite de `jsonSerialize()` de `MetaResponse` : sérialise le tableau `$properties`.
