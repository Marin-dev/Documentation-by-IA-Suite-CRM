# Fichier : reschedule_count.php

**Chemin :** `modules/Calls_Reschedule/reschedule_count.php`
**Type :** helper (logic hook / champ calcule)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe `reschedule_count` utilisee comme logic hook pour calculer et afficher le nombre de tentatives de replanification d'un appel dans la vue liste.

## Role technique
Classe avec methode `count($focus, $event, $args)` qui inclut `modules/Calls/reschedule_history.php` et appelle `reschedule_count($focus, '', '', 'ListView')`.

---

## Dependances cles
- `modules/Calls/reschedule_history.php` — fonction `reschedule_count()`

## Exports / Symboles principaux
- `reschedule_count` — classe — logic hook comptage

---

## Relations cles
- **Appele par :** framework logic hooks SuiteCRM (probablement `process_record` sur Call)
- **Appelle :** `reschedule_count()` (fonction dans `reschedule_history.php`)

---

## Points d'attention
- Enregistrement du hook INCONNU dans ce fichier.
