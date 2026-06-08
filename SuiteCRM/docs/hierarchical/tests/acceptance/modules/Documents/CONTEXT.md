# Documents

## Rôle
Tests d'acceptation du module Documents de SuiteCRM. Vérifie l'upload, la gestion des versions et les relations des documents avec les autres entités CRM.

## Contenu
| Fichier | Rôle |
|---|---|
| `DocumentsCest.php` | Scénarios d'acceptation pour le module Documents |

## Points d'entrée
- `DocumentsCest` — suite de tests du module

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/Step/Acceptance/`
- Utilisé par : pipeline CI/CD

## Notes
Lié aux modules Contracts et aux APIs externes de stockage (Google Drive via `externalAPI/`).
