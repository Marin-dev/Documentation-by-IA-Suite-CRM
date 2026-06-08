# Fichier : ProcessBouncedEmails.php

**Chemin :** `modules/Campaigns/ProcessBouncedEmails.php`
**Type :** PHP - Helper (traitement des rebonds email)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Bibliotheque de fonctions pour le traitement des emails rebonds (bounced). Analyse les messages MAILER-DAEMON recus, identifie la campagne source via le header `X-CampTrackID` ou le lien `removeme`, cree des entrees `CampaignLog` de type `invalid email` ou `send error`, et marque les adresses email invalides.

## Role technique

Ensemble de fonctions PHP globales (pas de classe). Utilise des expressions regulieres pour parser les codes de statut SMTP (RFC 3464). Cree des beans `CampaignLog` et `SugarEmailAddress` pour les mises a jour.

---

## Dependances cles

- `BeanFactory::newBean('CampaignLog')` — creation d'entrees de log
- `SugarEmailAddress` — gestion des adresses email invalides
- `LoggerManager::getLogger()` — journalisation

## Exports / Symboles principaux

- `campaign_process_bounced_emails(&$email, &$email_header)` — point d'entree principal : analyse un email rebond (l.231)
- `retrieveErrorReportAttachment(Email $email)` — extrait le rapport d'erreur des pieces jointes (l.57)
- `createBouncedCampaignLogEntry($row, $email, $email_description)` — cree l'entree CampaignLog (l.88)
- `markBounceEmailAddressInvalid(CampaignLog $bounce)` — marque l'adresse email comme invalide (l.119)
- `checkBouncedEmailInvalid($email_description)` — detecte si le rebond est un code 5.x.x permanent (l.137)
- `markEmailAddressInvalid($email_address)` — met a jour `email_addresses.opt_out` (l.174)
- `getExistingCampaignLogEntry($identifier)` — retrouve l'entree log par tracker key (l.192)
- `checkBouncedEmailForIdentifier($email_description)` — recherche l'identifiant dans le contenu (l.209)

## Consommateurs identifies

- Scheduler `pollMonitoredInboxesForBouncedCampaignEmails` (INCONNU : verifier le fichier scheduler)
- `modules/EmailMan` ou processus d'ingestion IMAP

## Relations cles

- **Tables DB modifiees :** `campaign_log`, `email_addresses`
- **Position dans le flux :** Traitement post-reception des bounces email, apres polling IMAP

---

## Points d'attention

- La detection d'invalidite est basee sur le code SMTP 550 + statut 5.x.x (RFC 3464) — ne couvre pas tous les cas de rebond.
- Ne cree pas de doublon si un `invalid email` ou `send error` existe deja pour le meme `target_tracker_key` (l.258-269).
- `retrieveErrorReportAttachment` assume un encodage `quoted-printable` pour les pieces jointes de type `message/rfc822`.
