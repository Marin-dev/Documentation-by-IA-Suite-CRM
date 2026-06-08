# Fichier : UserDemoData.php

**Chemin :** `install/UserDemoData.php`
**Type :** installer (classe donnees demo utilisateurs)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Definit la classe `UserDemoData` qui cree les utilisateurs de demonstration dans SuiteCRM lors de l'installation. Six utilisateurs predetermines sont crees : jim, sarah, sally, max, will, chris.

## Role technique
Classe PHP avec proprietes `$_user`, `$_large_scale_test`, et un tableau `$guids` mappant les noms d'utilisateurs a des GUIDs de seed (`seed_jim_id`, etc.). Ces GUIDs fixes permettent la reproductibilite des relations entre demo data.

---

## Dependances cles
- **Imports principaux :** INCONNU (non lus — methodes de la classe)
- **Globaux :** INCONNU
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `UserDemoData` | classe — creation des utilisateurs de demonstration |
| `UserDemoData::$guids` | tableau — mapping nom->GUID seed pour les 6 utilisateurs |

**Utilisateurs de demo :** jim, sarah, sally, max, will, chris (avec GUIDs seed_*_id).

## Interactions
- **Appele par :** `install/populateSeedData.php` (ligne 54)
- **Appelle :** INCONNU (probablement API User/BeanFactory)

---

## Notes
- Le code commente (lignes 57-60) montre des GUIDs full-UUID planifies mais non implementes — cette approche a ete remplacee par des GUIDs de seed symboliques.
- `$_large_scale_test` suggere un mode de test a grande echelle (INCONNU : detail de fonctionnement).
- `#[\AllowDynamicProperties]` indique compatibility PHP 8.2+.
