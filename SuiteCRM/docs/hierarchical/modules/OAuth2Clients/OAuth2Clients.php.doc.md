# 📄 OAuth2Clients.php

**Chemin :** `modules/OAuth2Clients/OAuth2Clients.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle représentant un client OAuth2 enregistré dans SuiteCRM. Un client OAuth2 est une application tierce autorisée à accéder à l'API SuiteCRM au nom d'un utilisateur. Gère les différents types de grants (Authorization Code, Client Credentials, Password).

## Rôle technique

Classe `OAuth2Clients` héritant de `SugarBean` (table `oauth2clients`). Surcharge `save()` pour hacher le secret (`sha256` du `new_secret` du formulaire) et calculer `duration_value` en secondes à partir de `duration_amount` + `duration_unit`.

---

## Dépendances clés

- `SugarBean` — classe parente ORM
- `$_REQUEST['new_secret']`, `duration_amount`, `duration_unit` — paramètres du formulaire

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuth2Clients` | classe | Modèle client OAuth2 |
| `save($check_notify)` | méthode | Hache le secret et calcule duration_value avant sauvegarde |

## Champs principaux

| Champ | Rôle |
|---|---|
| `secret` | Secret haché (SHA-256) du client |
| `redirect_uri` | URI de redirection autorisée |
| `allowed_grant_type` | Type de grant (authorization_code, client_credentials, password) |
| `duration_value` | Durée de vie du token en secondes |

---

## Relations clés

- **Appelé par :** vues `view.detail.php`, `view.edit.php`, serveur OAuth2 API V8
- **Appelle :** `SugarBean::save()`
- **Position dans le flux global :** configuration des applications tierces autorisées à utiliser l'API OAuth2

---

## Notes

- Le secret est haché en SHA-256 uniquement si `$_REQUEST['new_secret']` est non vide — le secret existant est conservé si le champ est laissé vide lors de l'édition.
- `duration_value` par défaut = 60 secondes (1 minute) si les champs de durée sont absents.
- `disable_row_level_security = true`.
