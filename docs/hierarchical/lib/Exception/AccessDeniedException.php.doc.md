# AccessDeniedException.php

**Chemin :** `lib/Exception/AccessDeniedException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Exception levée lorsqu'un accès est refusé à une ressource ou une opération dans SuiteCRM. Indique une violation de permissions au niveau applicatif.

## Responsabilités

- Préfixer les messages d'exception avec `[AccessDeniedException]`.
- Hériter du comportement de logging et de détail de la classe `Exception` parente.

## Dépendances internes

- `SuiteCRM\Exception\Exception` — classe parente.
- `SuiteCRM\Enumerator\ExceptionCode` — code par défaut `APPLICATION_UNHANDLED_BEHAVIOUR = 6000`.

## Exports / Points d'entrée

- `AccessDeniedException` (classe) — étend `SuiteCRM\Exception\Exception`.
  - Constructeur : `__construct($message = '', $code = 6000, $previous = null)`

**Consommateurs identifiés :** INCONNU (aucun usage trouvé par grep dans le scope documenté).

## Notes techniques

- Cette classe ne surcharge pas `getDetail()` ni `getLogLevel()` — elle hérite donc du niveau `CRITICAL` et du message générique de la classe parente.
- Le code par défaut `APPLICATION_UNHANDLED_BEHAVIOUR` semble générique ; dans un refactoring futur il pourrait être judicieux d'utiliser un code dédié `ACCESS_DENIED`.
