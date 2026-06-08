# AOPInboundEmail.php

**Chemin :** `modules/InboundEmail/AOPInboundEmail.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Extension de `InboundEmail` dédiée au traitement des emails entrants pour le module AOS/AOP (Advanced OpenCases/Process). Gère spécifiquement le polling des boîtes surveillées pour la création automatique de cas. Inclut le traitement des images inline (CID).

## Type

model

---

## Dépendances clés

- `InboundEmail` (classe parente)
- `include/clean.php`
- `$sugar_config['site_url']` — URL pour les liens d'images

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOPInboundEmail` | classe | Extension InboundEmail pour AOP |
| `$job_name` | propriété | Nom du job scheduler : `function::pollMonitoredInboxesAOP` |
| `processImageLinks()` | méthode | Remplace les liens `cid:` d'images inline par des URLs SuiteCRM |

## Interactions

- **Appelé par :** `EmailImportService::run()`, scheduler `pollMonitoredInboxesAOP`
- **Appelle :** `InboundEmail` (héritage)

## Notes

- Le job scheduler `pollMonitoredInboxesAOP` est le point d'entrée pour l'importation automatique des emails en cas.
- `processImageLinks()` convertit les images embarquées (CID) en liens vers l'entryPoint `download`.
