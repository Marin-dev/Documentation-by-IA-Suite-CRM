# EmailImportService.php

**Chemin :** `modules/InboundEmail/Services/EmailImportService.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Service orchestrant l'import des emails depuis les boites de reception configurees dans SuiteCRM. Selectionne le prochain compte InboundEmail a traiter (round-robin ou priorite), connecte le serveur IMAP, importe les messages et met a jour la date du dernier import.

**Type :** service

---

## Dependances cles
- `AOPInboundEmail`
- `ImapHandlerFactory`
- `SuiteValidator` (`SuiteCRM\Utility\SuiteValidator`)
- `Configurator`

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `EmailImportService` | classe | Service d'import email (scheduler) |
| `run()` | methode | Point d'entree principal (retourne bool) |
| `importFromInboundEmailAccount()` | methode protected | Import depuis un compte donne |
| `getNextInboundEmailAccountToImport()` | methode | Selectionne le prochain compte a traiter |
| `updateInboundEmailAccountImportTime()` | methode | MAJ timestamp dernier import |

---

## Interactions
- **Appele par :** scheduler SuiteCRM (`pollMonitoredInboxesAOP`)
- **Appelle :** `AOPInboundEmail`, `ImapHandlerFactory`

---

## Notes
- Traite un seul compte par execution (conception pour eviter les timeouts scheduler).
