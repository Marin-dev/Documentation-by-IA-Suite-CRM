# sugar_version.php

**Chemin :** `sugar_version.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Déclare les variables de version de la base SugarCRM Community Edition. Chargé très tôt dans le cycle de vie de l'application (notamment par l'installateur) pour rendre les informations de version disponibles globalement.

## Responsabilités
- Définir `$sugar_version` (`6.5.25`) — version SugarCRM CE de base
- Définir `$sugar_db_version` (`6.5.25`) — version du schéma DB
- Définir `$sugar_flavor` (`CE`) — édition Community
- Définir `$sugar_build` (`344`) — numéro de build
- Définir `$sugar_timestamp` (`2017-02-06 12:07PM`) — date du build

## Dépendances internes
- Aucune (fichier autonome de données)

## Exports / Points d'entrée
- Variables globales : `$sugar_version`, `$sugar_db_version`, `$sugar_flavor`, `$sugar_build`, `$sugar_timestamp`
- Consommateurs identifiés : `install.php` (ligne 84), `include/entryPoint.php` (INCONNU — à vérifier)

## Notes techniques
- Protégé par la garde `sugarEntry` : ne peut être inclus que dans un contexte applicatif valide.
- La version SugarCRM de base (6.5.25) est historique et ne reflète pas la version SuiteCRM réelle (voir `suitecrm_version.php`).
- Ces variables coexistent avec les données JSON équivalentes dans `sugar_version.json`.
