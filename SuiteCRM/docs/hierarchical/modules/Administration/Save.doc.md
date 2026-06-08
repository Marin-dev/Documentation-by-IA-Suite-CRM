# Save.php

**Chemin :** `modules/Administration/Save.php`
**Type :** PHP (action / controleur procedral)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Traite la soumission des formulaires d'administration generiques. Itere sur les donnees POST, filtre celles appartenant aux categories de configuration autorisees, et les persiste dans la table `config`. Redirige ensuite vers l'action specifiee dans `$_POST['return_action']`.

## Role technique
Script procedral sans classe. Utilise `BeanFactory::newBean('Administration')` pour obtenir l'instance Administration, puis appelle `saveSetting()` par parametre filtre. Traite specialement les champs `license_expire_date` (conversion de format via `$timedate`) et `license_key` (trim).

---

## Dependances cles
| Element | Role |
|---|---|
| `BeanFactory::newBean('Administration')` | Instance du modele Administration |
| `Administration::get_config_prefix()` | Decoupe category_key |
| `Administration::saveSetting()` | Persistance individuelle |
| `$timedate` (global) | Conversion format date pour license |
| `$_POST['return_action']` / `$_POST['return_module']` | Parametres de redirection |

## Symboles principaux
- Aucune classe ni fonction — script d'action procedral

## Interactions
- **Appele par :** Formulaires HTML du module Administration (action POST)
- **Appelle :** `Administration::saveSetting()`, `$timedate->swap_formats()`
- **Redirige vers :** `index.php?action={return_action}&module={return_module}`

---

## Notes
- Acces restreint : `is_admin($current_user)` verifie en debut de script (ligne 49).
- Seules les categories presentes dans `$focus->config_categories` sont traitees — filtrage de securite.
- Le cas `license` est traite specialement mais cette categorie n'est plus dans `$config_categories` par defaut ; il s'agit probablement d'un vestige SugarCRM.
