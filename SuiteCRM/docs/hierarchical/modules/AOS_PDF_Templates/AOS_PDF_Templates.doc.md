# AOS_PDF_Templates.php

**Chemin :** `modules/AOS_PDF_Templates/AOS_PDF_Templates.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele principal des templates PDF du module AOS. Represente un gabarit de document PDF (entete, corps, pied de page) associe a un module CRM, utilisable pour generer des PDF de devis, factures, contrats, etc.

## Role technique
Etend `AOS_PDF_Templates_sugar`. Surcharge `cleanBean()` pour purifier le HTML des champs `pdfheader`, `description` et `pdffooter` en interdisant les `<iframe>` (securite XSS).

---

## Dependances / Imports
- `AOS_PDF_Templates_sugar` (classe parente generee)
- `purify_html()` — fonction de purification HTML SuiteCRM

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `AOS_PDF_Templates` | Classe | Modele de template PDF |
| `cleanBean()` | Methode | Purification HTML des champs header/body/footer |

**Consommateurs identifies :**
- `modules/AOS_PDF_Templates/generatePdf.php` — generation du PDF final
- `modules/AOS_PDF_Templates/formLetter.php` — generation de lettre
- `modules/AOS_PDF_Templates/formLetterPdf.php` — generation lettre en PDF
- `modules/AOS_PDF_Templates/sendEmail.php` — envoi par email

## Relations cles
- **Table DB :** `aos_pdf_templates`
- **Appelle :** `purify_html()` avec interdiction de `<iframe>`

---

## Points d'attention
- La purification HTML interdit uniquement `<iframe>` — d'autres balises potentiellement dangereuses ne sont pas filtrees par ce code.
- La logique de generation PDF effective est dans `templateParser.php`, `generatePdf.php`, etc. — pas dans ce modele.
