# Fichier : Status.php

**Chemin :** `modules/Emails/Status.php`
**Type :** PHP — Vue legacy (statut d'envoi)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche le statut d'un email envoye : succes ou erreur. Vue legacy utilisant XTemplate.

## Role technique

Script procedural. Recupere l'email par `$_REQUEST['record']`, affiche le statut via un template HTML `Status.html`.

---

## Dependances

- **Globales :** `$mod_strings`, `$app_strings`, `$current_user`
- **Utilise :** `BeanFactory::newBean('Emails')`, `XTemplate`, `getClassicModuleTitle()`

## Exports / Symboles principaux

- Aucun — script d'affichage uniquement

## Relations cles

- **Appele par :** URL `index.php?module=Emails&action=Status&record={id}`

---

## Points d'attention

- Vue legacy XTemplate — maintenue pour compatibilite.
