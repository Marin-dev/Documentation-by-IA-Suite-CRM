# Fichier : RelationshipObjectHelper.php

**Chemin :** `Api/V8/JsonApi/Helper/RelationshipObjectHelper.php`
**Type :** helper
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Construit l'objet `relationships` JSON:API d'un `SugarBean` en listant toutes ses relations disponibles et en générant les liens correspondants. Chaque relation est représentée par un objet `links.related` pointant vers l'endpoint `/relationships/{nom_relation}`.

---

## Type

helper

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\Helper\VarDefHelper` | Fournit la liste de toutes les relations du bean via `getAllRelationships()` |
| `Api\V8\JsonApi\Response\LinksResponse` | Construit l'objet `links` de chaque relation |
| `Api\V8\JsonApi\Response\RelationshipResponse` | Objet de retour global pour toutes les relations |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `RelationshipObjectHelper` | classe | Helper injectable pour la construction du noeud `relationships` JSON:API |
| `getRelationships(\SugarBean $bean, string $uriPath)` | méthode publique | Retourne un `RelationshipResponse` contenant les liens vers toutes les relations du bean |

---

## Interactions

**Appelé par :**
- `Api/V8/Service/ModuleService.php`
- `Api/V8/Service/UserService.php`
- `Api/V8/Service/ListViewService.php`
- `Api/V8/Service/ListViewSearchService.php`

**Appelle :**
- `VarDefHelper::getAllRelationships(\SugarBean $bean)` — récupère le tableau `[relationshipName => module]`
- `Api\V8\JsonApi\Response\LinksResponse::setRelated()` — définit l'URL de la relation
- `Api\V8\JsonApi\Response\RelationshipResponse` — constructeur

**Enregistré comme service dans :**
- `Api/V8/Config/services/helpers.php`
- `Api/V8/Config/services/services.php`

---

## Notes

- Les relations sont triées avec `asort()` avant d'être dédupliquées avec `array_unique()` (lignes 33-36).
- L'URL générée suit le pattern `{uriPath}/relationships/{relationshipName}` (ligne 39).
- La clé du tableau de résultat est le nom du module (pas de la relation), ce qui peut causer des conflits si deux relations pointent vers le même module : seule la dernière serait conservée via `$relationshipsLinks[$module]` (ligne 43). Point d'attention potentiel.
