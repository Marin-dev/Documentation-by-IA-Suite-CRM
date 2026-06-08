# ImportMapAct.php

**Chemin :** `modules/Import/maps/ImportMapAct.php`
**Type :** PHP - Modèle (mapping d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de mapping pour l'import de fichiers ACT! (logiciel CRM). Hérite de `ImportMapOther` et fournit les mappings de champs spécifiques au format ACT! pour les modules Contacts et Leads (adresses, téléphones, email, etc.).

## Type
model

## Dépendances clés
- `modules/Import/maps/ImportMapOther.php` — classe parente

## Exports / Symboles principaux
- `ImportMapAct` (classe, étend `ImportMapOther`)
  - `$name` = `'act'`
  - `$delimiter` = `','`, `$enclosure` = `'"'`, `$has_header` = `true`
  - `getMapping($module)` — retourne le tableau de mapping ACT! => champs CRM pour Contacts/Leads

## Interactions
- **Appelé par :** `ImportMap::getImportMap()` lors de la sélection du format ACT!
- **Appelle :** `parent::getMapping()` (ImportMapOther)

## Notes
- Mapping défini pour `Contacts` et `Leads` uniquement (switch statement).
