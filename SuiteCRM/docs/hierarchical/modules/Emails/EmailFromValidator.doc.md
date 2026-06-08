# Fichier : EmailFromValidator.php

**Chemin :** `modules/Emails/EmailFromValidator.php`
**Type :** PHP — Helper / Validateur
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Valide la coherence des champs expediteur d'un bean Email avant l'envoi : verifie que `From`, `from_addr`, `FromName`, `from_name` et `from_addr_name` sont correctement renseignes et coherents entre eux.

## Role technique

Classe autonome avec injection du bean `Email`. La methode principale `isValid()` orchestre cinq validations independantes. Les erreurs sont accumulees dans un tableau et peuvent etre recuperees sous forme de codes numeriques ou de textes localises (via `LangText`).

---

## Dependances

- **Imports :**
  - `modules/Emails/Email.php`
  - `modules/Emails/EmailValidatorException.php`
  - `SuiteCRM\LangText` (textes localises)

## Exports / Symboles principaux

- `EmailFromValidator` — classe validateur
  - `isValid(Email $email, $tryToFix = true)` — valide tous les champs expediteur, retourne bool
  - `getErrors()` — retourne les codes d'erreur (vide le buffer)
  - `getErrorsAsText()` — retourne les erreurs en texte localise
  - Constantes ERR_FIELD_* (1-22) : codes de validation granulaires pour chaque champ
  - Constantes EX_ERROR_CODE_* (100-101) : erreurs internes d'implementation

- **Consommateurs :**
  - `modules/Emails/Email.php` (envoi)
  - `modules/Emails/EmailsDataAddressCollector.php` (validation reply-to)

## Relations cles

- **Appelle :** `isValidEmailAddress()` (helper global), `LangText::get()`
- **Appele par :** `Email` (avant envoi), `EmailsDataAddressCollector`
- **Position :** barriere de validation avant transmission SMTP

---

## Points d'attention

- Les validations de `To`, `CC`, `BCC` sont commentees (lignes 115-117) — pas encore implementees.
- `$tryToFix = true` ne fait actuellement rien de special (ligne 120-121) — la correction automatique n'est pas implementee.
- Cinq champs sont valides pour la meme adresse expediteur (duplication legacy From/from_addr, FromName/from_name, from_addr_name).
