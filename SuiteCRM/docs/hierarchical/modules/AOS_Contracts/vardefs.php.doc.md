# Fichier vardefs.php — AOS_Contracts
**Chemin :** `modules/AOS_Contracts/vardefs.php`
**Type :** PHP — configuration
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Définit le schéma de la table `aos_contracts` : champs (start_date, end_date, renewal_reminder_date, call_id, status, contract_type, total_contract_value, line_items_group via relations, currency fields).

## Type
config

## Notes
Template VardefManager `basic`, `assignable`, `currency`. Relations vers AOS_Line_Item_Groups, AOS_Products_Quotes, Accounts, Contacts.
