# Fichier : TeamDemoData.php

**Chemin :** `install/TeamDemoData.php`
**Type :** installer (classe donnees demo equipes)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Definit la classe `TeamDemoData` qui cree les equipes de demonstration dans SuiteCRM lors de l'installation. Utilise les memes GUIDs de seed que `UserDemoData` pour maintenir la coherence des relations utilisateurs-equipes.

## Role technique
Classe PHP avec proprietes `$_team`, `$_large_scale_test`, et un tableau `$guids` identique a celui de `UserDemoData` (seed_jim_id, etc.). Structure symetrique a `UserDemoData` pour la creation d'equipes.

---

## Dependances cles
- **Imports principaux :** INCONNU (methodes non lues)
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `TeamDemoData` | classe — creation des equipes de demonstration |
| `TeamDemoData::$guids` | tableau — meme mapping que UserDemoData |

## Interactions
- **Appele par :** `install/populateSeedData.php` (ligne 55)
- **Appelle :** INCONNU (probablement API Teams/SecurityGroups)

---

## Notes
- Pas de garde `sugarEntry` visible dans les 60 premieres lignes — verifier si elle est presente plus loin.
- `#[\AllowDynamicProperties]` — compatibilite PHP 8.2+.
- Les equipes et utilisateurs partagent les memes GUIDs de seed pour que les relations puissent etre etablies lors de la generation.
