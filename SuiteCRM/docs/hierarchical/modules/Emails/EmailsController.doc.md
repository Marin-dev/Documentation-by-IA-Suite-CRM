# Fichier : EmailsController.php

**Chemin :** `modules/Emails/EmailsController.php`
**Type :** PHP — Controller (SugarController)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Controleur principal du module Emails. Traite toutes les actions HTTP du module : affichage de la liste, composition, envoi, sauvegarde de brouillon, suppression, import depuis IMAP, reponse/transfert, gestion des dossiers et des pièces jointes.

## Role technique

Herite de `SugarController`. Chaque methode `action_*` correspond a une action du routeur SuiteCRM. Utilise `BeanFactory` pour instancier les beans, `EmailsDataAddressCollector` et `EmailsControllerActionGetFromFields` pour construire les listes d'expediteurs, et valide les droits d'acces avant tout envoi.

---

## Dependances

- **Imports :**
  - `SugarControllerException` (`include/Exceptions/SugarControllerException.php`)
  - `EmailsDataAddressCollector` (`modules/Emails/EmailsDataAddressCollector.php`)
  - `EmailsControllerActionGetFromFields` (`modules/Emails/EmailsControllerActionGetFromFields.php`)
  - `SuiteValidator` (`SuiteCRM\Utility\SuiteValidator`)
  - `BeanFactory`, `DBManagerFactory`, `ControllerFactory` (globaux SuiteCRM)
  - `OutboundEmail`, `OutboundEmailAccounts`, `InboundEmail` (beans)

## Exports / Symboles principaux

- `EmailsController` — classe controleur
  - Constantes d'erreur : `ERR_INVALID_INBOUND_EMAIL_TYPE` (100), `ERR_STORED_OUTBOUND_EMAIL_NOT_SET` (101), etc.
  - Constantes de mode composition : `COMPOSE_BEAN_MODE_REPLY_TO` (1), `COMPOSE_BEAN_MODE_REPLY_TO_ALL` (2), `COMPOSE_BEAN_MODE_FORWARD` (3), `COMPOSE_BEAN_WITH_PDF_TEMPLATE` (4)
  - Actions publiques :
    | Action | Vue resultante | Description |
    |---|---|---|
    | `action_index` | list | Liste des emails |
    | `action_ComposeView` | compose | Formulaire de composition |
    | `action_send` | sendemail / ajax | Envoi d'email |
    | `action_SaveDraft` | savedraftemail | Sauvegarde brouillon |
    | `action_DeleteDraft` | deletedraftemail | Suppression brouillon |
    | `action_getFromFields` | ajax | Champs expediteur (JSON) |
    | `action_GetDraftAttachmentData` | ajax | Donnees pieces jointes |
    | `action_CheckEmail` | ajax | Synchronisation IMAP |
    | `action_GetFolders` | ajax | Dossiers utilisateur |
    | `action_DisplayDetailView` | detailnonimported / redirect | Affichage email IMAP |
    | `action_ImportAndShowDetailView` | redirect | Import + affichage |
    | `action_ImportFromListView` | redirect | Import en masse |
    | `action_ReplyTo` / `action_ReplyToAll` / `action_Forward` | compose | Reponse/transfert |
    | `action_MarkEmails` | ajax | Marquer emails (lu/non-lu) |
    | `action_DeleteFromImap` | ajax / redirect | Suppression sur serveur IMAP |
    | `action_QuickCreate` | ajax | Creation rapide depuis modal |

- `$doNotImportFields` — champs proteges lors de l'import

## Relations cles

- **Appelle :** `Email::send()`, `Email::sendFromOutbound()`, `Email::save()`, `InboundEmail::syncEmail()`, `InboundEmail::returnImportedEmail()`, `EmailsDataAddressCollector`, `EmailsControllerActionGetFromFields`
- **Appele par :** routeur SuiteCRM via `controller.php` / `modules/Emails/controller.php`
- **Position :** point d'entree de toutes les requetes HTTP du module Emails

---

## Points d'attention

- La methode `userIsAllowedToSendEmail()` effectue une verification multi-criteres (acces au compte entrant, correspondance adresse from, acces compte sortant). Un log securite est emis en cas de refus.
- Le mode legacy `legacy_email_behaviour` dans `$sugar_config` conditionne le chemin `handleActionGetFromFields` vs `getOutboundFromFields`.
- `action_QuickCreate` modifie temporairement `$_REQUEST['module']` — risque de side-effect si exception levee.
- La methode `composeBean()` charge et manipule `$this->bean` directement, ce qui peut poser probleme si le bean n'est pas pre-charge.
- `$doNotImportFields` protege contre l'injection de champs sensibles lors de l'import.
