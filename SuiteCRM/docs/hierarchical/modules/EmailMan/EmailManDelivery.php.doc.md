# EmailManDelivery.php

**Chemin :** `modules/EmailMan/EmailManDelivery.php`
**Type :** controller (script de traitement)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script de traitement de la file d'envoi de campagnes email. Interroge la table `emailman` pour les messages à envoyer (date passée, non en file ou re-tentative après 24h), itère sur les entrées et déclenche l'envoi via `EmailMan::sendEmail()` ou `EmailMan::sendOptInEmail()` selon le type. Gère le mode test et le mode envoi total (`send_all`).

## Type
controller (script inclus, pas de classe)

---

## Dépendances clés
- `SugarPHPMailer` (`include/SugarPHPMailer.php`)
- `EmailMan` (BeanFactory `'EmailMan'`)
- `DBManagerFactory` — requêtes SQL directes
- `TimeDate` — comparaison de dates
- `Configurator` — vérification opt-in
- `OutboundEmailAccounts` — configuration SMTP alternative par campagne
- `AOPInboundEmail` (indirect via EmailImportService)

## Exports / Symboles principaux
- Aucune classe/fonction exportée — script procédural inclus dans le contexte d'exécution SuiteCRM

## Interactions
- **Appelé par :** scheduler SuiteCRM, ou manuellement depuis l'interface Campaigns (action `EmailManDelivery`)
- **Appelle :** `EmailMan::sendEmail()`, `EmailMan::sendOptInEmail()`, `EmailMan::verify_campaign()`

## Notes
- Limite configurable d'emails par run via `Administration::massemailer_campaign_emails_per_run` (défaut : 500).
- En mode test, filtre uniquement les listes de type `test`.
- Support d'un compte d'envoi sortant alternatif par campagne (`outbound_email_id` sur `EmailMarketing`).
- Boucle `do...while` avec `$send_all` pour vider complètement la file si demandé.
- Variable `$_REQUEST['campaign_id']` filtrant la file pour une campagne précise.
