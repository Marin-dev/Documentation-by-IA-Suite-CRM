# EAPM.php

**Chemin :** `modules/EAPM/EAPM.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle des comptes d'APIs externes utilisateurs (External API Manager). Stocke les credentials de connexion aux services externes (Google, Dropbox, etc.) par utilisateur, avec mot de passe chiffré. Utilisé par le module Connectors et EAPM pour l'authentification OAuth/basique.

## Type

model

---

## Dépendances clés

- `Basic` (`include/SugarObjects/templates/basic/Basic.php`) — classe parente
- `ExternalAPIFactory` (`include/externalAPI/ExternalAPIFactory.php`)
- `SugarOauth` (`include/SugarOauth.php`)
- `blowfishDecode()` / `blowfishGetKey()` (`include/utils/encryption_utils.php`)
- `$_SESSION['EAPM']` — cache des credentials

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `EAPM` | classe | Entité compte API externe par utilisateur (table `eapm`) |
| `getLoginInfo()` | méthode statique | Récupère les credentials d'un utilisateur pour une application donnée (cache session) |
| `save()` | méthode | Sauvegarde avec protection du placeholder de mot de passe |
| `create_new_list_query()` | méthode | Restreint la liste aux enregistrements de l'utilisateur courant (non-admin) |
| `$passwordPlaceholder` | constante statique | `'::PASSWORD::'` — valeur sentinelle pour ne pas réinitialiser le mot de passe |

## Interactions

- **Appelé par :** ExternalAPIFactory, module Connectors, vues Documents (doc_type externe)
- **Appelle :** `blowfishDecode()` (déchiffrement mot de passe), ExternalAPIFactory

## Notes

- `disable_row_level_security = true` : les enregistrements EAPM sont filtrés manuellement par `assigned_user_id` dans `create_new_list_query()`.
- Le mot de passe est chiffré en base (Blowfish). `getLoginInfo()` le déchiffre avant de le retourner.
- Cache session `$_SESSION['EAPM'][$application]` évite les requêtes répétées en base.
