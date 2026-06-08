# Fichier : Save.php (Contacts)

**Chemin :** `modules/Contacts/Save.php`
**Type :** PHP - Script d'action (sauvegarde)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree pour la sauvegarde d'un contact. Delegue entierement la logique a `ContactFormBase::handleSave()`. Gere la detection de doublons via le prefixe `Contacts`.

## Role technique

Script procedural ultra-court. Instancie `ContactFormBase`, determine le prefixe selon `$_REQUEST['dup_checked']`, puis appelle `handleSave($prefix, true, false)`.

---

## Dependances cles

- `modules/Contacts/ContactFormBase.php` — `ContactFormBase::handleSave()`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural de 3 lignes utiles.

## Consommateurs identifies

- Formulaire HTML POST depuis les vues EditView et QuickCreate du module Contacts

## Relations cles

- **Appelle :** `ContactFormBase::handleSave()`
- **Position dans le flux :** Entree POST -> ContactFormBase -> Contact::save()

---

## Points d'attention

- Si `dup_checked` est vide (premiere soumission), le prefixe est vide — la detection de doublons est active.
- Si `dup_checked` est defini (doublon confirme), le prefixe est `'Contacts'` pour bypasser la verification.
