# 📄 FilterParser.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Parsers/FilterParser.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Parseur de la syntaxe filtre JSON API v1. Transforme les paramètres de requête HTTP (`filter[Module.field]`, `filter[Today]`) en structures de données internes `[module][field][operators+operands]` consommables par `FilterInterpreter`.

## ⚙️ Rôle technique
Méthode principale : `parseFilter(string $filterKey, string $filterValue): array`. Décompose la clé (ex: `Accounts.contacts.name` → arbre `[Accounts][contacts][name]`) et la valeur (ex: `[[eq]]John,[[ne]]Jane` → `['[[eq]]', 'John', '[[ne]]', 'Jane']`). Utilise des propriétés statiques pour les listes d'opérateurs (initialisées depuis le container au premier appel).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Psr\Container\ContainerInterface`
  - `SuiteCRM\API\JsonApi\v1\Filters\Operators\FieldOperator`, `Operator`
  - `SuiteCRM\API\JsonApi\v1\Filters\Validators\FieldValidator`, `FilterValidator`
  - `SuiteCRM\API\v8\Exception\BadRequestException`
  - Services container : `FilterOperators`, `FilterFieldOperators`, `FilterSpecialOperators`

## 📤 Sorties / Exports
- `FilterParser` — classe (service)
  - `parseFilter(string $filterKey, string $filterValue): array` — structure de filtre parsée
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Repositories/FilterRepository.php`

## 🔗 Relations clés
- **Appelé par :** `FilterRepository::fromRequest()`
- **Appelle :** `FieldOperator`, `FieldValidator`, `FilterValidator`
- **Position dans le flux global :** première étape de traitement des filtres HTTP, avant interprétation SQL

---

## 💡 Points d'attention
- Même problème de propriétés statiques partagées entre instances que `FilterInterpreter`.
- La méthode `stringDifference()` utilise `array_diff` sur les caractères — comportement non standard avec des caractères multi-octets (UTF-8 incomplet).
- Si `$filterKey` est vide, la valeur est retournée telle quelle (filtre pré-défini).
