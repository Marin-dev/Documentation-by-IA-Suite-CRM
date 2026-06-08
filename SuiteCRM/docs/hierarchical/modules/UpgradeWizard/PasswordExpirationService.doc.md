# PasswordExpirationService.php

**Chemin :** `modules/UpgradeWizard/PasswordExpirationService.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Service gérant la notification d'expiration des mots de passe lors du wizard de mise à jour. Génère un message d'avertissement avec un lien vers la configuration du gestionnaire de mots de passe dans l'Administration.

## Type
service

## Dépendances clés
- `$sugar_config` — configuration globale (site_url)
- `$mod_strings` — traductions (LBL_PASSWORD_EXPIRATON_CHANGED, LBL_PASSWORD_EXPIRATON_REDIRECT)

## Exports / Symboles principaux
- `PasswordExpirationService` (classe)
  - `getExpirationMessage()` — retourne un message HTML avec lien vers `Administration/PasswordManager`
  - `setExpiration()` — configure les paramètres d'expiration (INCONNU - non lu en détail)

## Interactions
- **Appelé par :** processus UpgradeWizard (INCONNU - consommateurs non vérifiés)
- **Appelle :** `sprintf()` pour formater le message

## Notes
- Génère un lien vers `index.php?module=Administration&action=PasswordManager`.
