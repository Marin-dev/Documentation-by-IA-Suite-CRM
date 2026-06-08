# Fichier : DataResponse.php

**Chemin :** `Api/V8/JsonApi/Response/DataResponse.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Objet de valeur représentant un élément `data` individuel dans une réponse JSON:API. Encapsule le type, l'identifiant et les noeuds optionnels `attributes`, `relationships` et `links` d'une ressource. Implémente `\JsonSerializable` pour la sérialisation directe.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\JsonApi\Response\AttributeResponse` | Type de la propriété `$attributes` |
| `Api\V8\JsonApi\Response\RelationshipResponse` | Type de la propriété `$relationships` |
| `Api\V8\JsonApi\Response\LinksResponse` | Type de la propriété `$links` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `DataResponse` | classe | DTO représentant un objet ressource JSON:API |
| `__construct(string $type, string $id)` | méthode publique | Initialise le type et l'id de la ressource |
| `getType()` / `getId()` | méthodes publiques | Accesseurs du type et de l'identifiant |
| `setAttributes()` / `getAttributes()` | méthodes publiques | Gère le noeud `attributes` |
| `setRelationships()` / `getRelationships()` | méthodes publiques | Gère le noeud `relationships` |
| `setLinks()` / `getLinks()` | méthodes publiques | Gère le noeud `links` |
| `jsonSerialize()` | méthode publique | Retourne le tableau JSON:API filtré des clés nulles |

---

## Interactions

**Appelé par :**
- `Api/V8/Service/ModuleService.php`
- `Api/V8/Service/UserService.php`
- `Api/V8/Service/UserPreferencesService.php`
- `Api/V8/Service/RelationshipService.php`
- `Api/V8/Service/MetaService.php`
- `Api/V8/Service/LogoutService.php`
- `Api/V8/Service/ListViewSearchService.php`

**Appelle :**
- `array_filter()` dans `jsonSerialize()` pour exclure les clés nulles (ligne 119)

---

## Notes

- `jsonSerialize()` utilise `array_filter()` : les noeuds non définis (`null`) sont automatiquement exclus de la réponse (ligne 119).
- Contrairement à `DocumentResponse`, `DataResponse` représente une ressource individuelle (pas le document racine).
