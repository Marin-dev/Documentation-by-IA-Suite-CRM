# ImportMapOutlook.php

**Chemin :** `modules/Import/maps/ImportMapOutlook.php`
**Type :** PHP - Modèle (mapping d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de mapping pour l'import de contacts depuis Microsoft Outlook (CSV export). Hérite de `ImportMapOther` et fournit les mappings spécifiques au format Outlook pour les modules Contacts, Leads et Accounts.

## Type
model

## Dépendances clés
- `modules/Import/maps/ImportMapOther.php` — classe parente

## Exports / Symboles principaux
- `ImportMapOutlook` (classe, étend `ImportMapOther`)
  - `$name` = `'outlook'`
  - `$delimiter` = `','`, `$enclosure` = `'"'`, `$has_header` = `true`
  - `getMapping($module)` — retourne le mapping Outlook => champs CRM

## Interactions
- **Appelé par :** `ImportMap::getImportMap()` lors de la sélection du format Outlook
- **Appelle :** `parent::getMapping()` (ImportMapOther)

## Notes
- Mapping spécifique pour les noms de colonnes Outlook (ex: "Business Street", "Mobile Phone", etc.).
