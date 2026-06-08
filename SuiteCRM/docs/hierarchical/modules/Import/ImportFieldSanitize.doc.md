# ImportFieldSanitize.php

**Chemin :** `modules/Import/ImportFieldSanitize.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe de sanitisation des valeurs de champs lors de l'import CSV. Adapte les formats de dates, heures, devises, séparateurs selon la locale de l'utilisateur. Peut créer des beans liés à la volée (ex. : contacts, comptes) si `addRelatedBean` est activé.

## Type
service / helper

## Dépendances clés
- `modules/Import/sources/ImportFile.php`
- Méthodes de sanitisation des `SugarField` (convention de nommage par type de champ)

## Exports / Symboles principaux
- `ImportFieldSanitize` (classe)
  - Propriétés locale : `$dateformat`, `$timeformat`, `$timezone`, `$currency_symbol`, `$num_grp_sep`, `$dec_sep`
  - `$createdBeans` (static array) — beans créés pendant la sanitisation d'une ligne
  - `$addRelatedBean` — activation de la création de beans liés

## Interactions
- **Appelé par :** `Importer::importRow()`
- **Appelle :** méthodes de sanitisation des `SugarField`

## Notes
- `$createdBeans` doit être réinitialisé entre chaque ligne (fait dans `Importer`).
