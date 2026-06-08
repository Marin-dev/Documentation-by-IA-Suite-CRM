# emailmandelivery.php

**Chemin :** `emailmandelivery.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée pour le déclenchement de la livraison des emails en masse gérés par le module EmailMan (Email Manager). Sert de wrapper d'initialisation pour l'envoi planifié de campagnes email.

**Type :** entrypoint

## Rôle technique

Définit `sugarEntry`, charge l'environnement via `entryPoint.php`, inclut le module de livraison `EmailManDelivery.php` (qui contient la logique métier d'envoi), puis appelle `sugar_cleanup()`.

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation complète de SuiteCRM
  - `modules/EmailMan/EmailManDelivery.php` — logique d'envoi des emails de campagne en masse

## Sorties / Comportement

- Délègue entièrement la logique à `EmailManDelivery.php`
- Appelle `sugar_cleanup()` après l'exécution

## Relations clés

- **Appelé par :** INCONNU (probablement via un job planifié ou le scheduler SuiteCRM)
- **Appelle :** `modules/EmailMan/EmailManDelivery.php`

---

## Points d'attention

- Fichier très simple (3 lignes de logique) — toute la complexité est dans `EmailManDelivery.php`.
- Contrairement à `cron.php`, ne vérifie pas si l'exécution est en CLI — pourrait théoriquement être appelé via HTTP si le serveur web est mal configuré.
