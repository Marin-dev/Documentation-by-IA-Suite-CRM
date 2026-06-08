# Fichier : Save.php

**Chemin :** `modules/Calls/Save.php`
**Type :** controller (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Point d'entree de l'action `Save` du module Calls. Delegue a `CallFormBase::handleSave()`.

## Role technique
3 lignes utiles : inclut `CallFormBase.php`, instancie `CallFormBase`, appelle `handleSave('', true, false)`.

---

## Relations cles
- **Appele par :** routeur SuiteCRM (`index.php?module=Calls&action=Save`)
- **Appelle :** `CallFormBase::handleSave()`

---

## Points d'attention
RAS.
