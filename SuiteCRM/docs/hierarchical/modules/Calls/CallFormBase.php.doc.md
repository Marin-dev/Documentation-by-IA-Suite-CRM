# Fichier : CallFormBase.php

**Chemin :** `modules/Calls/CallFormBase.php`
**Type :** controller / helper formulaire
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe de base pour les formulaires de creation et d'edition d'appels. Equivalent de `MeetingFormBase` pour le module Calls. Fournit le rendu HTML du formulaire et le traitement de la soumission avec gestion des invites.

## Role technique
Etend `FormBase`. Methodes `getFormBody()`, `getForm()` pour le rendu HTML. `handleSave()` pour le traitement POST, gestion des invites (users, contacts, leads) et sauvegarde via `Call::save()`. Logique identique a `MeetingFormBase::handleSave()`.

---

## Dependances cles
- `FormBase` (`include/SugarObjects/forms/FormBase.php`)
- `BeanFactory::newBean('Calls')`
- `populateFromPost()` (`include/formbase.php`)
- `vCal::cache_sugar_vcal()`
- `ACLController`

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `CallFormBase` | classe | formulaire et sauvegarde appels |
| `handleSave()` | methode | traitement POST et sauvegarde |

---

## Relations cles
- **Appele par :** `Save.php` (Calls)
- **Appelle :** `Call::save()`, `vCal::cache_sugar_vcal()`

---

## Points d'attention
- Logique identique a `MeetingFormBase` — voir documentation de ce fichier pour les details.
