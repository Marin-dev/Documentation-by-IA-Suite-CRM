# Fichier : EmailsDataAddressCollector.php

**Chemin :** `modules/Emails/EmailsDataAddressCollector.php`
**Type :** PHP — Service / Collecteur
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Collecte et formate la liste complete des adresses expediteur disponibles pour l'utilisateur courant lors de la composition d'un email. Agregation de : comptes InboundEmail autorises, adresses personnelles utilisateur, compte systeme SMTP.

## Role technique

Classe avec injection du `User` courant et de la config Sugar. Methode principale `collectDataAddressesFromIEAccounts()` itere sur les comptes entrants, valide chaque compte (OutboundEmail, storedOptions), construit les DataAddress via `EmailsDataAddress`. Integre aussi les adresses personnelles (`email_allow_send_as_user`) et le compte systeme.

---

## Dependances

- **Injecte dans le constructeur :** `User $currentUser`, `array $sugarConfig`
- **Instancie :** `EmailsDataAddress`, `EmailFromValidator`, `OutboundEmail`, `SugarEmailAddress`
- **Utilise :** `BeanFactory`, `LoggerManager`, `SuiteCRM\Utility\SuiteValidator`
- **Variables d'environnement :** `$sugar_config['email_allow_send_as_user']`

## Exports / Symboles principaux

- `EmailsDataAddressCollector` — classe service
  - `collectDataAddressesFromIEAccounts(ieAccounts, showFolders, prependSignature, emailSignatures, defaultEmailSignature)` — retourne tableau de DataAddress
  - `addSystemEmailAddress(array &$dataAddresses)` — ajoute l'adresse systeme (methode publique)
  - Constantes d'erreur : `ERR_INVALID_INBOUND_EMAIL_TYPE` (201), `ERR_STORED_OUTBOUND_EMAIL_NOT_SET` (202), `ERR_STORED_OUTBOUND_EMAIL_ID_IS_INVALID` (203), `ERR_REPLY_TO_ADDR_NOT_FOUND` (204), etc.

- **Consommateurs :**
  - `modules/Emails/EmailsControllerActionGetFromFields.php`

## Relations cles

- **Appelle :** `EmailsDataAddress`, `EmailFromValidator`, `OutboundEmail::getSystemMailerSettings()`, `SugarEmailAddress::getAddressesByGUID()`
- **Appele par :** `EmailsControllerActionGetFromFields`
- **Position :** agregation des sources d'expedition pour le compose view

---

## Points d'attention

- Si un compte de groupe (`isGroupEmailAccount`) n'a pas `allow_outbound_group_usage = true`, il est exclu de la liste (ligne 158).
- La validation du `SuiteValidator::isValidId()` est inversee dans `getOutboundEmailOrError()` (ligne 218) : verifie que l'ID est valide pour lever une erreur — comportement contre-intuitif.
- Les erreurs de configuration ne bloquent pas le flux : elles sont loguees et les valeurs de fallback des `storedOptions` sont utilisees.
