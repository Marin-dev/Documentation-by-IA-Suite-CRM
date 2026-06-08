# InvalidArgumentException.php

**Chemin :** `lib/Exception/InvalidArgumentException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception lancee lorsqu'un argument invalide est passe a une methode ou fonction de SuiteCRM.

## Role technique
Etend `SuiteCRM\Exception\Exception`. Prefixe le message avec `[InvalidArgumentException]`. Code par defaut : `APPLICATION_UNHANDLED_BEHAVIOUR` (6000).

---

## Dependances cles
- `SuiteCRM\Enumerator\ExceptionCode`
- `SuiteCRM\Exception\Exception`

## Exports / Symboles principaux
- `InvalidArgumentException` — classe exception — argument invalide

## Relations cles
- **Appele par :** plusieurs classes de `lib/Search/`, `lib/PDF/`, `lib/Utility/`
- **Appelle :** `Exception::__construct()`

---

## Points d'attention
- RAS.
