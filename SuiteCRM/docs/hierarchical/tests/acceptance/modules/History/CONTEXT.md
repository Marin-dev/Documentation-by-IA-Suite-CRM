# History

## Rôle
Tests d'acceptation du module History (historique) de SuiteCRM. Vérifie l'affichage et la gestion du sous-panneau historique des activités (e-mails, notes, appels archivés) sur les modules principaux.

## Contenu
| Fichier | Rôle |
|---|---|
| `HistoryCest.php` | Scénarios d'acceptation pour le module History |

## Points d'entrée
- `HistoryCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Module transversal — l'historique apparaît sur Accounts, Contacts, Opportunities, Cases.
