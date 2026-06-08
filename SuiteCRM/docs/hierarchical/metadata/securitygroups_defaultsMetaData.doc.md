# securitygroups_defaultsMetaData.php

**Chemin :** `metadata/securitygroups_defaultsMetaData.php`
**Type :** config (métadonnées de table de configuration groupes de sécurité par défaut)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `securitygroups_default` qui stocke le groupe de sécurité par défaut à appliquer pour chaque module. Permet de configurer quel groupe de sécurité est attribué automatiquement aux nouveaux enregistrements d'un module donné.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['securitygroups_default']` | variable globale PHP | Définition de la table |

### Structure de la table `securitygroups_default`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | char(36) | Clé primaire UUID (requis) |
| `securitygroup_id` | char(36) | FK vers `securitygroups.id` |
| `module` | varchar(50) | Nom du module concerné |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (requis, défaut : 0) |

## Notes

- Pas de garde `sugarEntry`. Section `relationships` vide.
- Un enregistrement par module : indique quel groupe est le groupe de sécurité par défaut pour ce module.
