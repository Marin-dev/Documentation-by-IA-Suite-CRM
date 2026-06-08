# PDFEngine.php

**Chemin :** `lib/PDF/PDFEngine.php`
**Type :** PHP — Classe abstraite
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Contrat abstrait pour tous les moteurs de generation PDF de SuiteCRM. Definit l'interface commune que doivent respecter `LegacyMPDFEngine` et `TCPDFEngine`.

## Role technique
Classe abstraite PHP avec 6 methodes abstraites correspondant au cycle de vie d'un document PDF : configuration, ecriture HTML, en-tete, pied de page, CSS, page vierge, et sortie.

---

## Dependances cles
- Aucun import externe

## Exports / Symboles principaux
- `PDFEngine` — classe abstraite
  - `abstract writeHTML(string $html): void`
  - `abstract writeFooter(string $html): void`
  - `abstract writeHeader(string $html): void`
  - `abstract addCSS(string $css): void`
  - `abstract writeBlankPage(): void`
  - `abstract outputPDF(string $name, string $destination, string $fullName = ''): ?string`
  - `abstract configurePDF(array $options): void`

- **Implementeurs identifies :**
  - `lib/PDF/LegacyMPDF/LegacyMPDFEngine.php`
  - `lib/PDF/TCPDF/TCPDFEngine.php`

## Relations cles
- **Appele par :** `lib/PDF/PDFWrapper.php`
- **Position dans le flux global :** abstraction centrale du sous-systeme PDF

---

## Points d'attention
- `$configMapperFile` est declare en static private mais n'est jamais utilise dans cette classe abstraite (laisse aux sous-classes de gerer leur mapping).
