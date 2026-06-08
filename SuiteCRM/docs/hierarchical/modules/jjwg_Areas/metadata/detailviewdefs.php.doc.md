# detailviewdefs.php (jjwg_Areas)

**Chemin :** `modules/jjwg_Areas/metadata/detailviewdefs.php`
**Type :** PHP — configuration de vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Definit la disposition des champs dans la vue Detail du module jjwg_Areas. Inclut un footer personnalise (`tpls/DetailViewFooter.tpl`) qui affiche probablement le bouton de visualisation carte.

**Type :** config

---

## Champs affiches (panneaux)
- name / assigned_user_name
- city / state
- country
- date_entered / date_modified
- description
- coordinates

**Footer personnalise :** `modules/jjwg_Areas/tpls/DetailViewFooter.tpl`

---

## Notes
- Le `footerTpl` est cle : c'est lui qui permet d'acceder a la vue cartographique depuis le detail.
