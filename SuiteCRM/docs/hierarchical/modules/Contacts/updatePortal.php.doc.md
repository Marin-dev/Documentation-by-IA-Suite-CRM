# Fichier : updatePortal.php

**Chemin :** `modules/Contacts/updatePortal.php`
**Type :** PHP - Hook logique (mise a jour portail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe hook utilisee pour synchroniser les modifications d'un contact (acces portail, informations) avec le portail Joomla/AOP. Appelee apres la sauvegarde d'un contact pour mettre a jour les permissions portail.

## Role technique

Classe `updatePortal`. Methode `updateUser(Contact $bean)` : si AOP est actif et que `joomla_account_access` est defini, envoie une mise a jour a l'API Joomla via `file_get_contents()`. Requiert `modules/AOP_Case_Updates/util.php`.

---

## Dependances cles

- `modules/AOP_Case_Updates/util.php` — `isAOPEnabled()`
- `$sugar_config['aop']['joomla_url']`
- Champ `Contact::joomla_account_access`

## Exports / Symboles principaux

- `updatePortal` — classe
  - `updateUser(Contact $bean)` — synchronise le contact avec le portail (l.53)

## Consommateurs identifies

- Logic hook `after_save` sur le module Contacts (INCONNU : fichier de hook exact)

## Relations cles

- **Appelle :** API Joomla/AOP via HTTP
- **Position dans le flux :** After_save -> synchronisation portail

---

## Points d'attention

- Ne s'execute que si `joomla_account_access` est defini et non vide (l.59).
- `file_get_contents()` synchrone — peut ralentir la sauvegarde du contact si le portail est lent.
