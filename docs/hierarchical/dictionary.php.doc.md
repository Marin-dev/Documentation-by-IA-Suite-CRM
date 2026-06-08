# dictionary.php

**Chemin :** `dictionary.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée secondaire pour le chargement du dictionnaire de tables SuiteCRM. Il initialise l'environnement applicatif puis inclut le fichier de définition globale des tables.

## Responsabilités
- Vérifier le jeton d'entrée `sugarEntry` (protection contre l'accès direct)
- Charger l'environnement complet via `include/entryPoint.php`
- Inclure `modules/TableDictionary.php` qui définit le dictionnaire de métadonnées des tables

## Dépendances internes
- `include/entryPoint.php` — bootstrap global de SuiteCRM
- `modules/TableDictionary.php` — définitions des tables relationnelles (dictionnaire de schéma)

## Exports / Points d'entrée
- Aucun export PHP direct ; ce fichier est un script d'initialisation inclus par d'autres composants.

## Notes techniques
- La constante `sugarEntry` est le mécanisme de protection standard de SuiteCRM contre l'appel direct des fichiers PHP.
- INCONNU : quels composants incluent explicitement ce fichier ? Une recherche `include.*dictionary.php` dans le repo permettrait de le confirmer.
