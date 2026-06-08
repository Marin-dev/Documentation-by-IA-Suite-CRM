# AOS_Contracts.php

**Chemin :** `modules/AOS_Contracts/AOS_Contracts.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele principal des contrats commerciaux (Contracts) dans le module AOS. Gere la creation de contrats avec date de rappel de renouvellement automatique, les lignes de produits associees, et la creation de reminders.

## Role technique
Etend `AOS_Contracts_sugar`. Le constructeur calcule automatiquement la date de rappel de renouvellement (`renewal_reminder_date`) si la configuration `renewalReminderPeriod` est definie. La methode `save` peut creer un reminder via `createReminder()` si une date de rappel est fournie.

---

## Dependances / Imports
- `AOS_Contracts_sugar` (classe parente generee)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()`
- `$sugar_config['aos']['contracts']['renewalReminderPeriod']` — nombre de jours avant echeance pour le rappel

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `AOS_Contracts` | Classe | Modele de contrat |
| `save($check_notify)` | Methode | Sauvegarde contrat + conversion USD + groupes de lignes + reminder |
| `createReminder()` | Methode | Cree un reminder pour la date de renouvellement (dans classe parente — INCONNU) |

## Relations cles
- **Table DB :** `aos_contracts`
- **Appelle :** `AOS_Line_Item_Groups->save_groups()`, `perform_aos_save()`
- **Config :** `$sugar_config['aos']['contracts']['renewalReminderPeriod']`

---

## Points d'attention
- La date de rappel est calculee uniquement si `$this->id == null` (nouveau contrat) ET si `end_date` est renseignee.
- `createReminder()` est definie dans `AOS_Contracts_sugar` (non lu dans ce contexte) — INCONNU quant a son implementation exacte.
- Les lignes de produits sont nettoyees du POST lors de duplication (`duplicateSave`).
