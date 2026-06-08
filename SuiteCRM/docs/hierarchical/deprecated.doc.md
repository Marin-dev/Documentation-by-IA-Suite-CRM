# deprecated.php

**Chemin :** `deprecated.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Fichier de rétrocompatibilité chargé automatiquement par Composer à chaque démarrage de l'application. Crée des alias de classes pour permettre à du code legacy utilisant les anciens noms de classes de continuer à fonctionner sans modification.

**Type :** helper (autoload Composer)

## Rôle technique

Enregistre des alias PHP via `class_alias()` pour trois familles de classes :
1. **OneLogin SAML2** — mappe `OneLogin_Saml2_*` vers `OneLogin\Saml2\*` (11 classes)
2. **Zend OAuth** — mappe `Zend\Oauth\Provider` vers `SuiteCRM\Zend_Oauth_Provider`
3. **Html2Text** — mappe `Html2Text\Html2Text` vers `Soundasleep\Html2Text`

Si les alias échouent (classes non trouvées), des classes vides avec `#[\AllowDynamicProperties]` sont définies en fallback.

---

## Dépendances clés

- **Imports principaux :** aucun (fichier autocontenu)
- **Classes sources requises (à l'exécution) :**
  - `OneLogin\Saml2\*` (via `onelogin/php-saml`)
  - `SuiteCRM\Zend_Oauth_Provider` (interne SuiteCRM)
  - `Soundasleep\Html2Text` (via `soundasleep/html2text`)

## Exports / Aliases créés

| Alias (ancien nom) | Classe cible (nouveau nom) |
|---|---|
| `OneLogin_Saml2_Auth` | `OneLogin\Saml2\Auth` |
| `OneLogin_Saml2_AuthnRequest` | `OneLogin\Saml2\AuthnRequest` |
| `OneLogin_Saml2_Constants` | `OneLogin\Saml2\Constants` |
| `OneLogin_Saml2_Error` | `OneLogin\Saml2\Error` |
| `OneLogin_Saml2_ValidationError` | `OneLogin\Saml2\ValidationError` |
| `OneLogin_Saml2_IdPMetadataParser` | `OneLogin\Saml2\IdPMetadataParser` |
| `OneLogin_Saml2_LogoutRequest` | `OneLogin\Saml2\LogoutRequest` |
| `OneLogin_Saml2_LogoutResponse` | `OneLogin\Saml2\LogoutResponse` |
| `OneLogin_Saml2_Metadata` | `OneLogin\Saml2\Metadata` |
| `OneLogin_Saml2_Response` | `OneLogin\Saml2\Response` |
| `OneLogin_Saml2_Settings` | `OneLogin\Saml2\Settings` |
| `OneLogin_Saml2_Utils` | `OneLogin\Saml2\Utils` |
| `Zend\Oauth\Provider` | `SuiteCRM\Zend_Oauth_Provider` |
| `Html2Text\Html2Text` | `Soundasleep\Html2Text` |

## Relations clés

- **Appelé par :** Composer autoloader (déclaré dans `composer.json` > `autoload.files`) — chargé à chaque requête
- **Appelle :** rien (pur enregistrement d'aliases)

---

## Points d'attention

- Ce fichier est chargé **avant tout autre code applicatif** par Composer — toute erreur de syntaxe bloque l'ensemble de l'application.
- Les classes vides définies en fallback (lignes 26-61) sont du code mort si les packages Composer sont correctement installés.
- `#[\AllowDynamicProperties]` est requis pour PHP 8.2+ qui interdit les propriétés dynamiques par défaut.
