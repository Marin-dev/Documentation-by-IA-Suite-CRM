# EmailAddress.php

**Chemin :** `modules/EmailAddresses/EmailAddress.php`
**Type :** model
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe stub héritant de `SugarEmailAddress`. Permet au système de liens (`Link`) d'utiliser facilement la gestion des adresses email SuiteCRM. Désactive la sécurité par ligne et initialise les flags `opt_out` et `invalid_email` à 0.

## Type
model

---

## Dépendances clés
- `SugarEmailAddress` (classe parente, chemin interne : `include/SugarEmailAddress/SugarEmailAddress.php` — INCONNU précis)
- `SugarBean` (ancêtre indirect)

## Exports / Symboles principaux
- `EmailAddress` — classe — stub de SugarEmailAddress avec RLS désactivé

## Interactions
- **Appelé par :** `Link` (système de relations), modules qui chargent les adresses email via BeanFactory
- **Appelle :** `parent::saveEmail()` (SugarEmailAddress) ou `SugarBean::save()` selon le nombre d'arguments

## Notes
- La méthode `save()` a un comportement bifurqué : avec >1 argument → `saveEmail()` ; avec 1 argument → `SugarBean::save()`. Logique non-évidente.
- `disable_row_level_security = true` : toutes les adresses email sont accessibles sans filtre ACL.
