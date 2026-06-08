# ContactOpportunityRelationshipEdit.php

**Chemin :** `modules/Contacts/ContactOpportunityRelationshipEdit.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script d'affichage du formulaire d'édition de la relation Contact-Opportunité. Permet de définir ou modifier le rôle (`contact_role`) d'un contact dans une opportunité. Intègre une recherche quicksearch pour sélectionner l'opportunité liée.

**Type :** view (script d'affichage formulaire)

---

## Dépendances clés

- `modules/Contacts/ContactOpportunityRelationship.php` — classe `ContactOpportunityRelationship`
- `XTemplate` (template `modules/Contacts/ContactOpportunityRelationshipEdit.html`)
- `include/QuickSearchDefaults.php` — configuration de la recherche rapide
- `$app_list_strings['opportunity_relationship_type_dom']` — options de rôle
- JSON / `javascript` — validation et quicksearch

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

---

## Interactions

**Appelle :**
- `new ContactOpportunityRelationship()` et `retrieve()` si `record` défini
- `QuickSearchDefaults::getQSParent()` pour la recherche d'opportunité
- `get_select_options_with_id()` pour le champ rôle

**Appelée par :** Sous-panneau "Opportunités" dans la vue détail d'un Contact (lien "Modifier").

**Position dans le flux global :** Édition du rôle d'un contact dans une opportunité ; soumission vers `SaveContactOpportunityRelationship.php`.

---

## Notes

- La validation JS vérifie la dépendance binaire `opportunity_name`/`opportunity_id` (ligne 111) — le nom doit correspondre à un ID valide via quicksearch.
- Gère le mode duplication (`isDuplicate=true`) en vidant l'ID (ligne 61-63).
