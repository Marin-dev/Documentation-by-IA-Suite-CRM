# AccessDeniedException.php

**Chemin :** `lib/Exception/AccessDeniedException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception lancee lorsqu'un acces est refuse a un utilisateur ou a un processus. Permet de signaler une violation d'autorisation dans l'application.

## Role technique
Etend `SuiteCRM\Exception\Exception`. Prefixe le message avec `[AccessDeniedException]`. Utilise le code `APPLICATION_UNHANDLED_BEHAVIOUR` (6000) par defaut.

---

## Dependances cles
- `SuiteCRM\Enumerator\ExceptionCode` — code d'erreur par defaut
- `SuiteCRM\Exception\Exception` — classe parente

## Exports / Symboles principaux
- `AccessDeniedException` — classe exception — acces refuse

## Relations cles
- **Appele par :** INCONNU (consommateurs a identifier par grep sur l'application)
- **Appelle :** `Exception::__construct()`
- **Position dans le flux global :** lancee en cas de violation de droits

---

## Points d'attention
- Le code 6000 (`APPLICATION_UNHANDLED_BEHAVIOUR`) est ambigu pour un acces refuse ; un code plus specifique serait souhaitable.
