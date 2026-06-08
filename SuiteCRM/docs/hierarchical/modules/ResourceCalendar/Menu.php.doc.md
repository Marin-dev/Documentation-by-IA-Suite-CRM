# Menu.php (ResourceCalendar)

**Chemin :** `modules/ResourceCalendar/Menu.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Definit le menu de navigation du module ResourceCalendar (Calendrier des ressources). Le menu est vide — ce module ne propose pas d'actions directes dans la navigation.

**Type :** config (menu module)

---

## Dependances cles
- Aucune

## Exports / Symboles principaux
- `$module_menu` — tableau vide

## Interactions
- **Appele par :** framework SuiteCRM pour construire la navigation
- **Appelle :** rien

## Notes
- Menu vide : ResourceCalendar est un module de redirection vers le module Project.
- L'action principale est definie dans index.php (redirection vers `Project&action=ResourceList`).
