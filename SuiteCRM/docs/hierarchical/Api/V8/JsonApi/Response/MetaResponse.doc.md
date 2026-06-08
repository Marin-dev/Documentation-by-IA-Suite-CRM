# Fichier : MetaResponse.php

**Chemin :** `Api/V8/JsonApi/Response/MetaResponse.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Objet de valeur générique représentant le noeud `meta` JSON:API. Accepte un tableau ou un `stdClass` de propriétés arbitraires via les méthodes magiques `__get`/`__set`. Sert de classe de base à `AttributeResponse` et `RelationshipResponse`.

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
| `MetaResponse` | classe | Conteneur de propriétés dynamiques sérialisable en JSON |
| `__construct($properties)` | méthode publique | Initialise les propriétés depuis un tableau ou `stdClass` |
| `__get(string $name)` | méthode magique | Lit une propriété dynamique |
| `__set(string $name, mixed $value)` | méthode magique | Écrit une propriété dynamique |
| `jsonSerialize()` | méthode publique | Retourne le tableau interne `$properties` |

---

## Interactions

**Étendu par :**
- `Api/V8/JsonApi/Response/AttributeResponse.php`
- `Api/V8/JsonApi/Response/RelationshipResponse.php`

**Instancié par :**
- `Api/V8/JsonApi/Helper/PaginationObjectHelper.php` — pour les méta-données de pagination
- `Api/V8/JsonApi/Response/DocumentResponse.php` — message par défaut si réponse vide

---

## Notes

- Les propriétés sont stockées dans `$properties` (tableau privé) et exposées via `__get`/`__set`, grâce à l'attribut `#[\AllowDynamicProperties]` sur les classes enfants.
- Lève `\InvalidArgumentException` si les propriétés passées ne sont ni un tableau ni un `stdClass` (ligne 20-22).
- La sérialisation retourne directement `$properties`, donc seules les valeurs assignées via `__set` ou le constructeur sont présentes dans la sortie JSON.
