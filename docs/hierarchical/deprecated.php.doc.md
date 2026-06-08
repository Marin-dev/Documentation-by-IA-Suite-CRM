# deprecated.php

**Chemin :** `deprecated.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Fichier de compatibilité ascendante (backwards compatibility) chargé automatiquement par Composer à chaque requête. Il crée des alias de classes pour les anciens noms utilisés avant la migration vers les namespaces PSR-4.

## Responsabilités
- Créer des alias `OneLogin_Saml2_*` pointant vers `OneLogin\Saml2\*` (12 classes SAML2)
- Créer un alias `Zend\Oauth\Provider` pointant vers `SuiteCRM\Zend_Oauth_Provider`
- Créer un alias `Html2Text\Html2Text` pointant vers `Soundasleep\Html2Text`
- Déclarer des classes vides portant les anciens noms si elles n'existent pas encore (garde-fou)

## Dépendances internes
- `OneLogin\Saml2\*` — classes SAML2 du vendor `onelogin/php-saml`
- `SuiteCRM\Zend_Oauth_Provider` — classe OAuth interne (namespace `SuiteCRM`)
- `Soundasleep\Html2Text` — classe du vendor `soundasleep/html2text`
- Référencé dans `composer.json` section `autoload.files` (ligne 99) : chargé à chaque bootstrap Composer

## Exports / Points d'entrée
- Alias de classe `OneLogin_Saml2_Auth`, `OneLogin_Saml2_AuthnRequest`, `OneLogin_Saml2_Constants`, `OneLogin_Saml2_Error`, `OneLogin_Saml2_ValidationError`, `OneLogin_Saml2_IdPMetadataParser`, `OneLogin_Saml2_LogoutRequest`, `OneLogin_Saml2_LogoutResponse`, `OneLogin_Saml2_Metadata`, `OneLogin_Saml2_Response`, `OneLogin_Saml2_Settings`, `OneLogin_Saml2_Utils`
- Alias de classe `Provider` (Zend OAuth)
- Alias de classe `Html2Text\Html2Text`

## Notes techniques
- Chargé via `autoload.files` dans `composer.json` : s'exécute avant tout autre code applicatif.
- Le bloc `if (!class_exists(...))` autour des classes SAML2 vides est un filet de sécurité : si `class_alias` échoue (vendor absent), les classes existent quand même pour éviter des erreurs fatales.
- Ce fichier ne doit jamais être supprimé tant que du code externe utilise les anciens noms de classes (risque de régression silencieuse).
