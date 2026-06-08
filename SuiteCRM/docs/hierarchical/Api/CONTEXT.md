# 📁 Api

**Chemin :** `Api/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient l'implémentation complète de l'API REST publique de SuiteCRM. Il expose les opérations CRUD sur tous les modules CRM, la gestion des relations inter-beans, l'authentification OAuth2, et les métadonnées de l'API. Toutes les réponses respectent la spec JSON:API.

## ⚙️ Responsabilité technique
Architecture à deux couches : `Core/` (bootstrap, configuration, loaders) et `V8/` (implémentation fonctionnelle de la version 8 de l'API). La couche `Core` orchestre le démarrage de l'application Slim 3 et charge la configuration de `V8`. La couche `V8` implémente le pattern MVC avec injection de dépendances via le conteneur Slim.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Core/` | Bootstrap de l'API : CORS, configuration Slim, conteneur DI, chargement des routes, surcharges custom | [→ CONTEXT](Core/CONTEXT.md) |
| `V8/` | Implémentation complète de l'API V8 : routes, contrôleurs, services, OAuth2, validation, sérialisation JSON:API | [→ CONTEXT](V8/CONTEXT.md) |

### Fichiers documentés
Aucun fichier direct dans ce dossier.

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `entryPoint.php` (probable) | Point d'entrée HTTP non documenté dans les fiches disponibles — INCONNU |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `include/entryPoint.php` (bootstrap SuiteCRM global), classes natives SuiteCRM (`BeanFactory`, `SugarBean`, `DBManager`, `ACLController`), `league/oauth2-server`, `Slim 3`, `Symfony\Component\Validator/OptionsResolver`
- **Expose :** endpoints HTTP REST JSON:API sur `/access_token`, `/V8/*` — consommés par les clients externes (frontends, intégrations tierces)
- **Flux typique :** client HTTP → front controller → `Api/Core/app.php` → `Api/V8/Config/routes.php` dispatch → contrôleur → service → `BeanManager` → réponse JSON:API.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Trouver tous les endpoints disponibles | [`V8/Config/routes.php`](V8/Config/routes.php.doc.md) |
| Comprendre le démarrage de l'API | [`Core/app.php`](Core/app.doc.md) |
| Comprendre l'authentification OAuth2 | [`V8/OAuth2/`](V8/OAuth2/CONTEXT.md) |
| Comprendre les opérations CRUD sur les modules | [`V8/Service/ModuleService.php`](V8/Service/ModuleService.php.doc.md) |
| Ajouter une route ou un service custom | [`Core/Loader/CustomLoader.php`](Core/Loader/CustomLoader.doc.md) |

---

## ⚠️ Zones INCONNU
- Front controller HTTP (probablement `index.php`) non documenté — INCONNU son emplacement exact.
- Scopes OAuth2 non implémentés (stub) — restriction des droits d'accès non opérationnelle.
- CORS permissif codé en dur (`*`) — risque de sécurité en production.
