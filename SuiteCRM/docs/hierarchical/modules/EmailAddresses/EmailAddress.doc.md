# EmailAddress.php

**Chemin :** `modules/EmailAddresses/EmailAddress.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe stub permettant à la classe `Link` de manipuler facilement `SugarEmailAddress`. Fournit un point d'entree unique pour sauvegarder ou associer des adresses email a un bean CRM. Desactive la securite par ligne (`disable_row_level_security = true`).

**Type :** model

---

## Dependances cles
- `SugarEmailAddress` (classe parente, core SugarCRM)
- `SugarBean::save()` (appele si un seul argument)
- `SugarEmailAddress::saveEmail()` (appele avec plusieurs arguments)

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `EmailAddress` | classe | Stub heritant de `SugarEmailAddress` |
| `save()` | methode | Dispatch vers `saveEmail()` (multi-args) ou `SugarBean::save()` (un arg) |

---

## Interactions
- **Appele par :** classe `Link` (core), tout code utilisant `BeanFactory::getBean('EmailAddresses')`
- **Appelle :** `SugarEmailAddress::saveEmail()`, `SugarBean::save()`

---

## Notes
- `opt_out` et `invalid_email` sont initialises a `0` dans le constructeur.
- La disproportion entre `save()` multi-args et mono-arg est un pattern legacy ; risque de confusion si appele sans connaitre la signature exacte.
