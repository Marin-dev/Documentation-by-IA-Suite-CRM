# vardefs.php (jjwg_Areas)

**Chemin :** `modules/jjwg_Areas/vardefs.php`
**Type :** PHP — configuration de schema
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Definit le schema de la table `jjwg_areas` : champs supplementaires, relations et options. Utilise `VardefManager` pour injecter les champs communs (basic, assignable, security_groups).

**Type :** config

---

## Parametres cles

| Parametre | Valeur/Type | Role |
|---|---|---|
| `table` | `jjwg_areas` | Nom de la table SQL |
| `audited` | `true` | Historique des modifications active |
| `city` | varchar(255) | Ville de reference de la zone |
| `state` | varchar(255) | Region/etat |
| `country` | varchar(255) | Pays |
| `coordinates` | text (rows 6, cols 80) | Coordonnees du polygone (lng,lat,elv) |
| `jjwg_maps_jjwg_areas` | link | Relation vers jjwg_Maps |
| `optimistic_locking` | `true` | Protection contre les conflits d'edition |

---

## Interactions
- **Consomme par :** `VardefManager::createVardef('jjwg_Areas', ...)` — injection des champs de base
- **Influence :** schema BDD, Studio, vues edit/detail/list/search

---

## Notes
- Le champ `coordinates` n'a pas de contrainte de format en base : le parsing est entierement applicatif (jjwg_Areas.php).
- La relation `jjwg_maps_jjwg_areas` est de type `link` (non-db) — pas de FK directe, jointure via table de relation.
