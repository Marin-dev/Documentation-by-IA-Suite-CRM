# jjwg_Maps_sugar.php

**Chemin :** `modules/jjwg_Maps/jjwg_Maps_sugar.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de base auto-generee pour le bean jjwg_Maps. Definit la structure ORM : table, champs, ACL.

**Type :** model (base auto-generee)

---

## Dependances cles
- `Basic` (SuiteCRM core)

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `jjwg_Maps_sugar` | Classe | Base ORM |
| `$table_name` | Propriete | `'jjwg_maps'` |
| `$distance` | Propriete | Distance pour la recherche par rayon |
| `$unit_type` | Propriete | Unite de distance (mi/km) |
| `$module_type` | Propriete | Module CRM affiche sur la carte |
| `$parent_name/type/id` | Proprietes | Champ flex-relate (point central de la carte) |
| `bean_implements('ACL')` | Methode | Retourne `true` |

---

## Notes
- Fichier genere automatiquement. Ne pas modifier manuellement.
