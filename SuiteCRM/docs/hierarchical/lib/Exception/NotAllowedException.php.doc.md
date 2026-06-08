# NotAllowedException.php

**Chemin :** `lib/Exception/NotAllowedException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception lancee lorsqu'une action est non autorisee (HTTP 405 ou refus metier). Utilisee notamment pour les echecs de negociation de contenu API.

## Role technique
Etend `SuiteCRM\Exception\Exception`. Prefixe avec `[Not Allowed]`. Code par defaut : `API_CONTENT_NEGOTIATION_FAILED` (8005).

---

## Dependances cles
- `SuiteCRM\Enumerator\ExceptionCode`
- `SuiteCRM\Exception\Exception`

## Exports / Symboles principaux
- `NotAllowedException` — classe exception

## Relations cles
- **Appele par :** INCONNU (a rechercher dans l'API)
- **Appelle :** `Exception::__construct()`

---

## Points d'attention
- Le code par defaut (`API_CONTENT_NEGOTIATION_FAILED`) suggere une utilisation principalement cote API V8.
