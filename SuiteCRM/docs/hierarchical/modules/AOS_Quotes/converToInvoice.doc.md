# converToInvoice.php

**Chemin :** `modules/AOS_Quotes/converToInvoice.php`
**Type :** PHP - Script d'action (conversion)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script de conversion d'un devis (AOS_Quotes) en facture (AOS_Invoices). Cree une nouvelle facture a partir des donnees du devis existant, marque le devis comme "Invoiced", et redirige vers la vue de la facture cree.

## Role technique
Script PHP execute directement (pas de classe). Verifie les droits ACL sur AOS_Invoices avant tout. Charge le devis via `$_REQUEST['record']`, formate les montants, cree la facture avec copie des champs, des lignes et des groupes de produits.

---

## Dependances / Imports
- `ACLController::checkAccess('AOS_Invoices', 'edit', true)` — verification droits
- `modules/AOS_Quotes/AOS_Quotes.php`
- `modules/AOS_Invoices/AOS_Invoices.php`
- `modules/AOS_Products_Quotes/AOS_Products_Quotes.php`
- `$timedate` (global)

## Flux d'execution
1. Verifie ACL AOS_Invoices edit
2. Charge le devis source via `$_REQUEST['record']`
3. Marque le devis comme `invoice_status = 'Invoiced'` et sauvegarde
4. Cree une nouvelle facture avec copie des champs du devis
5. Copie les lignes de produits (via logique de groupes — suite non lue)
6. Redirige vers la DetailView de la facture

## Relations cles
- **Appele par :** Bouton "Convertir en facture" sur la DetailView d'un devis
- **Appelle :** `AOS_Quotes->save()`, `AOS_Invoices->save()`

---

## Points d'attention
- Verifie les droits uniquement sur `AOS_Invoices` edit — pas sur `AOS_Quotes` edit.
- Les montants du devis sont reformates avec `format_number()` avant copie — risque de probleme si le format utilisateur differe du format DB.
- `$quote->shipping_amount` est formatte uniquement si non null — coherence avec les autres champs a verifier.
