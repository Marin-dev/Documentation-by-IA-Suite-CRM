# ProcessBouncedEmails.php

**Chemin :** `modules/Campaigns/ProcessBouncedEmails.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Traite les emails bounced (non délivrés) reçus dans la boîte de réception bounce. Identifie l'email campagne grâce à l'identifiant de tracking, crée une entrée de log dans `campaign_log` avec le type `invalid email` ou `send error`, et marque l'adresse email comme invalide si le bounce est permanent (erreur SMTP 5.x.x/550).

## Type

`helper` (bibliothèque de fonctions)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `BeanFactory::newBean('CampaignLog')` | Création des entrées de log |
| `SugarEmailAddress` | Récupération et mise à jour de l'adresse email invalide |
| `LoggerManager::getLogger()` | Journalisation |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `campaign_process_bounced_emails()` | fonction | Point d'entrée principal : analyse l'email bounced et crée le log |
| `retrieveErrorReportAttachment()` | fonction | Extrait le contenu de l'attachement d'erreur (RFC822, delivery-status) |
| `createBouncedCampaignLogEntry()` | fonction | Crée une entrée CampaignLog de type bounce |
| `markBounceEmailAddressInvalid()` | fonction | Marque l'adresse email principale de la cible comme invalide |
| `checkBouncedEmailInvalid()` | fonction | Détecte si le bounce est permanent (status 5.1.1 ou 5.x.x + SMTP 550) |
| `markEmailAddressInvalid()` | fonction | Met à jour `email_addresses.invalid=1` |
| `getExistingCampaignLogEntry()` | fonction | Récupère l'entrée log existante par `target_tracker_key` |
| `checkBouncedEmailForIdentifier()` | fonction | Cherche l'identifiant campaign dans header `X-CampTrackID` ou URL `removeme` |

---

## Interactions

- **Appelé par :** Scheduler `pollMonitoredInboxesForBouncedCampaignEmails` (module InboundEmail)
- **Appelle :** `campaign_log` (lecture/écriture), `email_addresses` (update)
- **Position dans le flux global :** Traitement post-envoi, analyse des retours d'erreur SMTP

---

## Points d'attention

- L'identification de l'email bounced repose sur le header `X-CampTrackID` ou l'URL `removeme` dans le corps — si aucun des deux n'est présent, le bounce est ignoré (ligne 281).
- Le filtre MAILER-DAEMON/POSTMASTER (ligne 239) peut rater certains serveurs non standards.
- Un bounce n'est enregistré qu'une seule fois : si un log `invalid email` ou `send error` existe déjà pour le même tracker, il est ignoré (lignes 258-270).
- La détection d'adresse invalide (RFC 3464) vérifie status 5.1.1 OU code SMTP 550 avec statut 5.x.x (lignes 154-166).
