# 📁 BeanDecorator

**Chemin :** `Api/V8/BeanDecorator/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier fournit la couche d'abstraction sur les beans SuiteCRM pour l'API V8. Il encapsule `BeanFactory`, standardise l'accès (avec exceptions typées), gère les aliases de modules et offre un pattern Fluent Builder pour les requêtes de liste.

## ⚙️ Responsabilité technique
Trois classes : `BeanManager` (service central injectable), `BeanListRequest` (builder fluent pour `SugarBean::get_list()`), `BeanListResponse` (DTO encapsulant le résultat). `BeanManager` est injecté dans pratiquement tous les services et middlewares de l'API V8.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `BeanManager.php` | Service central d'accès aux beans SuiteCRM : résolution, création, relations, comptage — avec exceptions typées | [→ fiche](BeanManager.php.doc.md) |
| `BeanListRequest.php` | Fluent builder pour construire et exécuter une requête de liste sur un SugarBean | [→ fiche](BeanListRequest.php.doc.md) |
| `BeanListResponse.php` | DTO encapsulant le résultat de `SugarBean::get_list()` (liste de beans + nombre de lignes) | [→ fiche](BeanListResponse.php.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `BeanFactory` (global SuiteCRM), `DBManager`, `Relationship`, `SugarBean`, `beanAliases` (table de mapping depuis `beanAliases.php`)
- **Expose :** `BeanManager` injecté dans tous les services, middlewares, repositories OAuth2 et options de paramètres ; `BeanListRequest`/`BeanListResponse` utilisés par `ModuleService`
- **Flux typique :** service appelle `$beanManager->newBeanSafe('Accounts')` → résolution de l'alias → `BeanFactory::newBean` → bean retourné ; ou `$beanManager->getList('Accounts')->where($sql)->fetch()` → `BeanListResponse` avec beans paginés.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'accès aux beans SuiteCRM dans l'API | [`BeanManager.php`](BeanManager.php.doc.md) |
| Comprendre la construction de requêtes de liste paginées | [`BeanListRequest.php`](BeanListRequest.php.doc.md) |
| Comprendre le résultat des requêtes de liste | [`BeanListResponse.php`](BeanListResponse.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `BeanManager::getLinkedFieldName` : comportement exact de `Relationship::retrieve_by_modules` non documenté — format de retour incertain.
- `BeanManager::countRecords` : requête SQL brute avec JOIN conditionnel sur table `_cstm` — logique non triviale.
