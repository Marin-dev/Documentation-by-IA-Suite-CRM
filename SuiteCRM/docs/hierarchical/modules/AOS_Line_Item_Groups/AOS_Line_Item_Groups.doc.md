# AOS_Line_Item_Groups.php

**Chemin :** `modules/AOS_Line_Item_Groups/AOS_Line_Item_Groups.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele representant un groupe de lignes de produits/services dans un devis, une facture ou un contrat AOS. Permet de regrouper des lignes avec un sous-total par groupe (ex: "Materiel", "Services").

## Role technique
Etend `AOS_Line_Item_Groups_sugar`. La methode `save_groups` orchestre la sauvegarde de tous les groupes depuis le POST, en creant les beans de lignes de produits associes via `AOS_Products_Quotes->save_lines()`. Gere la conversion de devise du document parent.

---

## Dependances / Imports
- `AOS_Line_Item_Groups_sugar` (classe parente generee)

## Methodes principales
| Methode | Role |
|---|---|
| `save_groups($post_data, $parent, $key)` | Sauvegarde tous les groupes de lignes depuis le POST |
| (methodes heritees de sugar) | CRUD standard |

**Consommateurs :**
- `AOS_Quotes->save()`
- `AOS_Invoices->save()`
- `AOS_Contracts->save()`

## Relations cles
- **Table DB :** `aos_line_item_groups`
- **Relation parent :** FK vers `aos_quotes`, `aos_invoices`, ou `aos_contracts`
- **Relation enfant :** vers `aos_products_quotes` (lignes de produits)
- **Appelle :** `AOS_Products_Quotes->save_lines()`, `BeanFactory::newBean('AOS_Line_Item_Groups')`

---

## Points d'attention
- Chaque groupe est renumerote sequentiellement (`$j` incrementel).
- Le `assigned_user_id` du groupe est herite du document parent.
- La gestion de la devise parent (`$parentCurrencyId`) est initialisee mais la logique complete est dans la suite du fichier (limite de lecture) — INCONNU pour les details.
- Le logging de warning est present si le champ `deleted` n'est pas dans le POST.
