# ExceptionCode.php

**Chemin :** `lib/Enumerator/ExceptionCode.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

---

## Role

Repertoire centralisé de tous les codes d'erreur numériques utilisés dans les exceptions de SuiteCRM. Fournit une référence unique pour identifier la catégorie et la nature de chaque erreur levée dans l'application et l'API.

## Responsabilités

- Définir des constantes entières uniques pour chaque type d'erreur métier ou technique.
- Respecter la convention de nommage `[Sous_Système]_[Nom_Erreur]` afin de regrouper les codes par domaine.
- Servir de contrat entre les couches Exception, Controller et les clients de l'API.

## Dépendances internes

Aucune (classe de constantes pure, sans import).

## Exports / Points d'entrée

| Constante | Valeur | Domaine |
|---|---|---|
| `APPLICATION_MALWARE_FOUND` | 4000 | Sécurité anti-malware |
| `APPLICATION_UNHANDLED_BEHAVIOUR` | 6000 | Erreur applicative générique |
| `APPLICTAION_MODULE_NOT_FOUND` | 6005 | Module introuvable (côté applicatif) |
| `API_EXCEPTION` | 8000 | Exception API générique |
| `API_CONTENT_NEGOTIATION_FAILED` | 8005 | Négociation de contenu échouée |
| `API_INVALID_BODY` | 8010 | Corps de requête invalide |
| `API_MODULE_NOT_FOUND` | 8015 | Module introuvable (côté API) |
| `API_MISSING_REQUIRED` | 8020 | Champ obligatoire absent |
| `API_DATE_CONVERTION_SUGARBEAN` | 8025 | Erreur de conversion de date |
| `API_USER_NOT_ACTIVE` | 8030 | Utilisateur inactif |
| `API_NOT_IMPLEMENTED` | 8035 | Fonctionnalité non implémentée |
| `API_RESERVED_KEYWORD_NOT_ALLOWED` | 8040 | Mot-clé réservé interdit |
| `API_RELATIONSHIP_NOT_FOUND` | 8045 | Relation introuvable |
| `API_RECORD_NOT_FOUND` | 8050 | Enregistrement introuvable |
| `API_VIEWDEF_NOT_FOUND` | 8055 | Définition de vue introuvable |
| `API_ID_ALREADY_EXISTS` | 8060 | ID déjà existant |

**Consommateurs identifiés dans le repo :**
- `lib/Exception/Exception.php`
- `lib/Exception/MalwareFoundException.php`
- `lib/Exception/NotAllowedException.php`
- `lib/Exception/NotFoundException.php`
- `lib/API/OAuth2/Exception/OAuth2.php`
- `lib/API/v8/Controller/ModuleController.php`
- `lib/API/OAuth2/Middleware/ResourceServer.php`

## Notes techniques

- La faute de frappe `APPLICTAION_MODULE_NOT_FOUND` (au lieu de `APPLICATION`) est présente dans le code source (ligne 54) — ne pas corriger sans vérifier les usages.
- Les codes API commencent tous à partir de 8000, permettant une ségrégation claire avec les codes applicatifs (4000, 6000).
