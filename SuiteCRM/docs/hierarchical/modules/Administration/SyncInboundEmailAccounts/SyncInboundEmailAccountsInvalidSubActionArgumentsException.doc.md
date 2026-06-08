# SyncInboundEmailAccountsInvalidSubActionArgumentsException.php

**Chemin :** `modules/Administration/SyncInboundEmailAccounts/SyncInboundEmailAccountsInvalidSubActionArgumentsException.php`
**Type :** PHP (exception)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Exception levee quand une sous-action est appelee avec des arguments invalides. Le message inclut automatiquement le nom de la methode appelante via `debug_backtrace()`.

## Symboles principaux
- Classe `SyncInboundEmailAccountsInvalidSubActionArgumentsException extends Exception`
- `getCallerMethod($step)` — lit la backtrace pour identifier la methode fautive

## Interactions
- **Levee par :** `SyncInboundEmailAccountsSubActionHandler::getRequestedInboundEmailAccounts()` (parametre `ie-sel` absent)
