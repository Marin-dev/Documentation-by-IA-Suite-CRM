# Fichier : Filter.php

**Chemin :** `Api/V8/JsonApi/Repository/Filter.php`
**Type :** service
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Traduit les paramètres de filtre JSON:API (tableau `filter[champ][operateur] = valeur`) en clause SQL `WHERE` utilisable dans les requêtes SuiteCRM. Gère les opérateurs de comparaison classiques, les opérateurs logiques AND/OR, et la gestion du flag `deleted`.

---

## Type

service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `\DBManager` (global SuiteCRM) | Injecté dans le constructeur — utilisé pour `quoted()` afin de sécuriser les valeurs dans la clause WHERE |
| `\SugarBean` (global SuiteCRM) | Passé en paramètre de `parseWhere()` pour valider les champs et résoudre les noms de tables |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Filter` | classe | Service de génération de clause SQL WHERE à partir de filtres JSON:API |
| `OP_EQ`, `OP_NEQ`, `OP_GT`, `OP_GTE`, `OP_LT`, `OP_LTE`, `OP_LIKE` | constantes publiques | Opérateurs de comparaison supportés |
| `OP_AND`, `OP_OR` | constantes publiques | Opérateurs logiques supportés |
| `parseWhere(\SugarBean $bean, array $params)` | méthode publique | Retourne une chaîne SQL WHERE à partir des paramètres de filtre |
| `addDeletedParameter(array $params)` | méthode protégée (dépréciée) | Ajoutait automatiquement `deleted=0` si absent — obsolète |

---

## Interactions

**Appelé par :**
- `Api/V8/Param/Options/Filter.php` (seul consommateur identifié dans `Api/`)

**Appelle :**
- `\DBManager::quoted($value)` — escaping SQL de la valeur
- `\SugarBean::getTableName()` — nom de la table principale
- `\SugarBean::get_custom_table_name()` — nom de la table des champs custom
- `\SugarBean::getObjectName()` — nom du module (pour les messages d'erreur)

---

## Notes

- Les champs `custom_fields` (source `custom_fields` dans `field_defs`) sont automatiquement redirigés vers la table custom du bean (ligne 71-72).
- L'opérateur logique par défaut est `AND` si `params['operator']` n'est pas fourni (ligne 41).
- La valeur `deleted` est gérée séparément des autres filtres : elle ne génère pas de clause via `checkOperator` mais contrôle directement le suffixe `AND {table}.deleted = '{0|1}'` (lignes 48-55 et 86-99).
- La méthode `checkOperator()` valide dynamiquement l'opérateur via `defined()` sur les constantes de la classe — toute valeur inconnue lève `\InvalidArgumentException` (ligne 127).
- `addDeletedParameter()` est marquée `@deprecated` (ligne 105).
