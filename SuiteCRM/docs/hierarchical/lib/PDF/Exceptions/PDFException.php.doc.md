# PDFException.php

**Chemin :** `lib/PDF/Exceptions/PDFException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception de base pour toutes les erreurs liees a la generation PDF dans SuiteCRM.

## Role technique
Etend `RuntimeException` PHP natif. Classe vide servant uniquement de type de base pour la hierarchie d'exceptions PDF.

---

## Dependances cles
- `RuntimeException` (PHP natif)

## Exports / Symboles principaux
- `PDFException` — classe exception de base PDF

- **Consommateurs identifies :**
  - `lib/PDF/Exceptions/PDFEngineNotFoundException.php`

## Relations cles
- **Appele par :** code applicatif de generation PDF (INCONNU — a verifier)
- **Position dans le flux global :** base de la hierarchie d'exceptions PDF

---

## Points d'attention
- RAS.
