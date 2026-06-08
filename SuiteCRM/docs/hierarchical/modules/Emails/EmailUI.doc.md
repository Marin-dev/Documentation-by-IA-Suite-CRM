# Fichier : EmailUI.php

**Chemin :** `modules/Emails/EmailUI.php`
**Type :** PHP — Service central (UI et logique email)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe utilitaire centrale pour l'interface email de SuiteCRM. Gere l'affichage des frames email (inbox, compose), la gestion des dossiers IMAP, la distribution des emails de groupe, la recherche de contacts, et les utilitaires de templates. C'est le moteur de la fonctionnalite email legacy (Email 2.0).

## Role technique

Classe non-SugarBean avec acces direct a la DB. Utilise YUI Tree (`include/ytree/`) pour l'arbre des dossiers, SugarFolders, Smarty pour le rendu. Contient une requete SQL template `$coreDynamicFolderQuery` pour les dossiers dynamiques.

---

## Dependances

- **Imports :**
  - `include/utils.php`
  - `include/ytree/Tree.php`, `include/ytree/ExtNode.php`
  - `include/SugarFolders/SugarFolders.php`
  - `SuiteCRM\Utility\SuiteValidator`
- **Utilise :** `BeanFactory`, `Sugar_Smarty`, `DBManagerFactory`, `SugarFolder`, `LoggerManager`

## Exports / Symboles principaux

- `EmailUI` — classe service
  - `displayEmailFrame($baseTpl)` — affiche la frame principale email
  - `displayQuickComposeEmailFrame()` — frame compose rapide
  - `generateComposePackageForQuickCreate(...)` — package compose pour modal
  - `populateComposeViewFields(...)` — peuple les champs du compose
  - `getDraftAttachments($ret)` — recupere les pieces jointes d'un brouillon
  - `getMailboxNodes(...)` — construit l'arbre des dossiers IMAP
  - `markEmails($type, $ieId, $folder, $uids)` — marque des emails (lu/non-lu/flagge)
  - `doAssignment(...)` — distribution des emails de groupe
  - `getDetailViewForEmail2($emailId)` — vue detail email
  - `handleReplyType($email, $type)` — prepare une reponse/transfert
  - `displayComposeEmail($email)` — prepare le compose
  - `getFromAllAccountsArray($ie, $ret)` — liste des comptes expediteurs (legacy)
  - Distribution : `distRoundRobin()`, `distLeastBusy()`, `distDirect()`
  - `getUserPreferencesJS()` / `getUserPrefsJS()` — preferences utilisateur en JS
  - `$coreDynamicFolderQuery` — requete SQL template pour les dossiers dynamiques

- **Consommateurs :**
  - `modules/Emails/Compose.php`
  - `modules/Emails/GenerateQuickComposeFrame.php`
  - `modules/Emails/EmailsController.php`

## Relations cles

- **Appelle :** `SugarFolder`, `InboundEmail`, `BeanFactory`, `Email`
- **Appele par :** `Compose.php`, `GenerateQuickComposeFrame.php`, de nombreuses actions legacy
- **Position :** coeur du systeme email legacy (Email 2.0) — tres large perimetre fonctionnel

---

## Points d'attention

- Fichier tres volumineux (2700+ lignes) — couvre un large spectre fonctionnel herite.
- `$cacheTimeouts` : messages caches 24h, dossiers 5min, pieces jointes 24h.
- `$appendTick = false` peut etre utilise pour desactiver le tick de l'icone compose.
- Co-existence avec le nouveau systeme MVC (`EmailsController`) — certaines methodes sont dupliquees ou deprecees.
