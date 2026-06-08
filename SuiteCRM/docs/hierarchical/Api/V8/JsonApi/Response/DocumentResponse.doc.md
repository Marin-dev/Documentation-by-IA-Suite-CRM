# Fichier : DocumentResponse.php

**Chemin :** `Api/V8/JsonApi/Response/DocumentResponse.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Objet de valeur racine d'une réponse JSON:API. Représente le document complet avec les noeuds `data`, `meta` et `links`. Implémente `\JsonSerializable` et gère le cas d'une réponse vide (ajout automatique d'un message meta).

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\JsonApi\Response\DataResponse` | Type du noeud `data` (objet unique ou tableau) |
| `Api\V8\JsonApi\Response\MetaResponse` | Type du noeud `meta` |
| `Api\V8\JsonApi\Response\LinksResponse` | Type du noeud `links` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `DocumentResponse` | classe | DTO représentant le document JSON:API racine |
| `setData($data)` / `getData()` | méthodes publiques | Gère le noeud `data` (tableau ou objet unique) |
| `setMeta()` / `getMeta()` | méthodes publiques | Gère le noeud `meta` (métadonnées, pagination, etc.) |
| `setLinks()` / `getLinks()` | méthodes publiques | Gère le noeud `links` (liens de pagination) |
| `jsonSerialize()` | méthode publique | Retourne le document JSON:API complet |

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
- `Api\V8\JsonApi\Response\MetaResponse` — instanciation automatique en cas de réponse vide (ligne 80)

---

## Notes

- Comportement spécial : si `data` est vide ET qu'aucun `meta` n'est défini, un `MetaResponse` avec `message = 'Request was successful, but there is no result'` est injecté automatiquement (lignes 79-81).
- Le `meta` est placé avant `data` dans la réponse sérialisée grâce à la fusion de tableaux (ligne 84 : `['meta' => ...] + $response`).
- `links` n'est ajouté que si défini (ligne 87-89).
