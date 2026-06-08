# Exception.php

**Chemin :** `lib/Exception/Exception.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Classe de base pour toutes les exceptions internes de SuiteCRM. Elle enrichit l'exception PHP native avec un niveau de log PSR-3 et un message de détail structuré, utilisés par les controllers pour formater les réponses d'erreur.

## Responsabilités

- Préfixer automatiquement tous les messages d'exception avec `[SuiteCRM]`.
- Fournir `getDetail()` : description lisible de la cause de l'erreur (utilisée dans les réponses JSON:API).
- Fournir `getLogLevel()` : niveau PSR-3 associé (`CRITICAL` par défaut).
- Servir de classe parente à toutes les exceptions spécifiques du domaine.

## Dépendances internes

- `SuiteCRM\Enumerator\ExceptionCode` — fournit le code par défaut (`APPLICATION_UNHANDLED_BEHAVIOUR = 6000`).
- `Psr\Log\LogLevel` — constantes de niveaux de log PSR-3.

## Exports / Points d'entrée

- `Exception` (classe) — étend `\Exception` PHP native.
  - Constructeur : `__construct($message = '', $code = 6000, $previous = null)`
  - `getDetail() : string` — retourne `'SuiteCRM has encountered an exception which has not been handled'`
  - `getLogLevel() : string` — retourne `LogLevel::CRITICAL`

**Consommateurs identifiés :**
- `lib/Exception/AccessDeniedException.php`
- `lib/Exception/InvalidArgumentException.php`
- `lib/Exception/MalwareFoundException.php`
- `lib/Exception/NotAllowedException.php`
- `lib/Exception/NotFoundException.php`
- `lib/API/OAuth2/Exception/OAuth2.php`

## Notes techniques

- Toutes les sous-classes doivent surcharger `getDetail()` et `getLogLevel()` pour des messages d'erreur précis.
- Le niveau `CRITICAL` par défaut implique que toute exception non qualifiée sera traitée comme critique dans les logs.
