# Overview.php

**Chemin :** `modules/InboundEmail/Overview.php`
**Type :** model (DTO)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Classe miroir d'un email IMAP récupéré via `imap_fetch_overview()`. Structure de données légère portant les métadonnées d'un email (sujet, expéditeur, destinataire, date, flags) et les définitions de champs du cache email.

## Type

model (DTO)

---

## Dépendances clés

- `$dictionary['email_cache']` — métadonnées de la table cache email (`metadata/email_cacheMetaData.php` ou `custom/`)

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Overview` | classe | DTO pour les métadonnées d'un email IMAP |
| `$subject`, `$from`, `$to`, `$date`, `$uid`, `$msgno` | propriétés | Métadonnées de l'email |
| `$flagged`, `$answered`, `$deleted`, `$seen`, `$draft` | propriétés | Flags IMAP |
| `$fieldDefs`, `$indices` | propriétés | Définitions du cache email |

## Interactions

- **Appelé par :** `InboundEmail` (inclus via require_once)
- **Appelle :** aucun

## Notes

- Simple DTO sans logique métier — wrapper des données `imap_fetch_overview()`.
