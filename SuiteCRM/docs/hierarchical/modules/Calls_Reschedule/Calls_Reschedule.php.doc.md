# Fichier : Calls_Reschedule.php

**Chemin :** `modules/Calls_Reschedule/Calls_Reschedule.php`
**Type :** model
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bean representant un enregistrement d'historique de replanification d'un appel. Chaque fois qu'un appel est replanifie, un enregistrement est cree avec la raison et l'ID de l'appel. Permet de tracker le nombre de tentatives de contact.

## Role technique
Etend `Calls_Reschedule_sugar` qui etend elle-meme `Basic`. La classe est vide (marquee "FOR DEVELOPERS TO MAKE CUSTOMIZATIONS IN"). Toute la logique est dans `Calls_Reschedule_sugar`.

---

## Dependances cles
- `modules/Calls_Reschedule/Calls_Reschedule_sugar.php` — classe parente generee
- `modules/Calls/Call.php` — inclus au meme niveau

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `Calls_Reschedule` | classe | historique replanification appel |

## Table SQL
- `calls_reschedule`

---

## Relations cles
- **Appele par :** `modules/Calls/Reschedule.php` (creation via `BeanFactory::newBean('Calls_Reschedule')`)
- **Lie a :** `Call` via `call_id`

---

## Points d'attention
- Champ principal : `reason` (enum `call_reschedule_dom`) + `call_id` (FK vers `calls`).
