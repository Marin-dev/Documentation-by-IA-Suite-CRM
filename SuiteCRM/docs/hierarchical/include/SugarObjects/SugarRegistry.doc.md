# SugarRegistry.php

**Chemin :** `include/SugarObjects/SugarRegistry.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Registre global generique key-value pour SuiteCRM. Permet de stocker et recuperer des objets ou valeurs partages entre differentes parties du code, avec support de namespaces par nom de registre. Peut egalement "exporter" son contenu dans `$GLOBALS` via `addToGlobals()`.

## Role technique

Singleton par nom (namespace) via tableau statique `$_instances`. Utilise les methodes magiques `__get`, `__set`, `__isset`, `__unset` pour un acces transparent aux donnees stockees dans `$_data`.

---

## Dependances cles

Aucune (classe autonome).

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `SugarRegistry` | classe singleton par nom | Registre generique |
| `getInstance(string): SugarRegistry` | methode statique | Retourne/cree le registre nomme |
| `addToGlobals(): void` | methode | Copie le contenu dans `$GLOBALS` |

- **Consommateurs identifies :** INCONNU (usage generique dans SuiteCRM)

## Relations cles

- **Appele par :** INCONNU
- **Appelle :** rien
- **Position dans le flux global :** couche de partage d'etat global

---

## Points d'attention

- `addToGlobals()` peut ecraser des variables globales existantes — a utiliser avec precaution.
- Pas de typage fort : toute valeur est acceptee.
