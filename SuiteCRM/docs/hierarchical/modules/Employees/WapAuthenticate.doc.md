# WapAuthenticate.php

**Chemin :** `modules/Employees/WapAuthenticate.php`
**Type :** PHP - Script d'authentification WAP (legacy)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Authentification WAP (Wireless Application Protocol) pour les employés. Script legacy permettant l'accès depuis des appareils mobiles WAP. Charge un bean Users et tente l'authentification avec le nom d'utilisateur fourni.

## Type
helper (legacy)

## Dépendances clés
- `BeanFactory::newBean('Users')`
- `$_REQUEST['user_name']`
- `$mod_strings` (global)

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** navigateurs WAP (accès mobile legacy)
- **Appelle :** `BeanFactory::newBean('Users')`

## Notes
- Technologie WAP obsolète. Cette fonctionnalité n'est plus utilisée dans les navigateurs modernes.
