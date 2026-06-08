# Fichier : EmailValidatorException.php

**Chemin :** `modules/Emails/EmailValidatorException.php`
**Type :** PHP — Exception metier
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Exception specifique au validateur d'adresse email. Levee par `EmailFromValidator` lors de problemes internes de validation (bean non initialise, erreur regex).

## Role technique

Herite de `Exception` PHP. Definit trois codes d'erreur lies a l'etat interne du validateur.

---

## Dependances

- Aucune import explicite

## Exports / Symboles principaux

- `EmailValidatorException` — classe exception
  - `EMAIL_IS_NOT_SET` (1) : le bean Email n'a pas ete injecte dans le validateur
  - `PREG_MATCH_ERROR_AT_FROMADDRNAME` (2) : erreur regex lors de la validation from_addr_name
  - `EMAIL_ISNT_EMAILOBJ` (3) : l'objet injecte n'est pas une instance de Email

- **Consommateurs :**
  - `modules/Emails/EmailFromValidator.php`
  - `modules/Emails/EmailsDataAddressCollector.php`

## Relations cles

- **Appele par :** `EmailFromValidator`, `EmailsDataAddressCollector`

---

## Points d'attention

- RAS
