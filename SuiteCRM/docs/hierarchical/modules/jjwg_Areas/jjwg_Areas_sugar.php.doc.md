# jjwg_Areas_sugar.php

**Chemin :** `modules/jjwg_Areas/jjwg_Areas_sugar.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de base auto-generee pour le bean jjwg_Areas. Definit la structure ORM du module : table, champs, interface ACL. Ne contient aucune logique metier ; sert uniquement de socle pour `jjwg_Areas`.

**Type :** model (base auto-generee)

---

## Dependances cles
- `Basic` (SuiteCRM core) — classe parente du bean

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `jjwg_Areas_sugar` | Classe | Base ORM du module |
| `$table_name` | Propriete | `'jjwg_areas'` |
| `$module_dir` | Propriete | `'jjwg_Areas'` |
| `$disable_row_level_security` | Propriete | `true` — RLS desactive |
| `$importable` | Propriete | `true` |
| `$coordinates` | Propriete | Champ texte stockant les coordonnees du polygone |
| `bean_implements('ACL')` | Methode | Retourne `true` — module soumis aux ACL |

---

## Interactions
- **Herite par :** `jjwg_Areas` (jjwg_Areas.php)
- **Appele par :** framework SuiteCRM lors du chargement du bean

---

## Notes
- Fichier genere automatiquement (pattern `_sugar`). Ne pas modifier manuellement.
- Les champs declares (city, state, country, coordinates) correspondent aux colonnes supplementaires definies dans `vardefs.php`.
