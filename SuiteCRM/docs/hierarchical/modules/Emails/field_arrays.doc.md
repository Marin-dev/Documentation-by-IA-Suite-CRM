# Fichier : field_arrays.php

**Chemin :** `modules/Emails/field_arrays.php`
**Type :** PHP — Configuration (champs de cache)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit les tableaux de champs utilises par le bean Email pour le cache et les vues liste. Deux sous-tableaux : `column_fields` (champs stockes en base) et `list_fields` (champs affiches en liste).

## Role technique

Script de configuration non-classe. Remplit `$fields_array['Email']` avec les deux listes de champs.

---

## Exports / Symboles principaux

- `$fields_array['Email']['column_fields']` — champs persistance (id, dates, adresses, type, status, intent, etc.)
- `$fields_array['Email']['list_fields']` — champs vue liste (id, name, parent, dates, adresses, type, status, etc.)

## Relations cles

- **Consomme par :** bean `Email` (heritage `Basic`/`SugarBean`) pour la construction des requetes

---

## Points d'attention

- RAS
