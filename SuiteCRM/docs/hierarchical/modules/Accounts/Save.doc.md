# Fichier : Save.php

**Chemin :** `modules/Accounts/Save.php`
**Type :** `PHP`
**Categorie :** controller (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree pour l'action `Save` du module Accounts. Orchestre la sauvegarde d'un enregistrement Account depuis un formulaire POST en delegant toute la logique a `AccountFormBase::handleSave()`.

## Role technique

Script procedural tres court (3 lignes actives). Determine le prefixe de champ (`''` ou `'Accounts'`) selon la presence de `dup_checked` dans la requete (cas de confirmation apres detection de doublon), puis appelle `handleSave`.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `AccountFormBase` | `modules/Accounts/AccountFormBase.php` | Gestion complete de la sauvegarde |

## Relations cles

- **Appele par :** Framework SuiteCRM (routing action=Save, module=Accounts)
- **Appelle :** `AccountFormBase::handleSave()`
- **Position dans le flux :** premier point d'entree HTTP pour la sauvegarde d'un compte

---

## Points d'attention

- Si `$_REQUEST['dup_checked']` est vide : prefixe vide (premiere soumission du formulaire).
- Si `$_REQUEST['dup_checked']` est present : prefixe `'Accounts'` (soumission apres page de doublons).
- La logique reelle (detection doublon, ACL, save, redirect) est entierement dans `AccountFormBase::handleSave()`.
