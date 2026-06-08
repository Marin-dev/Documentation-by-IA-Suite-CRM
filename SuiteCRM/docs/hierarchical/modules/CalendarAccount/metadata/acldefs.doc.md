# Fichier : acldefs.php

**Chemin :** `modules/CalendarAccount/metadata/acldefs.php`
**Type :** PHP — configuration (ACL definitions)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit les regles ACL specifiques au formulaire CalendarAccount. Desactive le bouton "btn1" (EditView) si l'utilisateur n'a pas l'action `list`.

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `btn1.display_option` | `disabled` | Bouton desactive si condition non remplie |
| `btn1.action_option` | `list` | Condition : acces `list` requis |
| `btn1.app_action` | `EditView` | Action ciblee |

## Impacte par / impacte
- Consomme par le framework ACL SugarCRM pour les vues CalendarAccount

## Points d'attention
- Fichier specifique CalendarAccount — complement de `CalendarAccountACLService.php`.
