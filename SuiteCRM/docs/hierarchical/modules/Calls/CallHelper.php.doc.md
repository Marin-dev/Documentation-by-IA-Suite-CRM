# Fichier : CallHelper.php

**Chemin :** `modules/Calls/CallHelper.php`
**Type :** helper (fonctions utilitaires)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Fournit des fonctions utilitaires pour les formulaires d'appels : rendu HTML du dropdown de duree en minutes, et rendu du dropdown de temps de rappel (deprecated).

## Role technique
Deux fonctions globales PHP :
- `getDurationMinutesOptions($focus, $field, $value, $view)` : construit le `<select>` des minutes de duree (0/15/30/45). Retourne la valeur brute en vue non-edit.
- `getReminderTime($focus, $field, $value, $view)` : deprecated depuis 6.5.0. Construit le `<select>` du temps de rappel.

---

## Dependances cles
- `$timedate` (global) — valeurs par defaut date/heure
- `get_select_options_with_id()` — rendu options HTML

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `getDurationMinutesOptions()` | fonction | dropdown minutes duree appel |
| `getReminderTime()` | fonction (deprecated) | dropdown temps rappel |

---

## Relations cles
- **Appele par :** vardef/field type `function` dans editviewdefs des Calls (INCONNU exactement sans lire editviewdefs)
- **Appelle :** `get_select_options_with_id()`

---

## Points d'attention
- `getReminderTime()` marque `@deprecated 6.5.0` — ne pas utiliser dans les nouvelles fonctionnalites.
