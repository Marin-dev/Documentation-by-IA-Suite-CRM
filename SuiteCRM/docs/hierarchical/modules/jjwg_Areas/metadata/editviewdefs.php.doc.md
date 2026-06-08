# editviewdefs.php (jjwg_Areas)

**Chemin :** `modules/jjwg_Areas/metadata/editviewdefs.php`
**Type :** PHP — configuration de vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Definit la disposition des champs dans la vue Edition du module jjwg_Areas. Inclut un footer personnalise (`tpls/EditViewFooter.tpl`) qui integre probablement l'iframe de dessin de polygone.

**Type :** config

---

## Champs affiches (panneaux)
- name / assigned_user_name
- city / state
- country
- description
- coordinates

**Footer personnalise :** `modules/jjwg_Areas/tpls/EditViewFooter.tpl`

---

## Notes
- Le champ `coordinates` est visible en edition (saisi manuellement ou via l'iframe de carte).
