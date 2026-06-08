# SugarDependentDropdown.php

**Chemin :** `include/SugarDependentDropdown/SugarDependentDropdown.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle

Gère les listes déroulantes dépendantes (cascadées) dans les formulaires SuiteCRM. Permet de définir des ensembles de champs dont les valeurs disponibles dépendent de la sélection d'un autre champ parent (select, input, checkbox).

## Responsabilités

- Charger et parser un fichier de métadonnées PHP décrivant la structure des dropdowns dépendants (tableau `$sugarDependentDropdown`)
- Initialiser chaque élément en fusionnant avec les valeurs par défaut (`$defaults`)
- Valider la cohérence des métadonnées (types valides, handlers présents pour chaque valeur)
- Gérer récursivement les sous-éléments "handlers" (mini-éléments enfants d'un élément)
- Exposer la structure préparée dans `$this->metadata` prête à être encodée en JSON pour le front-end

## Dépendances internes

- Fonction utilitaire `sugarArrayMerge()` (helper global SuiteCRM) — fusion des tableaux de métadonnées

## Exports / Points d'entrée

- `SugarDependentDropdown` — classe PHP
  - `__construct(string $metadata = '')` — constructeur, appelle `init()` si le chemin est fourni
  - `init(string $metadata)` — charge le fichier de métadonnées et prépare `$this->metadata`
  - `isValidElement(array $element)` — vérifie qu'un élément contient les champs requis (`name`, `id`)
  - `initElement(array $element, array $alwaysMerge)` — fusionne les défauts et initialise récursivement les handlers
  - `verifyMetadata(array $metadata)` — valide la cohérence complète de la structure (types, handlers)
  - `debugOutput(mixed $v)` — affiche un dump HTML pour débogage (activé via `$debugMode = true`)
  - `$metadata` — propriété publique contenant la structure finale prête pour JSON
  - `$debugMode` — flag permettant d'activer les logs de débogage

## Notes techniques

- Les types valides sont : `select`, `input`, `checkbox`, `none`, `multiple`
- Le fichier de métadonnées est inclus via `include()` et doit exposer un tableau `$sugarDependentDropdown`
- Les handlers sont des mini-éléments récursifs ; `verifyMetadata()` les vérifie via un faux conteneur `$fakeMetadata`
- Les éléments sont triés par clé (`ksort`) avant initialisation pour garantir l'ordre
- Le fichier exemple de métadonnées est `include/SugarDependentDropdown/metadata/dependentDropdown.php`
