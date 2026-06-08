# Fichier : SaveContactOpportunityRelationship.php

**Chemin :** `modules/Contacts/SaveContactOpportunityRelationship.php`
**Type :** PHP - Script d'action (sauvegarde relation)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Traite la sauvegarde du role d'un contact dans une opportunite. Cree ou met a jour l'enregistrement dans la table de jonction `opportunities_contacts`.

## Role technique

Script procedural. Instancie `ContactOpportunityRelationship`, peuple les champs depuis le POST, et appelle `save()`. Requiert `modules/Contacts/ContactOpportunityRelationship.php`.

---

## Dependances cles

- `modules/Contacts/ContactOpportunityRelationship.php`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Formulaire POST depuis `ContactOpportunityRelationshipEdit.php`

## Relations cles

- **Tables DB modifiees :** `opportunities_contacts`
- **Position dans le flux :** Sauvegarde du role Contact dans une Opportunite

---

## Points d'attention

- Utilise la classe legacy `ContactOpportunityRelationship`.
