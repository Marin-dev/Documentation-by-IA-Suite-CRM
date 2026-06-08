# ImportMapGoogle.php

**Chemin :** `modules/Import/maps/ImportMapGoogle.php`
**Type :** PHP - Modèle (mapping d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de mapping pour l'import de contacts depuis Google Contacts. Hérite de `ImportMapOther` et fournit un mapping complet des champs Google (Given Name, Family Name, Birthday, adresses Home/Work, téléphones, email, etc.) vers les champs CRM.

## Type
model

## Dépendances clés
- `modules/Import/maps/ImportMapOther.php` — classe parente

## Exports / Symboles principaux
- `ImportMapGoogle` (classe, étend `ImportMapOther`)
  - `$name` = `'google'`
  - `getMapping($module)` — retourne le mapping Google Contacts => champs CRM (contacts, leads)

## Interactions
- **Appelé par :** `ImportMap::getImportMap()` / `ExternalSourceEAPMAdapter`
- **Appelle :** `ImportMapOther` (héritage)

## Notes
- Structure de mapping différente des autres : tableaux associatifs `['sugar_key', 'sugar_label', 'default_label']` au lieu de simples paires.
