# Fichier : ContactOpportunityRelationship.php

**Chemin :** `modules/Contacts/ContactOpportunityRelationship.php`
**Type :** PHP - Modele (relation intermediaire)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Modele representant la relation many-to-many entre un Contact et une Opportunite. Stocke le role du contact dans l'opportunite (`contact_role`). Mappe la table de jonction `opportunities_contacts`.

## Role technique

Etend `SugarBean`. Mappe la table `opportunities_contacts` avec les champs `contact_id`, `opportunity_id`, `contact_role`, `date_modified`, `deleted`. Classe sans logique metier particuliere — essentiellement un modele de relation.

---

## Dependances cles

- **Extends :** `SugarBean`
- `DBManagerFactory::getInstance()` — initialise `$db` et `$dbManager` dans le constructeur

## Exports / Symboles principaux

- `ContactOpportunityRelationship` — classe — relation Contact <-> Opportunite
  - Champs : `id`, `contact_id`, `opportunity_id`, `contact_role`, `date_modified`
  - Table : `opportunities_contacts`

## Consommateurs identifies

- `modules/Contacts/ContactOpportunityRelationshipEdit.php`
- `modules/Contacts/SaveContactOpportunityRelationship.php`

## Relations cles

- **Table cible :** `opportunities_contacts`
- **Modules lies :** Contacts, Opportunities

---

## Points d'attention

- Cette classe est un vestige de l'architecture pre-ORM moderne — les relations sont normalement gerees via les vardefs et `Link2`. Note dans le code source : "This table definition moved to Opportunity module."
