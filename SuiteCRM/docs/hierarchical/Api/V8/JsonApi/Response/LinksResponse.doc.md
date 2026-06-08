# Fichier : LinksResponse.php

**Chemin :** `Api/V8/JsonApi/Response/LinksResponse.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Objet de valeur représentant le noeud `links` JSON:API d'une ressource ou d'une relation. Contient les liens `self` (URL canonique) et `related` (URL vers la ressource liée). Classe parente de `PaginationResponse`.

---

## Type

model

---

## Dépendances clés

Aucun import externe. Classe autonome implémentant `\JsonSerializable`.

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `LinksResponse` | classe | DTO pour le noeud `links` JSON:API |
| `setSelf(string)` / `getSelf()` | méthodes publiques | Lien canonique vers la ressource courante |
| `setRelated(string\|array)` / `getRelated()` | méthodes publiques | Lien vers la ressource liée |
| `jsonSerialize()` | méthode publique | Retourne le tableau filtré des valeurs non-nulles |

---

## Interactions

**Appelé par :**
- `Api/V8/JsonApi/Helper/RelationshipObjectHelper.php` — pour construire le lien `related` de chaque relation
- `Api/V8/JsonApi/Response/DataResponse.php` — type de `$links`
- `Api/V8/JsonApi/Response/DocumentResponse.php` — type de `$links`
- Étendu par `Api/V8/JsonApi/Response/PaginationResponse.php`

---

## Notes

- `jsonSerialize()` utilise `array_filter()` : les champs non renseignés (`null`) sont exclus de la sortie (ligne 59).
- `$related` peut être une chaîne ou un tableau, selon la spec JSON:API (ligne 16).
