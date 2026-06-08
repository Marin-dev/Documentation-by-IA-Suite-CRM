# ical_server.php

**Chemin :** `ical_server.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée HTTP pour le serveur iCalendar (iCal). Permet aux clients de calendrier externes (Outlook, Google Calendar, Apple Calendar…) de récupérer les événements SuiteCRM au format iCal (RFC 5545).

## Responsabilités
- Définir `sugarEntry` pour autoriser l'accès aux composants internes
- Initialiser l'environnement via `include/entryPoint.php`
- Déléguer la gestion de la requête iCal à `modules/iCals/Server.php`

## Dépendances internes
- `include/entryPoint.php` — bootstrap global
- `modules/iCals/Server.php` — logique du serveur iCalendar (génération du flux iCal)

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `GET /ical_server.php`
- Retourne un flux au format `text/calendar` (iCal)

## Notes techniques
- `ob_start()` est appelé avant le chargement de l'entryPoint pour éviter tout output accidentel avant les en-têtes HTTP.
- INCONNU : paramètres d'authentification acceptés par `modules/iCals/Server.php` (token URL ? session ?).
