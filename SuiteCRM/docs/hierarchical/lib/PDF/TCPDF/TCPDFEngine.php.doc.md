# TCPDFEngine.php

**Chemin :** `lib/PDF/TCPDF/TCPDFEngine.php`
**Type :** PHP — Service
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Moteur PDF principal de SuiteCRM base sur TCPDF. Gere la generation complete de documents PDF avec support CSS, en-tetes/pieds de page HTML, pagination et configuration avancee des marges et polices.

## Role technique
Etend `PDFEngine`. Enveloppe un `SuiteTCPDF`. Injecte une feuille de style CSS par defaut depuis `lib/PDF/TCPDF/default.css`. Les methodes CSS empilent CSS custom + CSS par defaut dans une balise `<style>`. La methode `writeHTML()` ajoute automatiquement une page si le document est vide.

---

## Dependances cles
- `SuiteCRM\PDF\PDFEngine` — classe abstraite parente
- `SuiteCRM\PDF\TCPDF\SuiteTCPDF` — objet TCPDF personnalise
- `lib/PDF/TCPDF/configMapping.php` — mapping de configuration
- `lib/PDF/TCPDF/default.css` — CSS par defaut (charge en string)

## Exports / Symboles principaux
- `TCPDFEngine` — classe moteur PDF TCPDF
  - `writeHTML(string $html): void`
  - `outputPDF(string $name, string $destination, string $fullName): ?string`
  - `writeHeader(string $html): void` / `writeFooter(string $html): void`
  - `addCSS(string $css): void` / `getCSS(): string`
  - `writeBlankPage(): void`
  - `configurePDF(array $options): void`

## Relations cles
- **Appele par :** `lib/PDF/PDFWrapper.php`
- **Appelle :** `SuiteTCPDF`, `configMapping.php`
- **Position dans le flux global :** moteur PDF actif par defaut pour PHP >= 8.0

---

## Points d'attention
- `outputPDF()` avec destination `'D'` (download) utilise le nom seul ; les autres destinations prefixent avec le chemin du projet (ligne 114-116).
- Le CSS par defaut est toujours applique en plus du CSS personnalise.
