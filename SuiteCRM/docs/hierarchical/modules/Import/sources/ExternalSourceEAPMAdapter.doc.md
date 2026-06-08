# ExternalSourceEAPMAdapter.php

**Chemin :** `modules/Import/sources/ExternalSourceEAPMAdapter.php`
**Type :** PHP - Adaptateur (source externe)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Adaptateur permettant d'importer des contacts depuis une source externe via le mécanisme EAPM (External Accounts / Partner Manager), typiquement Google Contacts. Implémente `ImportDataSource` pour fournir les données dans le flux d'import standard.

## Type
model (adapter)

## Dépendances clés
- `modules/Import/sources/ImportDataSource.php` — classe parente
- EAPM (External Accounts Partner Manager) — connexion Google
- `$_eapmName` = `'Google'` (codé en dur)

## Exports / Symboles principaux
- `ExternalSourceEAPMAdapter` (classe, étend `ImportDataSource`)
  - `$_eapmName` = `'Google'` — nom du service EAPM
  - `$_totalRecordCount` — nombre total d'enregistrements à importer
  - Méthodes Iterator héritées

## Interactions
- **Appelé par :** `Importer` lors d'un import depuis Google via EAPM
- **Appelle :** `ImportDataSource`, EAPM service

## Notes
- Supporte uniquement Google actuellement (`$_eapmName = 'Google'` hardcodé).
- Le compte de lignes `$_totalRecordCount` est initialisé à `-1` (non calculé) jusqu'à l'itération.
