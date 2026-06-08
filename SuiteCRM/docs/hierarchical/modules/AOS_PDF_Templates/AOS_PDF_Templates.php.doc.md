# Fichier AOS_PDF_Templates.php

**Chemin :** `modules/AOS_PDF_Templates/AOS_PDF_Templates.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle des modèles PDF. Représente un template HTML utilisé pour générer des documents PDF à partir de beans SuiteCRM (devis, factures, contacts, leads, comptes). Surcharge `cleanBean()` pour purifier les champs HTML des injections iframe.

## Type
model

---

## Dépendances clés
- `AOS_PDF_Templates_sugar` (classe parente générée)
- `purify_html()` — nettoyage XSS des champs HTML
- `modules/AOS_PDF_Templates/templateParser.php` — moteur de rendu des variables

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOS_PDF_Templates` | classe | Bean template PDF |
| `cleanBean()` | méthode | Purifie `pdfheader`, `description`, `pdffooter` (bloque les iframes) |

### Champs importants (INCONNU — à confirmer dans sugar)
| Champ | Rôle |
|---|---|
| `pdfheader` | En-tête HTML du template |
| `description` | Corps HTML du template (avec variables `{module_field}`) |
| `pdffooter` | Pied de page HTML |
| `body_header` | INCONNU |

## Interactions
- **Appelé par :** `formLetterPdf.php`, `generatePdf.php`, `sendEmail.php` (dans le même module), `AOR_ReportsController::action_downloadPDF()`
- **Appelle :** `templateParser::parse_template()`, `purify_html()`
- **Table BD :** `aos_pdf_templates`

## Notes
- `cleanBean()` utilise `purify_html()` avec `HTML.ForbiddenElements => ['iframe' => true]` — les autres éléments dangereux ne sont pas explicitement bloqués.
- Le moteur de templates utilise des variables de type `{table_fieldname}` remplacées par `templateParser`.
