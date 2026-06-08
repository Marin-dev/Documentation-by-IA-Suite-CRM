# oauth_nonce.php

**Chemin :** `metadata/oauth_nonce.php`
**Type :** config (métadonnées de table de sécurité OAuth)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `oauth_nonce` utilisée par le mécanisme OAuth de SuiteCRM pour stocker les nonces (nombres utilisés une seule fois). Protège contre les attaques de rejeu (replay attacks) lors de l'authentification OAuth.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['oauth_nonce']` | variable globale PHP | Définition de la table OAuth nonce |

### Structure de la table `oauth_nonce`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `conskey` | varchar(32) | Clé consommateur OAuth (requis, non null) |
| `nonce` | varchar(32) | Valeur nonce (requis, non null) |
| `nonce_ts` | long | Timestamp de la demande OAuth |

### Index

| Nom | Type | Champs |
|---|---|---|
| `oauth_nonce_pk` | primary | `conskey`, `nonce` |
| `oauth_nonce_keyts` | index | `conskey`, `nonce_ts` |

## Interactions

- **Appelé par :** couche OAuth de SuiteCRM (authentification API)
- **Appelle :** rien

## Notes

- Clé primaire composite `(conskey, nonce)` : garantit qu'un même nonce ne peut être utilisé deux fois pour un même consommateur.
- L'index `(conskey, nonce_ts)` permet le nettoyage des nonces périmés par timestamp.
- Le commentaire de ce fichier indique "storing reports filter information" (ligne 46) — erreur de copier-coller dans la documentation inline.
