# Fichier : Subscriptions.php

**Chemin :** `modules/Campaigns/Subscriptions.php`
**Type :** PHP - Script de vue (gestion des abonnements)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere l'affichage et la mise a jour des abonnements aux newsletters pour un contact, lead ou prospect. Permet a l'utilisateur de s'abonner ou se desabonner des campagnes newsletter disponibles.

## Role technique

Script procedural. Charge les campagnes de type NewsLetter actives, affiche les statuts d'abonnement via `get_subscription_lists()` depuis `utils.php`. Traite le POST de mise a jour via `process_subscriptions()` et `subscribe()`/`unsubscribe()`. Requiert `modules/Campaigns/utils.php`.

---

## Dependances cles

- `modules/Campaigns/utils.php` — `get_subscription_lists()`, `process_subscriptions()`, `subscribe()`, `unsubscribe()`
- `BeanFactory` — Contacts, Leads, Prospects
- Globales : `$mod_strings`, `$app_list_strings`, `$app_strings`, `$current_user`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Sous-panel "Abonnements aux newsletters" dans les vues detail de Contacts/Leads/Prospects
- Action `Subscriptions` du module Campaigns

## Relations cles

- **Appelle :** `get_subscription_lists()`, `subscribe()`, `unsubscribe()` (utils.php)
- **Tables DB modifiees :** `prospect_lists_prospects` (via subscribe/unsubscribe)
- **Position dans le flux :** Gestion des preferences d'abonnement d'un destinataire

---

## Points d'attention

- Affiche les campagnes selon le module du record (`return_module` : Contacts, Leads ou Prospects).
