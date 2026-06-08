# Fichier : Sort.php

**Chemin :** `Api/V8/JsonApi/Repository/Sort.php`
**Type :** service
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Traduit le paramètre de tri JSON:API (`sort=champ` ou `sort=-champ` pour DESC) en clause SQL `ORDER BY` utilisable dans les requêtes SuiteCRM. Valide l'existence du champ dans le bean avant de générer la clause.

---

## Type

service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `\SugarBean` (global SuiteCRM) | Passé en paramètre pour validation du champ de tri via `field_defs` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Sort` | classe | Service de génération de clause SQL ORDER BY à partir du paramètre `sort` JSON:API |
| `ORDER_BY_ASC` | constante publique | Valeur `'ASC'` |
| `ORDER_BY_DESC` | constante publique | Valeur `'DESC'` |
| `parseOrderBy(\SugarBean $bean, string $value)` | méthode publique | Retourne une chaîne `"{champ} ASC\|DESC"` |

---

## Interactions

**Appelé par :**
- `Api/V8/Param/Options/Sort.php` (seul consommateur identifié dans `Api/`)

**Appelle :**
- `\SugarBean::getObjectName()` — pour les messages d'erreur uniquement

---

## Notes

- Convention JSON:API respectée : un préfixe `-` dans la valeur indique un tri descendant (ligne 22-24).
- Le tri multiple n'est pas supporté à ce stade, selon le commentaire du code (ligne 14 : "We don't support multiple sorting. for now.").
- Lève `\InvalidArgumentException` si le champ n'existe pas dans `field_defs` du bean (ligne 28-33).
