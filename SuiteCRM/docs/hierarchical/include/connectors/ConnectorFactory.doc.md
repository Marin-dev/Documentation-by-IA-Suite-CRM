# ConnectorFactory.php

**Chemin :** `include/connectors/ConnectorFactory.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fabrique principale des connecteurs externes SuiteCRM. Instancie et met en cache les composants de connecteurs, et fournit un utilitaire de chargement de classes de connecteurs a partir de leur identifiant (ex: `ext_soap_hoovers` -> `ext/soap/hoovers.php`).

## Role technique

Classe statique avec cache `$source_map`. `getInstance()` cree un objet `component` encapsulant une `source`. `load()` / `loadClass()` convertissent le nom du connecteur (`_` -> `/`) en chemin de fichier et l'incluent depuis `custom/modules/Connectors/`, `modules/Connectors/` ou `connectors/` (ordre de priorite).

---

## Dependances cles

- **Imports principaux :**
  - `SourceFactory` — creation de la source sous-jacente
  - `component` — wrapper du connecteur

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `ConnectorFactory` | classe statique | Fabrique de connecteurs |
| `getInstance(string): component` | methode statique | Retourne/cree le connecteur cache |
| `load(string, string): void` | methode statique | Charge la classe d'un connecteur |
| `loadClass(string, string): void` | methode statique | Inclut le fichier PHP du connecteur |

- **Consommateurs identifies :** `ConnectorUtils`, `SourceFactory`, `FilterFactory`, `FormatterFactory`

## Relations cles

- **Appele par :** `ConnectorUtils::getSources()`, `FilterFactory::getInstance()`, `SourceFactory::getSource()`
- **Appelle :** `SourceFactory::getSource()`, `component::setSource()`, `component::init()`
- **Position dans le flux global :** point d'entree pour instancier tout connecteur externe

---

## Points d'attention

- Protection anti-traversal de repertoire : `strpos($dir, '..')` verifie que le nom ne contient pas `..` (ligne 87-89).
- Le cache `$source_map` est statique (par processus) — pas de gestion de TTL ni d'invalidation en mode developpeur.
