# ImportMapSalesforce.php

**Chemin :** `modules/Import/maps/ImportMapSalesforce.php`
**Type :** PHP - Modèle (mapping d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de mapping pour l'import de données exportées depuis Salesforce.com. Hérite de `ImportMapOther` et fournit les mappings spécifiques au format Salesforce pour les modules Contacts, Leads, Accounts et Opportunities.

## Type
model

## Dépendances clés
- `modules/Import/maps/ImportMapOther.php` — classe parente

## Exports / Symboles principaux
- `ImportMapSalesforce` (classe, étend `ImportMapOther`)
  - `$name` = `'salesforce'`
  - `$delimiter` = `','`, `$enclosure` = `'"'`, `$has_header` = `true`
  - `getMapping($module)` — retourne le mapping Salesforce => champs CRM

## Interactions
- **Appelé par :** `ImportMap::getImportMap()` lors de la sélection du format Salesforce
- **Appelle :** `parent::getMapping()` (ImportMapOther)

## Notes
- Permet la migration depuis Salesforce vers SuiteCRM.
