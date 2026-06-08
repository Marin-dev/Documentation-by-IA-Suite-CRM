# EmailImportService.php

**Chemin :** `modules/InboundEmail/Services/EmailImportService.php`
**Type :** helper (service)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Service d'importation des emails entrants. Orchestre le polling d'un compte `InboundEmail` actif à la fois, récupère les emails et les importe dans SuiteCRM (création de cas, leads, etc.). Utilisé par le scheduler.

## Type

helper (service)

---

## Dépendances clés

- `AOPInboundEmail` (`modules/InboundEmail/AOPInboundEmail.php`)
- `Configurator` (`modules/Configurator/Configurator.php`)
- `SuiteValidator` (`SuiteCRM\Utility\SuiteValidator`)
- Base de données — requête pour le prochain compte à importer

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `EmailImportService` | classe | Service d'importation email |
| `run()` | méthode | Exécute le polling d'un compte InboundEmail ; retourne bool |
| `getNextInboundEmailAccountToImport()` | méthode | Requête le prochain compte actif à traiter |
| `importFromInboundEmailAccount()` | méthode | Lance l'importation depuis un compte donné |

## Interactions

- **Appelé par :** scheduler SuiteCRM (job `pollMonitoredInboxesAOP`)
- **Appelle :** `AOPInboundEmail::retrieve()`, `AOPInboundEmail` (importation)

## Notes

- Traite un compte à la fois par exécution pour éviter les timeouts.
- Retourne `true` si aucun compte à traiter (pas d'erreur).
- Gestion d'exception avec log en cas d'erreur d'importation.
