# SyncInboundEmailAccounts.php

**Chemin :** `modules/Administration/SyncInboundEmailAccounts.php`
**Type :** PHP (point d'entree / orchestration)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Point d'entree de la fonctionnalite "Sync Inbound Email Accounts" dans la section Repair de l'administration. Charge toutes les dependances du sous-module et instancie `SyncInboundEmailAccountsPage`.

## Role technique
Script procedral. Inclut via `include_once` tous les fichiers du sous-module (`Exception`, `Page`, `SubActionHandler`, etc.) plus `ImapHandlerFactory`, puis cree `new SyncInboundEmailAccountsPage(get_defined_vars())`.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/InboundEmail/InboundEmail.php` | Bean email entrant |
| `modules/Emails/Email.php` | Bean email |
| `SyncInboundEmailAccounts/SyncInboundEmailAccountsPage.php` | Page principale |
| `SyncInboundEmailAccounts/SyncInboundEmailAccountsSubActionHandler.php` | Gestion sous-actions |
| `SyncInboundEmailAccounts/SyncInboundEmailAccountsException.php` (et variantes) | Exceptions specialisees |
| `include/Imap/ImapHandlerFactory.php` | Factory IMAP |

## Interactions
- **Appele par :** `index.php?module=Administration&action=SyncInboundEmailAccounts`
- **Delegue vers :** `SyncInboundEmailAccountsPage`, `SyncInboundEmailAccountsSubActionHandler`
