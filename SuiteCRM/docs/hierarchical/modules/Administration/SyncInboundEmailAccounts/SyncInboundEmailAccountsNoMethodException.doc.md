# SyncInboundEmailAccountsNoMethodException.php

**Chemin :** `modules/Administration/SyncInboundEmailAccounts/SyncInboundEmailAccountsNoMethodException.php`
**Type :** PHP (exception)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Exception levee quand une sous-action non supportee est demandee dans le handler de synchronisation.

## Symboles principaux
- Classe `SyncInboundEmailAccountsNoMethodException extends Exception` — pas de membres additionnels.

## Interactions
- **Levee par :** `SyncInboundEmailAccountsSubActionHandler::__construct()` (action inconnue dans le switch)
