# SuiteTCPDF.php

**Chemin :** `lib/PDF/TCPDF/SuiteTCPDF.php`
**Type :** PHP — Service (extension de TCPDF)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Sous-classe de `TCPDF` personnalisee pour SuiteCRM. Gere les en-tetes et pieds de page HTML, remplace les tokens `{PAGENO}` et `{DATE format}` dans les pieds de page, et securise l'affichage d'images externes via `validate_external_host()`.

## Role technique
Etend `TCPDF`. Surcharge `Header()` et `Footer()` pour injecter du HTML via `writeHTMLCell()`. La methode `Image()` surcharge la methode parente pour valider l'hote externe avant le chargement (`validate_external_host()`).

---

## Dependances cles
- `TCPDF` — librairie TCPDF (vendor)
- `validate_external_host()` — fonction globale SuiteCRM de validation d'URL

## Exports / Symboles principaux
- `SuiteTCPDF` — classe
  - `setHtmlHeader(string): void` / `getHtmlHeader(): string`
  - `setHtmlFooter(string): void` / `getHtmlFooter(): string` — remplace `{PAGENO}` et tokens `{DATE format}`
  - `Header(): void` — surcharge TCPDF
  - `Footer(): void` — surcharge TCPDF
  - `Image(...)` — surcharge avec validation de l'hote

- **Consommateurs identifies :**
  - `lib/PDF/TCPDF/TCPDFEngine.php`

## Relations cles
- **Appele par :** `TCPDFEngine`
- **Appelle :** `TCPDF`, `validate_external_host()`
- **Position dans le flux global :** couche de personnalisation TCPDF pour SuiteCRM

---

## Points d'attention
- `Image()` retourne `false` (sans erreur) si l'hote n'est pas valide — comportement silencieux.
- Le token `{DATE format}` est traite via `preg_replace_callback` avec `date()` (ligne 71).
