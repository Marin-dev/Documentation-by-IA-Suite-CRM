# SyncInboundEmailAccountsSubActionHandler.php

**Chemin :** `modules/Administration/SyncInboundEmailAccounts/SyncInboundEmailAccountsSubActionHandler.php`
**Type :** PHP (service / handler)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Gere la logique de synchronisation des comptes email entrant IMAP. En mode `index` : liste les comptes actifs. En mode `sync` : pour chaque compte selectionne, se connecte au serveur IMAP, recalcule les UID et le flag "orphane" de chaque email, et sauvegarde.

## Role technique
Classe `SyncInboundEmailAccountsSubActionHandler`. Lit `$_REQUEST['method']` pour dispatcher. La synchronisation connecte au serveur IMAP via `InboundEmail::connectMailserver()`, lit les headers IMAP, calcule un MD5 compose (message_id + delivered-to), compare avec les emails stockes en BDD, met a jour `uid` et `orphaned` sur chaque `Email` bean. La sortie est ecrite dans un fichier HTML intermediaire (`sync_output.html`).

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `SyncInboundEmailAccountsSubActionHandler` | Classe | Handler de sous-actions |
| `PROCESS_OUTPUT_FILE` | Constante | Chemin fichier sortie HTML temporaire |
| `action_Index()` | Methode | Affiche la liste des comptes IMAP actifs |
| `action_Sync()` | Methode | Execute la synchronisation pour les comptes selectionnes |
| `getEmailHeadersOfIMAPServer($ie)` | Methode | Connexion IMAP + lecture headers |
| `getCompoundMessageIdMD5($ie, $uid)` | Methode | Calcule MD5(message_id + delivered-to) |
| `isOrphanedEmail($e, $IMAPHeaders)` | Methode | Determine si un email n'existe plus sur le serveur |
| `getEmailIdsOfInboundEmail($ieId)` | Methode | Emails BDD associes a un compte IMAP |

## Interactions
- **Instancie par :** `SyncInboundEmailAccountsPage`
- **Appelle :** `InboundEmail::connectMailserver()`, `InboundEmail::getImap()`, `BeanFactory::getBean('Emails')`, `BeanFactory::getBean('InboundEmail')`
- **Ecrit dans :** `modules/Administration/SyncInboundEmailAccounts/sync_output.html`

---

## Notes
- `set_time_limit(0)` pendant la synchronisation (ligne 217) — peut durer longtemps.
- `SuiteValidator::isValidId($ieId)` verifie le format de l'ID IMAP (securite, ligne 351).
- Le fichier de sortie intermediaire est nettoye avant et apres chaque sync (`cleanup()`).
- `getCompoundMessageIdMD5()` : la condition `if (strlen($compoundMessageId) > 255)` est commentee (ligne 471) mais le MD5 est systematiquement applique.
