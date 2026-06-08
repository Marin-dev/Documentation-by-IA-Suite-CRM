# ConnectorRecord.php

**Chemin :** `modules/Connectors/ConnectorRecord.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Classe de record pour le module Connectors. Étend `MergeRecord` pour permettre la fusion de données externes (Facebook, Twitter, InsideView) avec les enregistrements CRM.

## Type

model

---

## Dépendances clés

- `MergeRecord` (classe parente — chemin exact INCONNU)

## Exports / Symboles principaux

- `ConnectorRecord` — classe — record de fusion pour les connecteurs externes

## Interactions

- **Appelé par :** vues Connectors (merge/fusion de données)
- **Appelle :** `MergeRecord` (héritage)

## Notes

- `module_dir = 'Connector'` (singulier) — différent du module `Connectors` (pluriel).
