# Fichier : Folder.php

**Chemin :** `modules/Emails/Folder.php`
**Type :** PHP — Model interne / Helper
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un dossier de messagerie IMAP dans le contexte de la vue liste. Fait le lien entre l'identifiant de dossier SugarCRM (table `folders`) et le compte InboundEmail correspondant.

## Role technique

Pseudo-bean (non SugarBean) avec acces direct a la base de donnees. La methode `retrieve()` remonte l'arbre des dossiers pour trouver le noeud racine (= ID InboundEmail). `loadMailboxFolder()` determine le dossier actif selon la session, les preferences utilisateur ou la requete.

---

## Dependances

- **Utilise :** `DBManagerFactory`, `SuiteValidator`, `SugarFolder`, `$_SESSION`
- **Leve :** `SuiteException`

## Exports / Symboles principaux

- `Folder` — classe pseudo-model
  - `retrieve($folderId)` — charge le dossier depuis la table `folders`, retourne l'ID racine ou null
  - `retrieveFromRequest(array $request)` — charge depuis `$request['folders_id']`, stocke en session
  - `loadMailboxFolder(?array $request)` — determine et charge le dossier actif (session > preferences > defaut)
  - `getType()` / `getId()` / `getMailbox()` — accesseurs
  - `isSelectedForDisplay($folderId)` — verifie si le dossier est affichable
  - `$type` : par defaut "inbound"

- **Consommateurs :**
  - `modules/Emails/include/ListView/ListViewDataEmails.php`
  - `modules/Emails/include/ListView/ListViewDataEmailsSearchOnIMap.php`

## Relations cles

- **Appelle :** `DBManagerFactory`, `SugarFolder::isToDisplay()`, `SugarFolder::getFirstDisplayFolders()`
- **Appele par :** `ListViewDataEmails`
- **Position :** resolution du contexte de dossier avant affichage de la liste emails

---

## Points d'attention

- En legacy, l'ID d'un dossier racine est egalement l'ID du compte InboundEmail — cela cree une confusion entre les deux entites (commentaire ligne 53).
- `$_SESSION['CURRENT_IMAP_MAILBOX_ID']` est utilise pour la persistance du dossier courant entre les requetes.
