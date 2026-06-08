# EmailMan.php

**Chemin :** `modules/EmailMan/EmailMan.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean principal de la file d'envoi en masse (mass emailer). Gere la preparation, l'envoi et la journalisation des emails de campagne pour chaque destinataire. Contient toute la logique metier : validation d'adresse, suppression, opt-out, opt-in confirme, creation d'emails archives.

**Type :** model

---

## Dependances cles
- `SugarBean` (classe parente)
- `SugarPHPMailer` (envoi SMTP)
- `EmailTemplateParser` (`modules/EmailTemplates/EmailTemplateParser.php`)
- `BeanFactory` (Emails, EmailMarketing, EmailTemplates, InboundEmail, Campaigns, CampaignLog, Notes)
- `Configurator` (param `email_enable_confirm_opt_in`)
- `LoggerManager`
- `UploadFile::duplicate_file()`

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `EmailMan` | classe | Bean file d'envoi campagne (table `emailman`) |
| `sendEmail()` | methode | Orchestre l'envoi d'un email a un destinataire unique |
| `set_as_sent()` | methode | Cree un `CampaignLog` et supprime l'entree de la file |
| `create_ref_email()` | methode | Cree/MAJ l'email de reference partage par tous les destinataires |
| `create_indiv_email()` | methode | Cree une copie individuelle archivee de l'email envoye |
| `verify_campaign()` | methode | Verifie qu'un marketing_id possede un template valide |
| `sendOptInEmail()` | methode | Envoie l'email de confirmation double opt-in |
| `addOptInEmailToEmailQueue()` | methode | Ajoute un email opt-in en file |
| `shouldBlockEmail()` | methode protected | Decide si l'email doit etre bloque (opt-out, invalide, niveau opt-in) |
| `valid_email_address()` | methode | Validation syntaxique basique de l'adresse |
| `is_primary_email_address()` | methode | Verifie qu'une adresse est bien l'adresse primaire du bean |

---

## Interactions
- **Appele par :** `EmailManDelivery.php` (script de livraison en boucle), scheduler CRM
- **Appelle :** `EmailTemplateParser`, `InboundEmail`, `CampaignLog`, `Emails`, `Notes`, `Campaigns`

---

## Notes
- La suppression depuis la file (`DELETE FROM emailman`) est physique, pas logique (ligne 498).
- Logique de domaines et adresses restricts chargee par `EmailManDelivery.php` dans `$emailman->restricted_domains` et `$emailman->restricted_addresses`.
- Le mode test (`$this->test = true`) contourne la deduplication par adresse email dans `campaign_log`.
- `send_attempts > 5` force la suppression meme sans `$delete = true`.
