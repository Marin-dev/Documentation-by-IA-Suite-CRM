# Cases

## Rôle
Tests d'acceptation du module Cases (incidents/tickets support) de SuiteCRM. Vérifie la création, l'escalade et la résolution des dossiers de support client.

## Contenu
| Fichier | Rôle |
|---|---|
| `CasesCest.php` | Scénarios d'acceptation pour le module Cases |

## Points d'entrée
- `CasesCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/Cases.php`
- Utilisé par : pipeline CI/CD

## Notes
Lié aux modules `AOK_KnowledgeBase`, Contacts, Accounts.
