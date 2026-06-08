# Quotes

## Rôle
Tests d'acceptation du module Quotes (devis) de SuiteCRM. Vérifie la création de devis avec lignes de produits, calcul des totaux, génération PDF et conversion en facture.

## Contenu
| Fichier | Rôle |
|---|---|
| `QuotesCest.php` | Scénarios d'acceptation pour le module Quotes |

## Points d'entrée
- `QuotesCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié aux modules `AOS_Products`, `AOS_PDF_Templates`, Invoices, Opportunities.
