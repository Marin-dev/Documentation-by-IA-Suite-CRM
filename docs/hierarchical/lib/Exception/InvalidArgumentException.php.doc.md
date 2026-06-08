# InvalidArgumentException.php

**Chemin :** `lib/Exception/InvalidArgumentException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Exception levée lorsqu'un argument invalide est passé à une méthode ou une fonction dans SuiteCRM. Complète la hiérarchie d'exceptions en couvrant les erreurs de validation d'arguments.

## Responsabilités

- Préfixer les messages d'exception avec `[InvalidArgumentException]`.
- Hériter du comportement de logging et de détail de la classe `Exception` parente.

## Dépendances internes

- `SuiteCRM\Exception\Exception` — classe parente.
- `SuiteCRM\Enumerator\ExceptionCode` — code par défaut `APPLICATION_UNHANDLED_BEHAVIOUR = 6000`.

## Exports / Points d'entrée

- `InvalidArgumentException` (classe) — étend `SuiteCRM\Exception\Exception`.
  - Constructeur : `__construct($message = '', $code = 6000, $previous = null)`

**Consommateurs identifiés :**
- `lib/API/v8/Controller/ModuleController.php` (ligne 449)
- `lib/API/v8/Controller/OAuth2Controller.php`

## Notes techniques

- Ne surcharge pas `getDetail()` ni `getLogLevel()` — hérite du niveau `CRITICAL`.
- Attention : PHP natif possède déjà une `\InvalidArgumentException` (SPL). La classe SuiteCRM a son propre espace de noms (`SuiteCRM\Exception`) ce qui peut créer des confusions. Vérifier les imports dans les fichiers consommateurs.
