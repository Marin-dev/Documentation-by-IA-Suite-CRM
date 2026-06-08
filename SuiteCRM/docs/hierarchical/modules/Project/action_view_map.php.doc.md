# Fichier : action_view_map.php (configuration)

**Chemin :** `modules/Project/action_view_map.php`
**Configure :** Mapping actions -> vues du module Project
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Declare deux mappings d'actions vers des vues specifiques au module Project pour la gestion des templates.

---

## Parametres cles

| Parametre | Valeur | Effet |
| --- | --- | --- |
| `$action_view_map['projecttemplateseditview']` | `'templatesedit'` | Route vers `views/view.templatesedit.php` |
| `$action_view_map['projecttemplatesdetailview']` | `'templatesdetail'` | Route vers `views/view.templatesdetail.php` |

---

## Impacte par / impacte

- Lu par le routeur SuiteCRM pour dispatcher les actions vers les vues template
- Utilise dans `modules/Project/Save.php` (redirection vers `ProjectTemplatesDetailView`, ligne 134)

---

## Points d'attention

- Ces mappings permettent d'avoir des vues edit/detail differentes selon que le projet est un template ou non.
