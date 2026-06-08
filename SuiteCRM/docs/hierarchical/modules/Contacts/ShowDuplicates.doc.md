# ShowDuplicates.php

**Chemin :** `modules/Contacts/ShowDuplicates.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de détection et affichage des doublons lors de la création d'un contact. Récupère la liste des contacts potentiellement dupliqués (IDs passés depuis `$_SESSION['SHOW_DUPLICATES']`), affiche un tableau comparatif, et propose à l'utilisateur de créer quand même le contact ou d'annuler. Gère aussi le flux email entrant (inbound email workflow).

**Type :** view (script d'action)

---

## Dépendances clés

- `$_SESSION['SHOW_DUPLICATES']` — données POST serialisées par `ContactFormBase::handleSave()`
- `modules/Contacts/ContactFormBase.php` — `ContactFormBase::buildTableForm()`
- `XTemplate` (template `modules/Contacts/ShowDuplicates.html`)
- `BeanFactory::newBean('Contacts')` — récupération des champs
- `SugarEmailAddress` — widget adresse email vue doublons
- Table `contacts`, `accounts_contacts`, `accounts` — requête JOIN pour les doublons

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

---

## Interactions

**Appelle :**
- `ContactFormBase::buildTableForm($duplicateContacts)` — génère le HTML du tableau comparatif
- `SugarEmailAddress::getEmailAddressWidgetDuplicatesView()` — widget email
- Requête SQL directe sur `contacts LEFT JOIN accounts_contacts LEFT JOIN accounts`

**Appelée par :** `ContactFormBase::handleSave()` lorsqu'un doublon potentiel est détecté — redirection via `header()`.

**Position dans le flux global :** Interception entre la saisie du formulaire contact et la sauvegarde effective ; l'utilisateur décide de continuer ou d'annuler.

---

## Notes

- Les données sont stockées dans `$_SESSION['SHOW_DUPLICATES']` pour contourner les limitations de longueur d'URL des redirections GET.
- Gestion spéciale pour le flux inbound email : si `inbound_email_id` est présent, `RETURN_MODULE='Emails'` et `RETURN_ACTION='EditView'`.
- Appelle `securexss()` sur toutes les données POST récupérées depuis la session (ligne 51).
