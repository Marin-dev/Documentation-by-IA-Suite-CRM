# default.php (jjwg_Areas subpanel)

**Chemin :** `modules/jjwg_Areas/metadata/subpanels/default.php`
**Type :** PHP — configuration de sous-panneau
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Definit le layout du sous-panneau par defaut de jjwg_Areas lorsqu'il est affiche dans d'autres modules (ex. dans une carte jjwg_Maps).

**Type :** config

---

## Colonnes affichees

| Champ | Type | Largeur |
|---|---|---|
| name | lien detail | 45% |
| city | varchar | 10% |
| state | varchar | 10% |
| country | varchar | 10% |
| date_modified | date | 45% |
| assigned_user_name | relate | 10% |
| edit_button | bouton | 4% |
| remove_button | bouton | 5% |

---

## Notes
- Utilise `SubPanelTopSelectButton` avec popup vers jjwg_Areas.
