# 📄 OAuthCodeMarkDeletedService.php

**Chemin :** `modules/OAuth2AuthCodes/services/OAuthCodeMarkDeletedService.php`
**Type :** PHP — service de nettoyage (scheduler)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Service de nettoyage des codes d'autorisation OAuth2 expirés. Marque comme supprimés (`deleted=1`) les codes d'autorisation dont la date d'expiration est antérieure au seuil configuré.

## Rôle technique

Classe `OAuthCodeMarkDeletedService` (non héritante). La méthode `run()` exécute un UPDATE SQL sur `oauth2authcodes`. Le seuil de suppression est configurable via `oauth_code_delete_threshold` dans la configuration SuiteCRM (format `-N days`), par défaut `-7 days`.

---

## Dépendances clés

- `DBManagerFactory` — accès DB
- `Configurator` — lecture de `oauth_code_delete_threshold`
- `$GLOBALS['log']` — journalisation

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuthCodeMarkDeletedService` | classe | Service de nettoyage des codes d'autorisation |
| `run()` | méthode | Exécute le nettoyage |

---

## Relations clés

- **Appelé par :** scheduler SuiteCRM (INCONNU — job name non lu)
- **Appelle :** `DBManagerFactory`, `Configurator`
- **Position dans le flux global :** maintenance périodique, empêche l'accumulation de codes expirés en DB

---

## Notes

- Le seuil est validé par regex `/^-\d+\s+days$/` — toute valeur invalide retombe sur `-7 days`.
- Soft delete uniquement (`deleted=1`, pas de DELETE physique).
