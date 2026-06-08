# PDFEngineNotFoundException.php

**Chemin :** `lib/PDF/Exceptions/PDFEngineNotFoundException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception lancee lorsque le moteur PDF demande n'existe pas ou n'est pas accessible.

## Role technique
Classe vide qui etend `PDFException`. Le type seul suffit pour etre catch specifiquement dans `PDFWrapper::fetchEngine()`.

---

## Dependances cles
- `SuiteCRM\PDF\Exceptions\PDFException`

## Exports / Symboles principaux
- `PDFEngineNotFoundException` — exception moteur PDF introuvable

- **Consommateurs identifies :**
  - `lib/PDF/PDFWrapper.php` (lignes 157, 165, 173 — throws)

## Relations cles
- **Appele par :** `PDFWrapper::fetchEngine()`
- **Position dans le flux global :** lancee lors de la resolution du moteur PDF

---

## Points d'attention
- RAS.
