# NotFoundException.php

**Chemin :** `lib/Exception/NotFoundException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception lancee lorsqu'une ressource demandee est introuvable (analogue HTTP 404). Utilisee dans l'API et dans les modules.

## Role technique
Etend `SuiteCRM\Exception\Exception`. Prefixe avec `[Not Found]`. Code par defaut : `API_CONTENT_NEGOTIATION_FAILED` (8005) — noter que ce code est potentiellement incorrect pour un 404.

---

## Dependances cles
- `SuiteCRM\Enumerator\ExceptionCode`
- `SuiteCRM\Exception\Exception`

## Exports / Symboles principaux
- `NotFoundException` — classe exception

## Relations cles
- **Appele par :** INCONNU
- **Appelle :** `Exception::__construct()`

---

## Points d'attention
- Le code par defaut `API_CONTENT_NEGOTIATION_FAILED` (8005) semble incorrect pour une ressource non trouvee ; `API_RECORD_NOT_FOUND` (8050) serait plus adapte.
