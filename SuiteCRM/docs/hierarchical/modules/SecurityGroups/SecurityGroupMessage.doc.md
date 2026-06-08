# SecurityGroupMessage.php

**Chemin :** `modules/SecurityGroups/SecurityGroupMessage.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bean representant un message de groupe (fil de discussion interne a un groupe de securite). Gere l'affichage avec auteur, groupe d'appartenance et horodatage relatif.

## Type
model

## Dependances cles
- `Basic` (heritage)
- `DBManagerFactory`, `BeanFactory`
- Table DB : `securitygroups_message`

## Exports / Symboles principaux
- `class SecurityGroupMessage extends Basic`
- `saveMessage($text, $securitygroup_id)` — cree un message (static)
- `get_list_view_data()` — surcharge avec rendu HTML enrichi (auteur, groupe, temps ecoule)
- `getTimeLapse($startDate)` — calcule le temps ecoule en texte lisible
- `bean_implements('ACL')` — retourne false

## Interactions
- **Appelle :** `BeanFactory::newBean('SecurityGroups')`, `BeanFactory::newBean('Users')`, `SugarThemeRegistry`
- **Appele par :** INCONNU (probablement vues de detail SecurityGroups)

## Notes
- `importable = false`
- `getTimeLapse` utilise le temps serveur (`time()`) et non le timezone utilisateur.
