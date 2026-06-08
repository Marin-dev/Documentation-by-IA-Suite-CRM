# Fichier : EmailException.php

**Chemin :** `modules/Emails/EmailException.php`
**Type :** PHP — Exception metier
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit l'exception specifique au module Emails pour les erreurs liees a l'adresse expediteur (from). Utilisee lors de la validation et de l'envoi des emails.

## Role technique

Herite de `Exception` PHP. Ajoute des constantes de codes d'erreur metier specifiques a la configuration de l'expediteur.

---

## Dependances

- Aucune import explicite (herite de `Exception` natif PHP)

## Exports / Symboles principaux

- `EmailException` — classe exception
  - `NO_DEFAULT_FROM_ADDR` (10) : aucune adresse expediteur par defaut
  - `NO_DEFAULT_FROM_EMAIL` (20) : aucun email expediteur par defaut
  - `NO_DEFAULT_FROM_NAME` (25) : aucun nom expediteur par defaut
  - `NO_PROBLEM_MSG_FOUND` (30) : aucun message de probleme trouve

- **Consommateurs :**
  - `modules/Emails/Email.php` (ligne 493) — levee si l'erreur saveAndStoreInSent n'est jamais lue

## Relations cles

- **Appele par :** `Email`, `NonGmailSentFolderHandler`
- **Position :** couche exception du domaine email

---

## Points d'attention

- Les codes d'erreur sont numerotes dans les plages 10-30 pour ne pas chevaucher ceux de `EmailValidatorException` (plage 1-3).
