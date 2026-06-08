# WapMenu.php

**Chemin :** `modules/Employees/WapMenu.php`
**Type :** PHP - Configuration (menu WAP legacy)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Menu WAP (Wireless Application Protocol) du module Employees. Version legacy du menu pour les accès mobiles WAP. Accessible aux admins uniquement.

## Type
config (legacy)

## Dépendances clés
- `$mod_strings`, `$current_user`
- `is_admin()`

## Exports / Symboles principaux
- `$module_menu` (tableau) — entrées de menu WAP (admin uniquement)

## Interactions
- **Appelé par :** navigateurs WAP (accès mobile legacy)
- **Appelle :** `is_admin()`

## Notes
- Technologie WAP obsolète. Ce fichier est conservé pour compatibilité historique.
