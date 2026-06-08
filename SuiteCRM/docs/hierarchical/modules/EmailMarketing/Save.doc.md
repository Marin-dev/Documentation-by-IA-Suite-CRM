# Save.php (EmailMarketing)

**Chemin :** `modules/EmailMarketing/Save.php`
**Type :** PHP — script de sauvegarde
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Script legacy de sauvegarde d'un message marketing email. Normalise le champ `time_start` (fusion meridiem AM/PM), puis delege au framework SugarCRM pour la persistence.

**Type :** controller (legacy)

---

## Dependances cles
- `$timedate` global
- `$current_user` global

---

## Notes
- Fichier procedural (pas de classe). Pattern legacy hors MVC.
- Gere la conversion AM/PM du champ horaire avant la sauvegarde.
