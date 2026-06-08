# createOpportunity.php

**Chemin :** `modules/AOS_Quotes/createOpportunity.php`
**Type :** PHP - Script d'action (conversion)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script de creation d'une opportunite (Opportunities) depuis un devis (AOS_Quotes). Permet de generer une opportunite CRM a partir d'un devis existant.

## Role technique
Script PHP execute directement. Verifie les droits ACL sur Opportunities. Charge le devis via `$_REQUEST['record']`, cree une opportunite avec les valeurs du devis.

---

## Dependances / Imports
- `ACLController::checkAccess('Opportunities', 'edit', true)`
- `modules/AOS_Quotes/AOS_Quotes.php`
- `modules/Opportunities/Opportunity.php`
- `$app_list_strings` (global)

## Relations cles
- **Appele par :** Bouton "Creer Opportunite" sur la DetailView d'un devis
- **Appelle :** `Opportunity->save()`

---

## Points d'attention
- Logique complete de copie des champs INCONNU (suite du fichier non lue).
- Verifie les droits sur Opportunities edit mais pas sur AOS_Quotes.
