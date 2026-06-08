# Fichier : EmailsControllerActionGetFromFields.php

**Chemin :** `modules/Emails/EmailsControllerActionGetFromFields.php`
**Type :** PHP — Service / Handler d'action
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Orchestre la construction de la liste des comptes expediteurs disponibles pour la vue de composition d'email. Supporte deux modes : legacy (InboundEmail) et nouveau (OutboundEmailAccounts).

## Role technique

Classe service avec injection de `User` et `EmailsDataAddressCollector`. Deux methodes publiques : `handleActionGetFromFields()` (mode legacy via InboundEmail) et `getOutboundFromFields()` (mode nouveau via OutboundEmailAccounts). Retourne du JSON encode en ISO-8859-1.

---

## Dependances

- **Imports :**
  - `include/SugarEmailAddress/SugarEmailAddress.php`
  - `EmailsSignatureResolver`, `EmailsDataAddress`, `EmailsDataAddressCollector`
- **Injecte dans constructeur :** `User $currentUser`, `EmailsDataAddressCollector $collector`
- **Instancie :** `OutboundEmailAccounts` via `BeanFactory`

## Exports / Symboles principaux

- `EmailsControllerActionGetFromFields` — classe handler
  - `handleActionGetFromFields(Email $email, InboundEmail $ie)` — mode legacy, retourne JSON
  - `getOutboundFromFields(Email $email)` — mode OutboundEmailAccounts, retourne JSON
  - Structure JSON retournee : `{"data": [DataAddress, ...]}`

- **Consommateurs :**
  - `modules/Emails/EmailsController.php::action_getFromFields()`

## Relations cles

- **Appelle :** `EmailsDataAddressCollector::collectDataAddressesFromIEAccounts()`, `collector::addSystemEmailAddress()`, `OutboundEmailAccounts::getUserOutboundAccounts()`
- **Appele par :** `EmailsController::action_getFromFields()`
- **Position :** handler intermediaire entre le controleur et le collecteur d'adresses

---

## Points d'attention

- Le choix entre les deux modes (`handleActionGetFromFields` vs `getOutboundFromFields`) est fait dans `EmailsController` selon `$sugar_config['legacy_email_behaviour']`.
- L'encodage de retour est ISO-8859-1 (ligne 109) pour compatibilite client JS legacy.
- `getOutboundFromFields` peut logger une erreur fatale si `json_encode` echoue (ligne 134).
