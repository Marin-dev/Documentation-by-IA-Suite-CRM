# Invoices

## Rôle
Tests d'acceptation du module Invoices (factures) de SuiteCRM. Vérifie la création, la modification et la génération PDF des factures à partir de devis ou directement.

## Contenu
| Fichier | Rôle |
|---|---|
| `InvoicesCest.php` | Scénarios d'acceptation pour le module Invoices |

## Points d'entrée
- `InvoicesCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié aux modules Quotes, `AOS_PDF_Templates`, `AOS_Products`.
