# Fichier : AcceptDecline.php

**Chemin :** `modules/Contacts/AcceptDecline.php`
**Type :** PHP - Script d'action (acceptation/declination)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Traite la reponse d'un contact a une invitation (appel, reunion). Permet au contact d'accepter ou decliner une invitation depuis un email ou l'interface CRM.

## Role technique

Script procedural. Recupere le bean Contact et met a jour son statut d'acceptation (`accept_status`) pour l'activite concernee (call ou meeting). Peut etre appele avec un `user_id` different pour le cas des invitations externes.

---

## Dependances cles

- `BeanFactory::newBean('Users')` — resolution de l'utilisateur
- Globales : `$beanList`, `$beanFiles`, `$app_strings`, `$current_user`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Liens d'acceptation/declination dans les emails d'invitation CRM

## Relations cles

- **Tables DB modifiees :** `calls_contacts` ou `meetings_contacts` (statut d'acceptation)
- **Position dans le flux :** Reponse a une invitation de reunion/appel

---

## Points d'attention

- Peut recevoir un `user_id` externe dans la requete (l.49) — bypasse le `current_user` habituel.
