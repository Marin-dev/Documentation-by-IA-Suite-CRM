# ExternalAPIBase.php

**Chemin :** `include/externalAPI/Base/ExternalAPIBase.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Classe de base abstraite pour toutes les implementations d'APIs externes dans SuiteCRM (Google Drive, WebEx, GoToMeeting, etc.). Fournit le mecanisme d'authentification EAPM (External Accounts & Password Manager) et les methodes communes a toutes les integrations externes.

## Role technique

Classe abstraite implementant `ExternalAPIPlugin`. Gere le chargement des credentials utilisateur depuis un bean EAPM (`loadEAPM()`). Supporte plusieurs methodes d'authentification (`password`, `oauth`, `oauth2`). Methodes etendues dans les sous-classes specifiques a chaque service.

---

## Dependances cles

- **Imports principaux :**
  - `ExternalAPIPlugin` (`include/externalAPI/Base/ExternalAPIPlugin.php`) — interface
  - `ExternalOAuthAPIPlugin` (`include/externalAPI/Base/ExternalOAuthAPIPlugin.php`) — plugin OAuth
  - `SourceFactory` — acces aux connecteurs
  - `EAPM` (module) — bean de credentials utilisateur

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `ExternalAPIBase` | classe abstraite | Base des APIs externes |
| `$useAuth` | propriete | Requiert une authentification |
| `$requireAuth` | propriete | Authentification obligatoire |
| `$authMethod` | propriete | Methode : `password`, `oauth`, `oauth2` |
| `loadEAPM(EAPM): void` | methode | Charge les credentials depuis EAPM |
| `APP_STRING_ERROR_PREFIX` | constante | Prefixe pour les messages d'erreur |

- **Consommateurs identifies :** toutes les classes `ExtAPI{Name}` dans `include/externalAPI/`

## Relations cles

- **Appele par :** `ExternalAPIFactory::loadAPI()`
- **Appelle :** `EAPM` (chargement credentials), sous-classes (implementation specifique)
- **Position dans le flux global :** base de l'ecosysteme d'integrations API externes

---

## Points d'attention

- Commentaire `FIXME` ligne 75 : le bean EAPM n'est pas valide si non authentifie — le code continue sans erreur explicite.
- Methodes specifiques (appel d'API, gestion d'erreurs) sont dans les sous-classes et non visibles ici.
