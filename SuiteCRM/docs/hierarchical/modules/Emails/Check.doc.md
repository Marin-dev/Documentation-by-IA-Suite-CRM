# Fichier : Check.php

**Chemin :** `modules/Emails/Check.php`
**Type :** PHP — Script d'action (verification email)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Declenche la verification manuelle des emails entrants. Selon le parametre `type` (personal ou group), importe les messages des comptes IMAP personnels ou de groupe, puis redirige vers la vue liste appropriee.

## Role technique

Script procédural (non-classe). Utilise `InboundEmail::importMessages()` pour chaque compte. Pour le mode group, interroge directement la base de donnees pour lister les comptes de groupe actifs.

---

## Dependances

- **Globales :** `$current_user`
- **Utilise :** `BeanFactory::newBean('InboundEmail')`, `User::hasPersonalEmail()`, `InboundEmail::retrieveByGroupId()`, `InboundEmail::importMessages()`

## Exports / Symboles principaux

- Aucun — script de traitement uniquement

## Relations cles

- **Appele par :** URL directe `index.php?module=Emails&action=Check&type=personal|group`
- **Position :** declencheur manuel de synchronisation IMAP

---

## Points d'attention

- La requete SQL du mode `group` (ligne 62) interroge directement `inbound_email` JOIN `users` sans passer par l'ORM.
- Pas de gestion d'erreur si `importMessages()` echoue — redirection systematique.
