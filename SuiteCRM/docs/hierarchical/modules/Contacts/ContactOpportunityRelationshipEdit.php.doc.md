# Fichier : ContactOpportunityRelationshipEdit.php

**Chemin :** `modules/Contacts/ContactOpportunityRelationshipEdit.php`
**Type :** PHP - Script de vue (edition relation)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche le formulaire d'edition du role d'un contact dans une opportunite. Permet de modifier le champ `contact_role` de la relation Contact-Opportunite.

## Role technique

Script procedural. Instancie `ContactOpportunityRelationship`, charge l'enregistrement si `record` est present, et affiche le formulaire d'edition.

---

## Dependances cles

- `modules/Contacts/ContactOpportunityRelationship.php`
- Globales : `$app_strings`, `$app_list_strings`, `$mod_strings`, `$sugar_config`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Lien "Modifier le role" dans le sous-panel Opportunities d'un contact

## Relations cles

- **Soumet vers :** `SaveContactOpportunityRelationship.php`
- **Position dans le flux :** Edition du role Contact dans une Opportunite

---

## Points d'attention

- Utilise la classe legacy `ContactOpportunityRelationship` plutot que l'ORM moderne.
