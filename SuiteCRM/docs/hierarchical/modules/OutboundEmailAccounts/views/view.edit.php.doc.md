# view.edit.php

**Chemin :** `modules/OutboundEmailAccounts/views/view.edit.php`
**Type :** vue

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Vue d'édition d'un compte email sortant. Permet de configurer les paramètres SMTP, le type d'authentification et l'adresse d'expédition.

## Type

vue

---

## Dépendances clés

- `SugarView`, `OutboundEmailAccounts`

## Exports / Symboles principaux

- Classe vue édition OutboundEmailAccounts

## Interactions

- **Appelé par :** dispatcher MVC (action EditView)

## Notes

- Gère les 3 types d'auth (no_auth, basic, oauth) via JavaScript probablement.
