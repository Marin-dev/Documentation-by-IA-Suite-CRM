# 📁 Core

**Chemin :** `Api/Core/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient le noyau de bootstrap de l'API SuiteCRM. Il orchestre le démarrage de l'application : initialisation de l'environnement HTTP, chargement du framework Slim, configuration du conteneur DI et enregistrement des routes. Il fournit aussi les mécanismes de surcharge custom et de résolution des fichiers de configuration.

## ⚙️ Responsabilité technique
Point d'entrée `app.php` (script de bootstrap séquentiel), trois sous-dossiers fonctionnels : `Config/` (paramètres statiques), `Loader/` (initialisation du conteneur et des routes), `Resolver/` (accès aux fichiers de config). L'ensemble est framework-agnostique vis-à-vis de la logique métier — il ne contient que l'infrastructure de démarrage.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Config/` | Registre statique de configuration (chemins, settings Slim, clés OAuth2) | [→ CONTEXT](Config/CONTEXT.md) |
| `Loader/` | Bootstrap : initialisation du conteneur DI Slim, enregistrement des routes, mécanisme de surcharge custom | [→ CONTEXT](Loader/CONTEXT.md) |
| `Resolver/` | Utilitaire de résolution et chargement des fichiers de configuration PHP | [→ CONTEXT](Resolver/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `app.php` | Script de bootstrap : CORS, bootstrap SuiteCRM, instanciation Slim, chargement DI et routes | [→ fiche](app.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `include/entryPoint.php` (bootstrap SuiteCRM), `Slim\App`, `Api\V8\Config\*` (via `ApiConfig`)
- **Expose :** `app.php` est le point d'entrée inclus par le front controller HTTP de l'API ; fournit l'instance `$app` Slim configurée
- **Flux typique :** front controller HTTP → `app.php` → `ContainerLoader::configure()` → conteneur Slim → `RouteLoader::configureRoutes($app)` → application Slim prête à traiter les requêtes.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la séquence de démarrage de l'API | [`app.php`](app.doc.md) |
| Comprendre les paramètres de configuration du core | [`Config/ApiConfig.php`](Config/ApiConfig.doc.md) |
| Comprendre comment ajouter une config custom | [`Loader/CustomLoader.php`](Loader/CustomLoader.doc.md) |

---

## ⚠️ Zones INCONNU
- `app.php` : CORS `*` codé en dur avec commentaire "should remove" — vestige non nettoyé.
- Front controller HTTP (`index.php`) qui inclut `app.php` — non documenté/localisé (INCONNU).
