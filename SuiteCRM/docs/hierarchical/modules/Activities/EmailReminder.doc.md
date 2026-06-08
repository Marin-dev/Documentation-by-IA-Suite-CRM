# EmailReminder.php

**Chemin :** `modules/Activities/EmailReminder.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe envoyant des rappels email aux invités de réunions et d'appels. Charge les beans Meeting, Call, User, Contact, Lead pour récupérer les invités et leur envoyer une notification email avant l'événement.

## Type
service

## Dépendances clés
- `modules/Meetings/Meeting.php`
- `modules/Calls/Call.php`
- `modules/Users/User.php`
- `modules/Contacts/Contact.php`
- `modules/Leads/Lead.php`
- `include/utils.php`

## Exports / Symboles principaux
- `EmailReminder` (classe)
  - Méthodes d'envoi de rappels (INCONNU — lecture partielle)

## Interactions
- **Appelé par :** planificateur (scheduler) de SuiteCRM
- **Appelle :** beans Meeting, Call, User, Contact, Lead

## Notes
- Utilisé par le job scheduler pour les rappels automatiques.
