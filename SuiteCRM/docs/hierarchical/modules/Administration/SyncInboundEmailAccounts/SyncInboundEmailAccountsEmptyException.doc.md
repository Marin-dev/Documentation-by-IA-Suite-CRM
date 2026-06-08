# SyncInboundEmailAccountsEmptyException.php

**Chemin :** `modules/Administration/SyncInboundEmailAccounts/SyncInboundEmailAccountsEmptyException.php`
**Type :** PHP (exception)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Exception levee quand aucun email ou compte IMAP n'est trouve lors de la synchronisation.

## Symboles principaux
- Classe `SyncInboundEmailAccountsEmptyException extends Exception` — pas de membres additionnels.

## Interactions
- **Levee par :** `SyncInboundEmailAccountsSubActionHandler::select()` (aucun resultat SQL), `getEmailIdsOfInboundEmail()`
- **Attrapee par :** `SyncInboundEmailAccountsSubActionHandler::action_Sync()` (affiche message "pas d'emails")
