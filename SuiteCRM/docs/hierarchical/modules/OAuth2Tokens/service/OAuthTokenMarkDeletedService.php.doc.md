# 📄 OAuthTokenMarkDeletedService.php

**Chemin :** `modules/OAuth2Tokens/service/OAuthTokenMarkDeletedService.php`
**Type :** PHP — service de nettoyage (scheduler)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Service de nettoyage des tokens OAuth2 expirés ou révoqués. Marque comme supprimés les tokens dont à la fois l'access token ET le refresh token sont expirés, ou les tokens révoqués dont la date de modification est antérieure au seuil.

## Rôle technique

Classe `OAuthTokenMarkDeletedService` (non héritante). Structure identique à `OAuthCodeMarkDeletedService`. Le seuil est configurable via `oauth_token_delete_threshold` (défaut `-7 days`).

---

## Dépendances clés

- `DBManagerFactory` — accès DB
- `Configurator` — lecture de `oauth_token_delete_threshold`
- `$GLOBALS['log']` — journalisation

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuthTokenMarkDeletedService` | classe | Service de nettoyage des tokens OAuth2 |
| `run()` | méthode | Exécute le nettoyage |

---

## Relations clés

- **Appelé par :** scheduler SuiteCRM (INCONNU — job name non lu)
- **Appelle :** `DBManagerFactory`, `Configurator`
- **Position dans le flux global :** maintenance périodique de la table `oauth2tokens`

---

## Notes

- Un token est supprimé si : (`refresh_token_expires < seuil` ET `access_token_expires < seuil`) OU (`token_is_revoked = 1` ET `date_modified < seuil`).
- Soft delete uniquement.
