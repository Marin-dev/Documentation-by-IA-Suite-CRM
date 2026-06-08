# ical_server.php

**Chemin :** `ical_server.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour le serveur iCalendar (iCal). Permet à des clients calendriers externes (Outlook, Google Calendar, etc.) de s'abonner au calendrier d'un utilisateur SuiteCRM via le protocole iCal/CalDAV.

**Type :** entrypoint

## Rôle technique

Initialise l'environnement SuiteCRM avec output buffering, charge `entryPoint.php`, puis délègue entièrement au serveur iCal du module via `modules/iCals/Server.php`.

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation complète de SuiteCRM
  - `modules/iCals/Server.php` — logique du serveur iCalendar

## Sorties / Comportement

- Produit une réponse au format iCalendar (`.ics`) consommable par des clients calendriers
- Utilise `ob_start()` pour bufferiser la sortie

## Relations clés

- **Appelé par :** clients calendriers externes (URL d'abonnement iCal)
- **Appelle :** `modules/iCals/Server.php`

---

## Points d'attention

- Toute la logique métier est dans `modules/iCals/Server.php` — ce fichier est un simple relais.
- `ob_start()` est utilisé sans `ob_end_flush()` visible ici — géré dans le module iCals.
