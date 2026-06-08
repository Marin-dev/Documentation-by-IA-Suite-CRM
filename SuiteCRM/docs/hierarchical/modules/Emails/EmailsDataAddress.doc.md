# Fichier : EmailsDataAddress.php

**Chemin :** `modules/Emails/EmailsDataAddress.php`
**Type :** PHP — Helper / DTO
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Construit la structure de donnees d'une adresse expediteur pour le formulaire de composition d'email. Agregation des informations de compte (type, id, adresse from, reply-to, nom, compte sortant, signature).

## Role technique

Classe utilitaire sans etat. La methode principale `getDataArray()` retourne un tableau structure normalise, encode en UTF-8. Instancie `EmailsSignatureResolver` pour resoudre les signatures HTML/texte.

---

## Dependances

- **Instancie :** `EmailsSignatureResolver`
- Aucun import explicite (classe chargee par autoload ou inclusion prealable)

## Exports / Symboles principaux

- `EmailsDataAddress` — classe DTO
  - `getDataArray(type, id, attributesReplyTo, attributesFrom, attributesName, attributesOe, prepend, isPersonalEmailAccount, isGroupEmailAccount, outboundEmailId, outboundEmailName, emailSignaturesArray, accountName, attributesReplyToName)` — construit le tableau d'adresse
  - Structure retournee : `{type, id, name, attributes{reply_to, reply_to_name, from, name, oe}, prepend, isPersonalEmailAccount, isGroupEmailAccount, outboundEmail{id, name}, emailSignatures{html, plain, no_default_available}}`

- **Consommateurs :**
  - `modules/Emails/EmailsDataAddressCollector.php`

## Relations cles

- **Appelle :** `EmailsSignatureResolver`
- **Appele par :** `EmailsDataAddressCollector`
- **Position :** construction du payload JSON des comptes expediteurs pour le compose view

---

## Points d'attention

- Toutes les chaines de caracteres sont converties en UTF-8 depuis ISO-8859-1 via `mb_convert_encoding`.
- `html_entity_decode` est applique sur la signature HTML avant encodage.
