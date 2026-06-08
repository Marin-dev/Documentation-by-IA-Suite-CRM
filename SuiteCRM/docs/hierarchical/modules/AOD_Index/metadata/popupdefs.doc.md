# popupdefs.php

**Chemin :** `modules/AOD_Index/metadata/popupdefs.php`
**Configure :** Comportement du selecteur popup du module AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit `$popupMeta` pour le module AOD_Index — les options du selecteur popup utilise dans les champs de type "relate" pointant vers AOD_Index.

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `moduleMain` | `AOD_Index` | Module cible |
| `varName` | `AOD_Index` | Variable JS recevant la valeur |
| `orderBy` | `aod_index.name` | Tri par defaut |
| `whereClauses` | `name` | Filtre de recherche dans le popup |
| `searchInputs` | `aod_index_number, name, priority, status` | Champs du formulaire popup |

## Impacte par / impacte
- Charge par le framework SugarCRM pour afficher le popup de selection d'un AOD_Index depuis un autre module

## Points d'attention
- `priority` et `status` sont declares dans `searchInputs` mais ne font pas partie des champs declares dans `vardefs.php` — probable copier-coller depuis un autre module, ces champs seront ignores en pratique.
