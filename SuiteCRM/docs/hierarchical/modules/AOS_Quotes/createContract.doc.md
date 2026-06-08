# createContract.php

**Chemin :** `modules/AOS_Quotes/createContract.php`
**Type :** PHP - Script d'action (conversion)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script de creation d'un contrat (AOS_Contracts) depuis un devis (AOS_Quotes). Copie les informations pertinentes du devis dans un nouveau contrat.

## Role technique
Script PHP execute directement. Verifie les droits ACL sur AOS_Contracts avant tout. Charge le devis via `$_REQUEST['record']`, cree un contrat avec les valeurs du devis, puis redirige.

---

## Dependances / Imports
- `ACLController::checkAccess('AOS_Contracts', 'edit', true)`
- `modules/AOS_Quotes/AOS_Quotes.php`
- `modules/AOS_Contracts/AOS_Contracts.php`

## Relations cles
- **Appele par :** Bouton "Creer Contrat" sur la DetailView d'un devis
- **Appelle :** `AOS_Contracts->save()`

---

## Points d'attention
- Logique complete de copie des champs INCONNU (suite du fichier non lue).
- Verifie uniquement les droits sur AOS_Contracts edit — pas sur AOS_Quotes.
