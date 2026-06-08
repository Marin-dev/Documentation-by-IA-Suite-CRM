# default.php (jjwg_Markers/metadata/subpanels)

**Chemin :** `modules/jjwg_Markers/metadata/subpanels/default.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Definit la mise en page du sous-panneau par defaut du module jjwg_Markers lorsqu'il est affiche dans d'autres modules (par exemple dans jjwg_Maps). Specifie les colonnes, boutons et l'ordre d'affichage.

**Type :** config (metadata sous-panneau)

---

## Dependances cles
- Aucune (fichier de configuration pur)

## Exports / Symboles principaux

Variable `$subpanel_layout` :

| Element | Valeur | Role |
|---|---|---|
| `top_buttons` | `SubPanelTopCreateButton`, `SubPanelTopSelectButton` | Boutons en haut du sous-panneau |
| Colonnes affichees | `name`, `city`, `state`, `country`, `marker_image`, `date_modified`, `assigned_user_name` | Champs visibles par defaut |
| `edit_button` | `SubPanelEditButton` | Bouton edition en ligne |
| `remove_button` | `SubPanelRemoveButton` | Bouton suppression relation |

## Interactions
- **Appele par :** systeme de sous-panneaux SuiteCRM quand jjwg_Markers est affiche en sous-panneau
- **Reference par :** `metadata/subpaneldefs.php` des modules parents (ex: jjwg_Maps)

## Notes
- `popup_module = 'jjwg_Markers'` sur le bouton Select : ouvre la popup de selection de marqueurs.
- Colonnes `name` et `date_modified` ont `width => '45%'` — occupation importante.
