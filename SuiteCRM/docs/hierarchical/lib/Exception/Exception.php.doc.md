# Exception.php

**Chemin :** `lib/Exception/Exception.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception de base de SuiteCRM. Toutes les exceptions metier et techniques de l'application en heritent. Fournit un niveau de log PSR-3 et un detail textuel sur la cause.

## Role technique
Etend `\Exception` PHP natif. Prefixe automatiquement le message avec `[SuiteCRM]`. Ajoute deux methodes : `getDetail()` retournant un texte fixe, et `getLogLevel()` retournant `LogLevel::CRITICAL` par defaut.

---

## Dependances cles
- `Psr\Log\LogLevel` — constantes de niveau de log PSR-3
- `SuiteCRM\Enumerator\ExceptionCode` — code par defaut = `APPLICATION_UNHANDLED_BEHAVIOUR` (6000)

## Exports / Symboles principaux
- `Exception` — classe (etend `\Exception`) — exception de base SuiteCRM
  - `getDetail(): string` — detail non-technique de la cause
  - `getLogLevel(): string` — niveau PSR-3 (CRITICAL par defaut)

- **Consommateurs identifies :**
  - `lib/Exception/AccessDeniedException.php`
  - `lib/Exception/InvalidArgumentException.php`
  - `lib/Exception/MalwareFoundException.php`
  - `lib/Exception/NotAllowedException.php`
  - `lib/Exception/NotFoundException.php`

## Relations cles
- **Appele par :** toutes les exceptions filles de `lib/Exception/`
- **Appelle :** `ExceptionCode::APPLICATION_UNHANDLED_BEHAVIOUR`
- **Position dans le flux global :** racine de la hierarchie d'exceptions SuiteCRM

---

## Points d'attention
- `getDetail()` renvoie toujours la meme chaine (ligne 70) ; les sous-classes peuvent surcharger cette methode.
- `getLogLevel()` retourne CRITICAL ; `MalwareFoundException` surcharge en EMERGENCY.
