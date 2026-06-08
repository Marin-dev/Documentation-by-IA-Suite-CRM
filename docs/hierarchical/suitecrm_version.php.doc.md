# suitecrm_version.php

**Chemin :** `suitecrm_version.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Déclare la version officielle de SuiteCRM. C'est la source de vérité pour la version du produit affichée dans l'interface, les logs, et utilisée par l'installateur.

## Responsabilités
- Définir `$suitecrm_version` (`7.15.1`) — version courante de SuiteCRM
- Définir `$suitecrm_timestamp` (`2026-03-19 12:00:00`) — date de release

## Dépendances internes
- Aucune (fichier autonome de données)

## Exports / Points d'entrée
- Variables globales : `$suitecrm_version`, `$suitecrm_timestamp`
- Consommateurs identifiés :
  - `install.php` (ligne 85) — `$setup_sugar_version = $suitecrm_version`
  - INCONNU : autres références dans l'entryPoint ou l'interface admin

## Notes techniques
- Protégé par la garde `sugarEntry`.
- Ce fichier est la seule source à modifier lors d'une release pour mettre à jour la version affichée.
- Distinct de `sugar_version.php` qui documente la version SugarCRM CE héritage (6.5.25).
