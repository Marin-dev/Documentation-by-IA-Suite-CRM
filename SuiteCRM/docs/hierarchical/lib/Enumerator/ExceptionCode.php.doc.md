# ExceptionCode.php

**Chemin :** `lib/Enumerator/ExceptionCode.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Enumerateur centralisant tous les codes d'erreur numeriques utilises dans les exceptions SuiteCRM. Joue le role de registre unique de codes pour eviter les collisions entre sous-systemes (Application, API, etc.).

## Role technique
Classe PHP sans instances (uniquement des constantes publiques `const`). Chaque constante suit la convention `[SOUS_SYSTEME]_[NOM_ERREUR] = integer_unique`. Couvre les erreurs applicatives (4000-6005) et les erreurs API (8000-8060).

---

## Dependances cles
- **Imports principaux :** aucun
- **Variables d'environnement :** aucune

## Exports / Symboles principaux
| Constante | Valeur | Description |
|---|---|---|
| `APPLICATION_MALWARE_FOUND` | 4000 | Malware detecte |
| `APPLICATION_UNHANDLED_BEHAVIOUR` | 6000 | Comportement non gere |
| `APPLICTAION_MODULE_NOT_FOUND` | 6005 | Module non trouve (typo dans le nom) |
| `API_EXCEPTION` | 8000 | Exception API generique |
| `API_CONTENT_NEGOTIATION_FAILED` | 8005 | Negociation de contenu echouee |
| `API_INVALID_BODY` | 8010 | Corps de requete invalide |
| `API_MODULE_NOT_FOUND` | 8015 | Module API non trouve |
| `API_MISSING_REQUIRED` | 8020 | Champ requis manquant |
| `API_DATE_CONVERTION_SUGARBEAN` | 8025 | Erreur conversion date |
| `API_USER_NOT_ACTIVE` | 8030 | Utilisateur inactif |
| `API_NOT_IMPLEMENTED` | 8035 | Non implemente |
| `API_RESERVED_KEYWORD_NOT_ALLOWED` | 8040 | Mot-cle reserve |
| `API_RELATIONSHIP_NOT_FOUND` | 8045 | Relation non trouvee |
| `API_RECORD_NOT_FOUND` | 8050 | Enregistrement non trouve |
| `API_VIEWDEF_NOT_FOUND` | 8055 | Viewdef non trouve |
| `API_ID_ALREADY_EXISTS` | 8060 | ID deja existant |

- **Consommateurs identifies :** `lib/Exception/Exception.php`, `lib/Exception/AccessDeniedException.php`, `lib/Exception/InvalidArgumentException.php`, `lib/Exception/MalwareFoundException.php`, `lib/Exception/NotAllowedException.php`, `lib/Exception/NotFoundException.php`

## Relations cles
- **Appele par :** toutes les classes d'exception de `lib/Exception/`
- **Appelle :** rien
- **Position dans le flux global :** reference statique passive utilisee a la construction de toute exception SuiteCRM

---

## Points d'attention
- Typo notoire : `APPLICTAION_MODULE_NOT_FOUND` (ligne 54) devrait etre `APPLICATION_MODULE_NOT_FOUND`.
- Les codes numeriques sont fixes en dur : toute addition doit s'assurer de l'unicite.
