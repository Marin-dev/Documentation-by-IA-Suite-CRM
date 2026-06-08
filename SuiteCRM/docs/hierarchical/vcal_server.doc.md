# vcal_server.php

**Chemin :** `vcal_server.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour le serveur vCalendar (vCal). Permet à des clients calendriers de synchroniser leurs événements avec SuiteCRM via le protocole vCalendar (format `.vcs`).

**Type :** entrypoint

## Rôle technique

Définit `sugarEntry`, charge l'environnement via `entryPoint.php`, puis délègue entièrement au serveur vCal du module `modules/vCals/Server.php`.

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation complète de SuiteCRM
  - `modules/vCals/Server.php` — logique du serveur vCalendar

## Sorties / Comportement

- Produit une réponse au format vCalendar (`.vcs`) pour les clients compatibles
- Toute la logique est dans `modules/vCals/Server.php`

## Relations clés

- **Appelé par :** clients calendriers compatibles vCalendar (clients plus anciens)
- **Appelle :** `modules/vCals/Server.php`

---

## Points d'attention

- vCalendar est un format plus ancien que iCalendar (iCal) — pour les clients modernes, `ical_server.php` est préféré.
- Structure identique à `ical_server.php` — refactoring possible en point d'entrée commun.
