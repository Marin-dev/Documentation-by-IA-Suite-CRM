# SyncInboundEmailAccountsException.php

**Chemin :** `modules/Administration/SyncInboundEmailAccounts/SyncInboundEmailAccountsException.php`
**Type :** PHP (exception)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Exception de base pour le sous-module de synchronisation des comptes email entrant. Definit les codes d'erreur.

## Symboles principaux

| Constante | Valeur | Signification |
|---|---|---|
| `UNKNOWN_ERROR` | 100 | Erreur inconnue |
| `PROCESS_OUTPUT_CLEANUP_ERROR` | 110 | Impossible de supprimer le fichier de sortie |
| `PROCESS_OUTPUT_WRITE_ERROR` | 120 | Impossible d'ecrire dans le fichier de sortie |

## Interactions
- **Etendu par :** Les autres exceptions du sous-module (`SyncInboundEmailAccountsEmptyException`, `SyncInboundEmailAccountsNoMethodException`, etc.)
- **Attrapee par :** `SyncInboundEmailAccountsSubActionHandler`
