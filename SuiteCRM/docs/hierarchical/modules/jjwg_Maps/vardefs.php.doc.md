# vardefs.php (jjwg_Maps)

**Chemin :** `modules/jjwg_Maps/vardefs.php`
**Type :** PHP — configuration de schema
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Definit le schema de la table `jjwg_maps` : champs specifiques, relations vers les modules CRM et les modules de cartographie.

**Type :** config

---

## Champs principaux

| Champ | Type | Role |
|---|---|---|
| distance | float(9,4) | Distance de recherche (rayon) |
| unit_type | enum (map_unit_type_list) | mi ou km |
| module_type | enum (map_module_type_list) | Module CRM a afficher |
| parent_name | parent (flex_relate) | Point central (enregistrement CRM source) |
| parent_type | parent_type | Type du flex_relate |
| parent_id | id | ID du flex_relate |

## Relations definies

| Relation | Type | Module lie |
|---|---|---|
| jjwg_Maps_accounts | one-to-many | Accounts |
| jjwg_Maps_contacts | one-to-many | Contacts |
| jjwg_Maps_leads | one-to-many | Leads |
| jjwg_Maps_opportunities | one-to-many | Opportunities |
| jjwg_Maps_cases | one-to-many | Cases |
| jjwg_Maps_projects | one-to-many | Project |
| jjwg_Maps_meetings | one-to-many | Meetings |
| jjwg_Maps_prospects | one-to-many | Prospects |
| jjwg_Maps_jjwp_partners | one-to-many | jjwp_Partners |
| jjwg_maps_jjwg_areas | link | jjwg_Areas |
| jjwg_maps_jjwg_markers | link | jjwg_Markers |

---

## Notes
- Toutes les relations one-to-many utilisent `parent_id/parent_type` (flex_relate) comme cle de jointure.
- `optimistic_locking` active.
