# Fichier AOS_Contracts.php

**Chemin :** `modules/AOS_Contracts/AOS_Contracts.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle du module Contrats (AOS_Contracts). Gère la création et la sauvegarde de contrats commerciaux avec lignes de produits/services, groupes de lignes, et reminders de renouvellement automatiques sous forme d'appels planifiés.

## Type
model

---

## Dépendances clés
- `AOS_Contracts_sugar` (classe parente générée)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()` (conversion devises)
- `modules/AOS_Line_Item_Groups/AOS_Line_Item_Groups.php` — sauvegarde des groupes de lignes
- `modules/AOS_Products_Quotes/AOS_Products_Quotes.php` — suppression des lignes produits
- `modules/Calls/Call.php` — création du reminder de renouvellement
- `$sugar_config['aos']['contracts']['renewalReminderPeriod']` — configuration du délai reminder

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOS_Contracts` | classe | Bean contrat |
| `save()` | méthode | Sauvegarde contrat + groupes lignes + reminder renouvellement |
| `mark_deleted()` | méthode | Supprime contrat + lignes produits + appel reminder |
| `createReminder()` | méthode | Crée/met à jour un enregistrement Call pour le reminder de renouvellement |
| `createLink()` | méthode | Lie l'appel reminder au compte client |
| `deleteCall()` | méthode | Supprime l'appel reminder associé |

## Interactions
- **Appelé par :** Vue EditView AOS_Contracts
- **Appelle :** `perform_aos_save()`, `AOS_Line_Item_Groups::save_groups()`, `AOS_Products_Quotes::mark_lines_deleted()`, `Call`
- **Table BD :** `aos_contracts`, `aos_line_item_groups`, `aos_products_quotes`

## Notes
- La date de reminder est calculée dans le constructeur : `end_date - renewalReminderPeriod jours` (si nouveau contrat et date de fin renseignée).
- `createReminder()` crée un appel de type Outbound/Planned avec reminder_time=60min et duration=30min.
- Le champ `call_id` stocke l'ID de l'appel reminder pour permettre la mise à jour.
- Si `renewal_reminder_date = 0`, aucun appel n'est créé/modifié.
