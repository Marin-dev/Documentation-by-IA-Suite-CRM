# generatePdf.php

**Chemin :** `modules/AOS_PDF_Templates/generatePdf.php`
**Type :** PHP - Script d'action (generation PDF)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script de generation et telechargement d'un PDF a partir d'un template AOS_PDF_Templates et d'un enregistrement CRM. Point d'entree pour la generation de PDF depuis la DetailView d'un module.

## Role technique
Script PHP execute directement. Verifie la presence de `uid` (ID du record) et `templateID`. Utilise `templateParser` pour la substitution de variables, `PDFWrapper` pour la generation PDF via mPDF.

---

## Dependances / Imports
- `SuiteCRM\PDF\PDFWrapper` — moteur PDF mPDF
- `SuiteCRM\PDF\Exceptions\PDFException`
- `modules/AOS_PDF_Templates/templateParser.php`
- `modules/AOS_PDF_Templates/sendEmail.php`
- `modules/AOS_PDF_Templates/AOS_PDF_Templates.php`
- `$_REQUEST['uid']` — ID du record source
- `$_REQUEST['templateID']` — ID du template PDF

## Relations cles
- **Appele par :** Bouton "Generer PDF" sur les DetailViews AOS
- **Appelle :** `templateParser::parse_template()`, `PDFWrapper::getPDFEngine()`

---

## Points d'attention
- Retourne une erreur immediate si `uid` ou `templateID` sont absents.
- La logique complete de construction du PDF est dans la suite du fichier (limite de lecture) — INCONNU pour les details.
- Utilise `sendEmail.php` — peut aussi declencher un envoi par email du PDF.
