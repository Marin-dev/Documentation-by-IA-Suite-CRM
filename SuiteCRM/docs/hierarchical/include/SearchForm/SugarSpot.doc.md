# SugarSpot.php

**Chemin :** `include/SearchForm/SugarSpot.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Moteur de recherche globale de SuiteCRM ("Sugar Spot"). Permet de rechercher des enregistrements dans plusieurs modules simultanement depuis la barre de recherche globale de l'application.

## Role technique

Classe de service avec `$module` optionnel (pour restreindre la recherche a un module). Methode principale `searchAndDisplay()` non lue entierement. La protection `sugarEntry` est commentee (ligne 2) — potentiellement accessible sans entrypoint standard.

---

## Dependances cles

INCONNU (methodes non lues dans ce contexte).

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `SugarSpot` | classe | Moteur de recherche globale |
| `searchAndDisplay()` | methode | Execute la recherche et affiche les resultats |

- **Consommateurs identifies :** barre de recherche globale SuiteCRM (INCONNU — probablement via AJAX)

## Relations cles

- **Position dans le flux global :** recherche transversale multi-modules

---

## Points d'attention

- La verification `sugarEntry` est commentee (ligne 2) — le fichier peut etre inclus sans passer par l'entrypoint normal. A verifier si c'est intentionnel ou un oubli securite.
- Corps complet des methodes non lu.
