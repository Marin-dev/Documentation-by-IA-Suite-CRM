# Fichier : Save.php

**Chemin :** `modules/Meetings/Save.php`
**Type :** controller (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Point d'entree de l'action `Save` du module Meetings. Delegue immediatement le traitement a `MeetingFormBase::handleSave()`.

## Role technique
Script PHP de 3 lignes utiles : inclut `MeetingFormBase.php`, instancie `MeetingFormBase` et appelle `handleSave('', true, false)`. Pas de logique propre.

---

## Dependances cles
- `modules/Meetings/MeetingFormBase.php`

## Exports / Symboles principaux
Aucun symbole exporte. Script d'execution directe.

---

## Relations cles
- **Appele par :** le routeur SuiteCRM (`index.php?module=Meetings&action=Save`)
- **Appelle :** `MeetingFormBase::handleSave()`

---

## Points d'attention
RAS - fichier de delegation pure.
