# Save.php

**Chemin :** `modules/Contacts/Save.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Script de sauvegarde d'un contact. Instancie `ContactFormBase` et délègue la sauvegarde avec gestion des doublons.

## Type

`helper` (action script)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `modules/Contacts/ContactFormBase.php` | Classe de sauvegarde formulaire |

---

## Exports / Symboles principaux

Aucune classe ni fonction exportée — script procédural.

---

## Interactions

- **Appelé par :** Formulaire HTML vue édition Contact (POST)
- **Appelle :** `ContactFormBase::handleSave()`

---

## Points d'attention

- Le préfixe est `'Contacts'` si `dup_checked` est présent dans la requête (mode doublon détecté), sinon vide — gestion des formulaires dupliqués.
