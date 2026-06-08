# emailmandelivery.php

**Chemin :** `emailmandelivery.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée pour le traitement de livraison des emails en masse (Email Man / campagnes). Initialise l'environnement SuiteCRM, déclenche la livraison des emails en attente, puis nettoie les ressources.

## Responsabilités
- Définir `sugarEntry` pour autoriser l'accès aux composants internes
- Charger l'environnement complet via `include/entryPoint.php`
- Inclure et exécuter `modules/EmailMan/EmailManDelivery.php` (logique de distribution des emails)
- Appeler `sugar_cleanup()` pour libérer les connexions et ressources

## Dépendances internes
- `include/entryPoint.php` — bootstrap global
- `modules/EmailMan/EmailManDelivery.php` — moteur de livraison des campagnes email

## Exports / Points d'entrée
- Script exécuté en tant que tâche planifiée (cron) ou point d'entrée HTTP direct.
- Aucun export PHP.

## Notes techniques
- Ce fichier est typiquement invoqué par le planificateur de tâches SuiteCRM (Schedulers) ou via cron OS.
- INCONNU : fréquence de déclenchement configurée dans le module Schedulers — à vérifier dans `modules/Schedulers/`.
