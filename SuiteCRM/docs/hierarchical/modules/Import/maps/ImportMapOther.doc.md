# ImportMapOther.php

**Chemin :** `modules/Import/maps/ImportMapOther.php`
**Type :** PHP - Modèle (classe de base)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de base pour les mappings d'import de fichiers délimités "autres" (génériques). Définit la structure commune (délimiteur, enclosure, header) et la méthode `getMapping()` avec les mappings par défaut pour les modules Contacts, Leads, Prospects, Accounts et les champs communs.

## Type
model

## Dépendances clés
Aucune dépendance externe.

## Exports / Symboles principaux
- `ImportMapOther` (classe de base pour tous les ImportMap*)
  - `$name` = `'other'`
  - `$delimiter`, `$enclosure`, `$has_header`
  - `getMapping($module)` — retourne le tableau de mapping champ source => champ CRM pour le module donné

## Interactions
- **Appelé par :** `ImportMapAct`, `ImportMapCsv`, `ImportMapOutlook`, `ImportMapSalesforce`, `ImportMapTab` (via héritage)
- **Appelle :** rien

## Notes
- Classe parente de toute la hiérarchie ImportMap.
- Les sous-classes spécialisées (Act, Outlook, Salesforce) étendent et/ou surchargent `getMapping()`.
