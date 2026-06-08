# SearchConfigurator.php

**Chemin :** `lib/Search/SearchConfigurator.php`
**Type :** PHP — Service / Fluent API
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Service de configuration du moteur de recherche actif. Permet de choisir le moteur (BasicSearch, AOD, Elasticsearch) et de sauvegarder la configuration de facon fluide.

## Role technique
Encapsule `Configurator`. Methode `setEngine()` gere le mapping moteur -> controleur : `BasicSearchEngine`/`BasicAndAodEngine` -> controleur `UnifiedSearch`, autres -> `Search`. Methodes fluentes.

---

## Dependances cles
- `Configurator` (modules/Configurator/Configurator.php)
- `InvalidArgumentException` (PHP natif)

## Exports / Symboles principaux
- `SearchConfigurator` — classe
  - `static make(): SearchConfigurator`
  - `setEngine(string $engine): SearchConfigurator`
  - `save(): SearchConfigurator`

## Relations cles
- **Appele par :** INCONNU (probablement depuis l'interface d'administration Recherche)

---

## Points d'attention
- `setEngine('BasicAndAodEngine')` mappe vers le controleur `UnifiedSearch` (ligne 104).
- Les valeurs sont ecrites dans `$configurator->config['search']`.
