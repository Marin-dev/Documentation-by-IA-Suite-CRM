# Fichier : ContactFormBase.php

**Chemin :** `modules/Contacts/ContactFormBase.php`
**Type :** PHP - Helper (formulaire Contact)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe de base pour les formulaires Contact. Gere la sauvegarde, la detection de doublons, et la generation des formulaires de creation rapide et de conversion de leads. Centralise la logique metier des formulaires Contact.

## Role technique

Etend `PersonFormBase` (`include/SugarObjects/forms/PersonFormBase.php`). Implemente `getDuplicateQuery()` pour la detection de doublons sur nom/prenom. Fournit `getWideFormBody()` pour le rendu du formulaire de contact large. Herite de `handleSave()` depuis `PersonFormBase`.

---

## Dependances cles

- `include/SugarObjects/forms/PersonFormBase.php` — classe parente
- `DBManagerFactory::getInstance()` — sanitisation SQL
- `ACLController::checkAccess()` — controle d'acces

## Exports / Symboles principaux

- `ContactFormBase` — classe
  - `getDuplicateQuery($focus, $prefix)` — retourne la requete SQL de detection de doublons (l.70)
  - `getWideFormBody($prefix, $mod, $formname, $contact, $portal)` — rendu HTML du formulaire large (l.97)

## Consommateurs identifies

- `modules/Contacts/Save.php`
- `modules/Contacts/ContactsQuickCreate.php`
- INCONNU : verifier les usages lors de la conversion de leads

## Relations cles

- **Appele par :** `Save.php`, `ContactsQuickCreate.php`
- **Appelle :** `PersonFormBase::handleSave()`, `getDuplicateQuery()`
- **Position dans le flux :** Traitement des formulaires POST avant `Contact::save()`

---

## Points d'attention

- La detection de doublons cherche par `last_name` obligatoire et `first_name` optionnel (l.81-87).
- `getWideFormBody` retourne `''` si l'utilisateur n'a pas le droit `edit` sur Contacts (l.99-100).
