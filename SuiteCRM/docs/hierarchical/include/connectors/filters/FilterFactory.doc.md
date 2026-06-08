# FilterFactory.php

**Chemin :** `include/connectors/filters/FilterFactory.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fabrique de filtres pour les connecteurs. Un filtre transforme ou valide les donnees avant qu'elles ne soient passees au bean SuiteCRM. Utilise un filtre specifique au connecteur si disponible, sinon le filtre par defaut.

## Role technique

Classe statique avec cache `$filter_map`. Cherche un fichier de filtre specifique dans `modules/Connectors/connectors/filters/` avant de tomber sur `default_filter`. Associe le filtre au composant connecteur via `setComponent()`.

---

## Dependances cles

- **Imports principaux :**
  - `filter` (`include/connectors/filters/default/filter.php`) — classe de base filtre
  - `ConnectorFactory` — chargement et instance du composant

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `FilterFactory` | classe statique | Fabrique de filtres |
| `getInstance(string, string): filter` | methode statique | Retourne/cree le filtre cache |

- **Consommateurs identifies :** INCONNU (utilise lors de la mise en correspondance de donnees connecteur)

## Relations cles

- **Appele par :** INCONNU — typiquement lors de l'application d'un mapping de connecteur
- **Appelle :** `ConnectorFactory::load()`, `ConnectorFactory::getInstance()`
- **Position dans le flux global :** transformation des donnees entre source externe et bean SuiteCRM

---

## Points d'attention

- RAS — classe simple, logique de fallback claire.
