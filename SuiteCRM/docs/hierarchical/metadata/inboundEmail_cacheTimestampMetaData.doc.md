# inboundEmail_cacheTimestampMetaData.php

**Chemin :** `metadata/inboundEmail_cacheTimestampMetaData.php`
**Type :** config (métadonnées de table de timestamp de cache email)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `inbound_email_cache_ts` qui stocke les timestamps de cache pour les boîtes email entrantes. Permet au système de savoir quand le cache email d'une boîte a été mis à jour pour éviter des rechargements inutiles.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['InboundEmail_cacheTimestamp']` | variable globale PHP | Définition de la table |

### Structure de la table `inbound_email_cache_ts`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(255) | Clé primaire — identifiant du cache (requis) |
| `ie_timestamp` | uint(16) | Timestamp de la dernière mise à jour du cache |

### Index

| Nom | Type | Champs |
|---|---|---|
| `ie_cachetimestamppk` | primary | `id` |

## Interactions

- **Appelé par :** module InboundEmail, système de cache IMAP
- **Appelle :** rien

## Notes

- `id` est un varchar(255) — pas un UUID standard. Le format de cette clé est INCONNU (probablement `ie_id + mbox` ou similaire).
- Table minimaliste : 2 colonnes seulement.
- Utilisée conjointement avec `email_cache` pour valider la fraîcheur des données IMAP.
