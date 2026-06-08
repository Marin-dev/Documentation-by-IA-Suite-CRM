# vcal_server.php

**Chemin :** `vcal_server.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée HTTP pour le serveur vCalendar (vCal). Permet aux clients de calendrier externes de récupérer les événements SuiteCRM au format vCalendar (précurseur de iCal).

## Responsabilités
- Définir `sugarEntry` pour autoriser l'accès aux composants internes
- Charger l'environnement via `include/entryPoint.php`
- Déléguer le traitement à `modules/vCals/Server.php`

## Dépendances internes
- `include/entryPoint.php` — bootstrap global
- `modules/vCals/Server.php` — logique du serveur vCalendar

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `GET /vcal_server.php`
- Retourne un flux au format vCalendar

## Notes techniques
- Analogue à `ical_server.php` mais pour le format vCal (plus ancien).
- INCONNU : différences fonctionnelles entre vCal et iCal dans l'implémentation SuiteCRM — à vérifier dans `modules/vCals/` vs `modules/iCals/`.
