# 📄 FilterInterpreter.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interpreters/FilterInterpreter.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Orchestrateur principal de la conversion des filtres JSON API en clauses SQL WHERE. Il détermine le type de filtre (par ID, par nom pré-défini, ou par attributs) et délègue à l'interpréteur approprié.

## ⚙️ Rôle technique
Classe avec trois méthodes publiques principales :
- `isFilterById()` / `isFilterByPreMadeName()` / `isFilterByAttributes()` — détection du type de filtre
- `getFilterById()`, `getFilterByPreMadeName()`, `getFilterByAttributes()` — conversion en SQL

La méthode `getFilterByAttributes()` est la plus complexe : elle parcourt `[module][field][operators+operands]` et utilise `FieldOperator`, `Operator`, et les opérateurs enregistrés dans le container pour construire la clause SQL. Gère les champs personnalisés (`_cstm`) via `isCustomField()`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Psr\Container\ContainerInterface`
  - `SuiteCRM\API\JsonApi\v1\Filters\Operators\FieldOperator`
  - `SuiteCRM\API\JsonApi\v1\Filters\Operators\Operator`
  - `SuiteCRM\API\JsonApi\v1\Filters\Validators\FieldValidator`
  - `SuiteCRM\API\JsonApi\v1\Filters\Interpreters\ByIdFilters\ByIdFilter`
  - `SuiteCRM\API\v8\Exception\BadRequestException`
  - `SuiteCRM\Utility\StringValidator`
  - Services container : `FilterOperators`, `FilterFieldOperators`, `FilterSpecialOperators`, `ByPreMadeFilterInterpreters`, `ByIdFilterInterpreter`

## 📤 Sorties / Exports
- `FilterInterpreter` — classe (service)
  - `isFilterById(array): bool`
  - `isFilterByPreMadeName(array): bool`
  - `isFilterByAttributes(array): bool`
  - `getFilterById(array): string`
  - `getFilterByPreMadeName(array): string`
  - `getFilterByAttributes(array, array $args): string`
- **Consommateurs identifiés :** INCONNU directement (probablement utilisé depuis `lib/API/v8/`)

## 🔗 Relations clés
- **Appelé par :** INCONNU (probablement contrôleurs v8)
- **Appelle :** `ByIdFilter`, `FieldOperator`, `Operator`, `FieldValidator`, `\BeanFactory`

---

## 💡 Points d'attention
- Les propriétés statiques `$filterOperators`, `$filterFieldOperators`, `$filterSpecialOperators` sont partagées entre instances (initialisées une seule fois) — attention aux effets de bord en tests.
- La gestion de `Behat\Gherkin\Filter\FilterInterface` dans l'import semble être une erreur de copier-coller (ligne 43 : import d'une bibliothèque de test BDD dans du code de production).
- `isCustomField()` appelle `\BeanFactory::newBean()` — requiert la BD.
