# Fichier generatePdf.php — AOS_PDF_Templates

**Chemin :** `modules/AOS_PDF_Templates/generatePdf.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Script de génération et téléchargement d'un PDF à partir d'un template AOS_PDF_Templates et d'un bean SuiteCRM. Invoqué depuis la DetailView des modules AOS (Quotes, Invoices, Contracts) et Contacts, Accounts, Leads.

## Type
autre (script de génération)

## Dépendances clés
- `AOS_PDF_Templates`, `templateParser`
- `PDFWrapper` (SuiteCRM PDF engine)
- `BeanFactory`

## Notes
Point d'entrée HTTP : `index.php?module=AOS_PDF_Templates&action=generatePdf&record={id}&bean_id={id}&bean_module={module}`.
