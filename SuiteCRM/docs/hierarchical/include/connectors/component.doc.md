# component.php

**Chemin :** `include/connectors/component.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Classe de composant wrapper pour les connecteurs SuiteCRM. Encapsule une source (`source`) et fournit des methodes de haut niveau pour remplir des beans SuiteCRM (`fillBean()`), mapper les entrees/sorties et interagir avec les sources de donnees externes.

## Role technique

Classe non abstraite avec `$_source` et `$_has_testing_enabled`. `fillBean()` appelle `$source->getItem()` avec les arguments mappes, puis charge les resultats dans le bean via `mapOutput()`. `init()` vide par defaut — les sous-classes peuvent la surcharger.

---

## Dependances cles

- **Imports principaux :**
  - `source` — source de donnees sous-jacente (injectee via `setSource()`)

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `component` | classe | Wrapper de connecteur |
| `fillBean(array, ?string, ?SugarBean): mixed` | methode | Remplit un bean avec les donnees de la source |
| `setSource(source): void` | methode | Injecte la source |
| `getMapping(): array` | methode probable | Retourne le mapping source->bean |

- **Consommateurs identifies :** `ConnectorFactory::getInstance()`, `FilterFactory`, `FormatterFactory`

## Relations cles

- **Appele par :** `ConnectorFactory` (creation), code d'enrichissement des vues Detail
- **Appelle :** `source::getItem()`, methodes de mapping
- **Position dans le flux global :** interface entre la source externe et les beans SuiteCRM

---

## Points d'attention

- Methodes `mapInput()`, `mapOutput()` et `getMapping()` non lues entierement dans ce contexte.
- `fillBean()` peut lancer une `Exception` si les resultats ne peuvent pas etre charges.
