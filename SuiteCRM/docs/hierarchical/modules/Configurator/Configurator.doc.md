# Configurator.php

**Chemin :** `modules/Configurator/Configurator.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe centrale de configuration de SuiteCRM. Lit, valide et écrit les paramètres dans `config_override.php`. Gère la configuration de l'authentification (SAML, authenticationClass), le mode développeur, les options d'affichage, et d'autres paramètres système.

## Type
service / config

## Dépendances clés
- `config_override.php` (lecture/écriture)
- `$sugar_config` (global)

## Exports / Symboles principaux
- `Configurator` (classe)
  - `$config` — tableau de configuration courant
  - `$override` — chemin vers config_override.php
  - `$allow_undefined` — liste de clés autorisées sans définition préalable (SAML, auth, etc.)
  - `$errors` — tableau d'erreurs de validation
  - `$useAuthenticationClass` — activation classe d'auth custom

## Interactions
- **Appelé par :** `modules/Configurator/controller.php`, vues admin
- **Appelle :** écriture dans `config_override.php`

## Notes
- Les clés `$allow_undefined` incluent SAML_loginurl, SAML_logouturl, SAML_X509Cert — sécurité critique à ne pas altérer sans précaution.
