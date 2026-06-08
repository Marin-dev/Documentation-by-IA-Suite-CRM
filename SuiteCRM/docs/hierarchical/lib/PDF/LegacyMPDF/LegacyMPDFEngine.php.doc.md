# LegacyMPDFEngine.php

**Chemin :** `lib/PDF/LegacyMPDF/LegacyMPDFEngine.php`
**Type :** PHP — Service
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Implementeur du moteur PDF base sur la librairie mPDF legacy (`modules/AOS_PDF_Templates/PDF_Lib/mpdf.php`). Gere la generation de documents PDF via cette librairie historique de SuiteCRM.

## Role technique
Etend `PDFEngine`. Enveloppe un objet `mPDF` (attribut `$pdf`). Toutes les operations mPDF sont appelees avec `@` (suppression d'erreurs). Charge `configMapping.php` via `include` pour construire les parametres du constructeur mPDF lors de `configurePDF()`.

---

## Dependances cles
- `mPDF` — librairie mPDF legacy (`modules/AOS_PDF_Templates/PDF_Lib/mpdf.php`)
- `SuiteCRM\PDF\PDFEngine` — classe abstraite parente
- `lib/PDF/LegacyMPDF/configMapping.php` — mapping de configuration

## Exports / Symboles principaux
- `LegacyMPDFEngine` — classe moteur PDF legacy
  - `writeHTML(string $html, int $section, bool $init, bool $close): void`
  - `outputPDF(string $name, string $destination, string $fullName): ?string`
  - `writeHeader(string $html): void`
  - `writeFooter(string $html): void`
  - `addCSS(string $css): void`
  - `writeBlankPage(): void`
  - `configurePDF(array $options): void`

## Relations cles
- **Appele par :** `lib/PDF/PDFWrapper.php`
- **Appelle :** librairie `mPDF`, `configMapping.php`
- **Position dans le flux global :** moteur PDF legacy, non compatible PHP >= 8.0

---

## Points d'attention
- Incompatible PHP >= 8.0 (exclu par `PDFWrapper::getEngines()` ligne 122).
- Le `@` sur les appels mPDF masque des erreurs potentielles.
- Lors de `writeHTML()` avec `$section === 1`, force le background-color a blanc et supprime font-size des INPUT (ligne 89-91).
