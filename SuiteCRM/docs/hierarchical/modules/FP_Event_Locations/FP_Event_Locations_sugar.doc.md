# Fichier : FP_Event_Locations_sugar.php

**Chemin :** `modules/FP_Event_Locations/FP_Event_Locations_sugar.php`
**Type :** PHP — modele genere (SugarBean)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Classe de base generee par Module Builder pour le module Lieux d'evenements (FP_Event_Locations). Represente un lieu physique ou virtuel pouvant etre associe a un evenement FP_events. Ne doit pas etre modifie directement.

## Role technique
Etend `Basic`. Table : `fp_event_locations`. Champs standard : `id`, `name`, `description`, `assigned_user_id`, etc. Implements ACL. `disable_row_level_security = true`.

---

## Dependances cles
- `Basic` — classe parente SugarBean

## Exports / Symboles principaux
- `class FP_Event_Locations_sugar extends Basic`
- `bean_implements('ACL')` — retourne true

## Relations cles
- **Etendu par :** `modules/FP_Event_Locations/FP_Event_Locations.php` (classe de customisation)
- **Appele par :** BeanFactory, vues module

---

## Points d'attention
- Classe generee — toute customisation doit etre faite dans `FP_Event_Locations.php`.
