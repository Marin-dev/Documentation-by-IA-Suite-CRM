# Fichier : Reschedule.php

**Chemin :** `modules/Calls/Reschedule.php`
**Type :** controller (action de replanification)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Traite la replanification d'un appel : met a jour la date/heure de debut, recalcule la date de fin, et enregistre un historique de la tentative de replanification via `Calls_Reschedule`.

## Role technique
Script PHP (~67 lignes). Lit les donnees POST (`call_id`, `date`, `reason`, `date_start_hours`, `date_start_minutes`, `date_start_meridiem`). Reconstruit `date_start` selon le format utilisateur. Recupere le bean Call, le met a jour, puis cree un bean `Calls_Reschedule` avec la raison. Deux appels a `$call->save()` (un pour `date_start`, un pour `date_end`).

---

## Dependances cles
- `modules/Calls_Reschedule/Calls_Reschedule.php`
- `modules/Calls/Call.php`
- `TimeDate` — formatage date/heure utilisateur
- `BeanFactory::newBean('Calls_Reschedule')`

## Exports / Symboles principaux
Aucun. Script d'execution directe.

---

## Relations cles
- **Appele par :** INCONNU (action du module Calls, probablement via popup ou AJAX)
- **Appelle :** `Call::save()`, `Calls_Reschedule::save()`

---

## Points d'attention
- Deux appels consecutifs a `$call->save()` — potentielle optimisation.
- La date_end est calculee en PHP natif via `strtotime()` (pas via `TimeDate`) — peut causer des problemes de timezone.
- Ne verifie pas le retour de `$call->retrieve()` au-dela de `null`.
