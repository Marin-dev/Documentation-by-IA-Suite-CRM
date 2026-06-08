# default.php (subpanel)

**Chemin :** `modules/AOD_Index/metadata/subpanels/default.php`
**Configure :** Mise en page du sous-panneau AOD_Index dans les modules tiers
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit `$subpanel_layout` pour le module AOD_Index — la structure du sous-panneau AOD_Index lorsqu'il apparait dans la vue detail d'un autre module (via une relation).

## Parametres cles
| Element | Valeur | Effet |
|---|---|---|
| Boutons | `SubPanelTopCreateButton`, `SubPanelTopSelectButton` | Creation et selection d'AOD_Index |
| Colonne `name` | 45%, lien detail | Nom de l'enregistrement |
| Colonne `date_modified` | 45% | Date de modification |
| Bouton `edit_button` | 4% | Edition inline |
| Bouton `remove_button` | 5% | Suppression de la relation |

## Impacte par / impacte
- Charge par le framework SugarCRM lorsqu'un module affiche un sous-panneau AOD_Index

## Points d'attention
- RAS — layout de sous-panneau standard.
