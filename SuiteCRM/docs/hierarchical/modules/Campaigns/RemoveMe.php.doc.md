# Fichier : RemoveMe.php

**Chemin :** `modules/Campaigns/RemoveMe.php`
**Type :** PHP - Script d'action (desinscription)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Traite les demandes de desinscription (opt-out) des destinataires de campagnes. Appele quand un contact/lead clique sur le lien "Se desinscrire" dans un email de campagne. Met a jour l'adresse email en opt-out global ou desabonne le contact d'une newsletter specifique.

## Role technique

Script procedural. Utilise l'`identifier` de la requete pour retrouver la cible via `log_campaign_activity()`. Selon le contexte : desinscription globale (UPDATE sur `email_addresses.opt_out`) ou desinscription specifique a la campagne via `unsubscribe()`. Les utilisateurs ne peuvent pas se desabonner.

---

## Dependances cles

- `modules/Campaigns/utils.php` — `log_campaign_activity()`, `unsubscribe()`
- `DBManagerFactory` — UPDATE direct sur `email_addresses`
- Globales : `$beanFiles`, `$beanList`, `$current_user`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Lien `entryPoint=removeme&identifier=...` dans les emails de campagne
- `modules/Campaigns/ProcessBouncedEmails.php` (detection de ce lien dans les bounces)

## Relations cles

- **Tables DB modifiees :** `email_addresses` (opt_out=1), `prospect_lists_prospects` (desabonnement)
- **Appelle :** `log_campaign_activity()`, `unsubscribe()`
- **Position dans le flux :** Fin du parcours de desinscription d'un destinataire

---

## Points d'attention

- Si `target_type == 'Users'`, affiche un message d'avertissement sans appliquer l'opt-out (l.70-72).
- Charge `$current_user` = admin (id=1) si non connecte, pour bypasser les restrictions d'equipe (l.60-63).
- L'UPDATE direct sur `email_addresses` affecte TOUTES les relations du bean (opt-out global), pas seulement la campagne courante.
