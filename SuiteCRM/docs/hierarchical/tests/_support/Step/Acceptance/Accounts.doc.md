# Accounts.php (helper / step acceptance)

**Chemin :** `tests/_support/Step/Acceptance/Accounts.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Step Object fournissant des actions métier spécifiques au module Accounts pour les tests acceptance : création directe d'un compte en base de données.

## Type
helper / step acceptance

## Dependances cles
- `AcceptanceTester` — classe parente
- Global `$db` — accès base de données

## Scenarios couverts
- `createAccount($name)` : insère un compte directement en base via `pQuery` et retourne son ID

## Notes
- Utilise le global `$db` (injection non explicite) — dépendance fragile.
- La requête utilise des paramètres positionnels `'?'` — vérifier la compatibilité avec le driver DB utilisé.
- Namespace : `Step\Acceptance`.
