# sugar_version.json (configuration)

**Chemin :** `sugar_version.json`
**Configure :** `Métadonnées de version SugarCRM CE (format JSON)`
**Dernière mise à jour doc :** 2026-05-30

## Rôle

Version JSON des informations de version SugarCRM CE. Doublon de `sugar_version.php` en format lisible par machine pour les outils non-PHP (scripts de déploiement, CI/CD, intégrations).

**Type :** config

## Ce que ce fichier configure

Expose les métadonnées de version de la base SugarCRM CE au format JSON pour consultation externe sans exécuter PHP.

## Paramètres clés

| Clé | Valeur | Rôle |
|---|---|---|
| `sugar_version` | `"6.5.25"` | Version SugarCRM CE |
| `sugar_db_version` | `"6.5.25"` | Version schéma DB |
| `sugar_flavor` | `"CE"` | Édition Community Edition |
| `sugar_build` | `"344"` | Numéro de build |
| `sugar_timestamp` | `"2017-02-06 12:07PM"` | Timestamp du build original |

## Impacté par / impacte

- INCONNU — consommateurs potentiels : scripts de déploiement, outils de vérification de version

## Points d'attention

- Identique en contenu à `sugar_version.php` — doivent être maintenus synchronisés.
- La version `6.5.25` est celle de la base SugarCRM CE, non de SuiteCRM (voir `suitecrm_version.php` pour `7.15.1`).
