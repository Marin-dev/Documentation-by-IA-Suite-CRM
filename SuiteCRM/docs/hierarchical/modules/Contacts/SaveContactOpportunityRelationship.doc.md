# SaveContactOpportunityRelationship.php

**Chemin :** `modules/Contacts/SaveContactOpportunityRelationship.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de sauvegarde de la relation Contact-Opportunité avec rôle. Récupère un enregistrement `ContactOpportunityRelationship` existant (ou crée), mappe les champs depuis `$_REQUEST`, sauvegarde et redirige vers la vue de retour.

**Type :** action (script de sauvegarde)

---

## Dépendances clés

- `modules/Contacts/ContactOpportunityRelationship.php` — classe `ContactOpportunityRelationship`
- `safe_map()` — mapping sécurisé des champs POST vers le bean
- `$_REQUEST['record']`, `$_REQUEST['return_action']`, `$_REQUEST['return_module']`, `$_REQUEST['return_id']`

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

---

## Interactions

**Appelle :**
- `new ContactOpportunityRelationship()` puis `retrieve()` / `save()`
- `safe_map()` pour chaque champ de la colonne

**Appelée par :** Soumission du formulaire `ContactOpportunityRelationshipEdit.php`.

**Position dans le flux global :** Sauvegarde du rôle d'un contact dans une opportunité (table `opportunities_contacts`).

---

## Notes

- Utilise `header()` pour la redirection (non `SugarApplication::redirect`) — approche classique.
- La table `opportunities_contacts` désactive la sécurité au niveau des lignes (`disable_row_level_security = true`).
