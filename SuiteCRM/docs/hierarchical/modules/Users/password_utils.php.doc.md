# Fichier : password_utils.php

**Chemin :** `modules/Users/password_utils.php`
**Type :** PHP — Helper (utilitaires mot de passe)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit deux fonctions utilitaires liees aux mots de passe : verification que l'envoi d'un mot de passe par email est possible (`canSendPassword`), et verification si le mot de passe d'un utilisateur a expire (`hasPasswordExpired`).

## Role technique

Fichier de fonctions procedurales. `canSendPassword()` instancie `SugarPHPMailer`, verifie la configuration SMTP et la presence d'un template email de generation de mot de passe. `hasPasswordExpired()` instancie un bean `User`, charge les parametres de politique depuis `$sugar_config['passwordsetting']`, et calcule l'expiration selon le type (temporel `case 1` ou par nombre de connexions `case 2`).

---

## Dependances principales

| Import | Role |
|---|---|
| `SugarPHPMailer` | Verification configuration SMTP |
| `BeanFactory::newBean('EmailTemplates')` | Verification template email |
| `User` | Bean utilisateur pour verification expiration |
| `$GLOBALS['sugar_config']['passwordsetting']` | Politique de mot de passe |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `canSendPassword()` | fonction | Retourne `null` (OK admin) ou string d'erreur |
| `hasPasswordExpired($username)` | fonction | Retourne `true` si expire, `false` sinon (ou rien si cas non couvre) |

## Consommateurs identifies

- INCONNU (a rechercher par grep sur `canSendPassword` et `hasPasswordExpired`)

---

## Relations cles

- **Appele par :** INCONNU — probablement le flux d'authentification
- **Appelle :** `SugarPHPMailer`, `BeanFactory`, `User`, `TimeDate`

---

## Points d'attention

- `hasPasswordExpired()` ne retourne rien (implicit `null`) pour les utilisateurs portail ou avec mot de passe systeme non genere — le comportement est `false` par defaut implicite.
- Le type d'expiration `case 2` (par nombre de connexions) incremente `loginexpiration` dans les preferences et sauvegarde a chaque appel — potentiel double-increment si appele plusieurs fois par connexion.
- `canSendPassword()` retourne une chaine d'erreur multi-ligne (avec `<br>`) — format HTML, a ne pas echo brut dans du JSON.
