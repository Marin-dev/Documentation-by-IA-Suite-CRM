# SyncInboundEmailAccountsIMapConnectionException.php

**Chemin :** `modules/Administration/SyncInboundEmailAccounts/SyncInboundEmailAccountsIMapConnectionException.php`
**Type :** PHP (exception)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Exception levee quand la connexion au serveur IMAP echoue lors de la synchronisation.

## Symboles principaux
- Classe `SyncInboundEmailAccountsIMapConnectionException extends Exception` — pas de membres additionnels.

## Interactions
- **Levee par :** `SyncInboundEmailAccountsSubActionHandler::getEmailHeadersOfIMAPServer()` (echec `connectMailserver`)
- **Attrapee par :** `action_Sync()` (affiche message d'erreur de connexion, loggue en warn)
