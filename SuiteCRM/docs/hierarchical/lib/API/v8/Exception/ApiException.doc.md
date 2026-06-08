# Fichier : ApiException.php

**Chemin :** `lib/API/v8/Exception/ApiException.php`
**Type :** PHP — exception (classe de base)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Classe de base de toutes les exceptions spécifiques à l'API v8 de SuiteCRM. Elle étend `LangException` (support i18n des messages) et enrichit le mécanisme d'exception standard PHP avec des informations JSON:API : `source` (pointeur JSON), `detail` (texte détaillé i18n) et `httpStatus` (code HTTP à retourner au client).

**Type :** exception (service)

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `SuiteCRM\LangException` | Exception avec support multilingue |
| `SuiteCRM\LangText` | Objet de texte localisé |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ApiException` | classe | Exception de base API v8 |
| `MSG_PREFIX` | constante | `[SuiteCRM] [API]` — préfixe dans le message |
| `DEFAULT_CODE` | constante | `8000` — code d'erreur par défaut |
| `HTTP_STATUS` | constante | `500` — statut HTTP par défaut |
| `DETAIL_TEXT_LABEL` | constante | `LBL_API_EXCEPTION_DETAIL` — clé i18n |
| `getDetail()` | méthode | Retourne le détail localisé de l'exception |
| `setDetail()` | méthode | Injecte un `LangText` comme détail |
| `setSource()` / `getSource()` | méthodes | Définit/retourne le pointeur JSON (`pointer`) |
| `getHttpStatus()` | méthode | Retourne le code HTTP approprié |

---

## Interactions

**Appelé par :**
- `ApiController::generateJsonApiErrorResponse()` — détecte `is_subclass_of($exception, ApiException::class)` pour extraire `detail`, `source`, `httpStatus`
- Toutes les sous-classes dans `lib/API/v8/Exception/`

**Appelle :**
- `LangException::__construct()` — construction avec préfixe automatique

---

## Notes

- La garde `if (!defined('sugarEntry') || !sugarEntry)` en ligne 47 empêche l'accès direct au fichier hors du contexte SuiteCRM.
- Le préfixe de message est construit dynamiquement : si la sous-classe redéfinit `MSG_PREFIX`, il est concaténé avec le préfixe parent (ligne 84).
- `$source` est un tableau `['pointer' => null, 'parameter' => null]` conforme à la spécification JSON:API (section `source`).
- Toutes les exceptions de l'API (BadRequest, Conflict, Forbidden, etc.) héritent de cette classe et se contentent de redéfinir les constantes.
