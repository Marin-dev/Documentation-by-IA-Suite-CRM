# EmailMan.php

**Chemin :** `modules/EmailMan/EmailMan.php`
**Type :** model
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Modèle principal de la file d'envoi de campagnes email. Représente un enregistrement de la table `emailman` : un message à envoyer à un destinataire précis dans le cadre d'une campagne. Gère l'envoi effectif, la validation de l'adresse, les listes de suppression, la journalisation dans `campaign_log`, et les emails de confirmation d'opt-in.

## Type
model

---

## Dépendances clés
- `SugarBean` (classe parente)
- `SugarPHPMailer` — envoi SMTP effectif
- `BeanFactory` — instanciation de CampaignLog, EmailMarketing, EmailTemplates, Emails, InboundEmail, Campaigns, Notes
- `EmailTemplateParser` (`modules/EmailTemplates/EmailTemplateParser.php`) — substitution des variables dans le template
- `Configurator` — vérification de l'opt-in obligatoire
- `LoggerManager` — journalisation
- `TimeDate` — gestion des dates

## Exports / Symboles principaux
| Symbole | Type | Rôle |
|---|---|---|
| `EmailMan` | classe | Entité de la file d'envoi campagne |
| `sendEmail()` | méthode | Envoie un email à un destinataire, gère opt-out/invalid/blocage |
| `set_as_sent()` | méthode | Crée un CampaignLog et supprime ou re-planifie l'entrée emailman |
| `verify_campaign()` | méthode | Vérifie que le marketing et le template sont valides |
| `create_ref_email()` | méthode | Crée/met à jour l'email de référence partagé pour une campagne |
| `create_indiv_email()` | méthode | Crée une copie individuelle d'email archivé par destinataire |
| `addOptInEmailToEmailQueue()` | méthode | Ajoute un email de confirmation opt-in en file |
| `sendOptInEmail()` | méthode | Envoie l'email de confirmation opt-in via SugarPHPMailer |
| `shouldBlockEmail()` | méthode | Détermine si l'envoi doit être bloqué (opt-out, invalide, opt-in non confirmé) |

## Interactions
- **Appelé par :** `EmailManDelivery.php` (script de traitement de file)
- **Appelle :** EmailMarketing, EmailTemplates, InboundEmail, Campaigns, CampaignLog, Emails, Notes, OutboundEmailAccounts

## Notes
- La méthode `sendEmail()` est le cœur du moteur campagne : valide l'adresse, vérifie les listes d'exclusion, substitue les variables de template, gère le tracking pixel et les URLs de désinscription.
- Après 5 tentatives échouées, l'entrée est supprimée de la file.
- Support du mode test (flag `$test`) qui préfixe le sujet et ignore la déduplication.
- `shouldBlockEmail()` vérifie le niveau d'opt-in configuré (`COI_STAT_DISABLED` / `COI_STAT_OPT_IN` / `COI_STAT_CONFIRMED_OPT_IN`).
