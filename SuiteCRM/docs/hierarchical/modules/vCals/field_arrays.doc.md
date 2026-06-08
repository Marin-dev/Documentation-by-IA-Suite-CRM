# Fichier : field_arrays.php

**Chemin :** `modules/vCals/field_arrays.php`
**Type :** PHP — configuration (tableau de champs)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Declare les colonnes de la table `vcals` utilisees pour le cache. Champs : `id`, `user_id`, `date_modified`, `type`, `content`, `source`, `deleted`.

## Parametres cles
- `$fields_array['vcal']['column_fields']` : champs persistes en DB pour le cache vCal/freebusy

## Impacte par / impacte
- Consomme par le framework SugarCRM (caching)
- Lie a `modules/vCals/vardefs.php` et `modules/vCals/vCal.php`

## Points d'attention
- Fichier de configuration standard.
