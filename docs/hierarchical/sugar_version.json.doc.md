# sugar_version.json

**Chemin :** `sugar_version.json`
**Configure :** `SugarCRM — informations de version (format JSON)`
**Dernière mise à jour doc :** 2026-05-28

---

## Ce que ce fichier configure
Déclare les métadonnées de version de la base SugarCRM Community Edition sur laquelle SuiteCRM est fondé. Utilisé par des outils ou scripts nécessitant un accès programmatique aux versions sans charger l'environnement PHP.

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `sugar_version` | `6.5.25` | Version de SugarCRM CE de base |
| `sugar_db_version` | `6.5.25` | Version du schéma de base de données SugarCRM |
| `sugar_flavor` | `CE` | Édition (Community Edition) |
| `sugar_build` | `344` | Numéro de build |
| `sugar_timestamp` | `2017-02-06 12:07PM` | Date du build SugarCRM de base |

## Impacté par / impacte
- Complément JSON de `sugar_version.php` (mêmes données, format différent)
- INCONNU : consommateurs directs dans le code PHP — à rechercher via `sugar_version.json`

## Notes techniques
- La version SugarCRM base (6.5.25, 2017) est figée : SuiteCRM a divergé de SugarCRM CE depuis lors. La version effective de l'application est dans `suitecrm_version.php` (7.15.1).
