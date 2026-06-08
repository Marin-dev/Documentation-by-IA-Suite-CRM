# 📁 Config

**Chemin :** `Api/V8/Config/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe la configuration complète de l'API V8 SuiteCRM : définition des routes HTTP (contrat API), et configuration du conteneur DI (services, contrôleurs, middlewares OAuth2, paramètres, helpers).

## ⚙️ Responsabilité technique
Deux fichiers d'agrégation (`routes.php`, `services.php`) et un sous-dossier `services/` contenant 9 fichiers de définitions partielles. `routes.php` enregistre tous les endpoints REST sur l'app Slim. `services.php` agrège les 9 fichiers partiels en un tableau DI complet.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `services/` | 9 fichiers de configuration DI partielle (contrôleurs, services, factories, helpers, OAuth2, params, validators, globals) | [→ CONTEXT](services/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `routes.php` | Déclaration de toutes les routes HTTP de l'API V8 avec middlewares OAuth2 et validation des paramètres | [→ fiche](routes.php.doc.md) |
| `services.php` | Agrégateur du conteneur DI V8 — fusionne les 9 sous-fichiers et déclare `BeanManager` et `foundHandler` | [→ fiche](services.php.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\Core\Loader\CustomLoader` (surcharges), `Api\V8\*` (tous les composants V8), `league/oauth2-server`
- **Expose :** `services.php` chargé par `ContainerLoader` ; `routes.php` chargé par `RouteLoader` (tous deux depuis `Api/Core/`)
- **Flux typique :** démarrage → `ContainerLoader` charge `services.php` → conteneur DI peuplé ; puis `RouteLoader` charge `routes.php` → routes enregistrées sur Slim → application prête.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Trouver tous les endpoints de l'API V8 | [`routes.php`](routes.php.doc.md) |
| Comprendre la structure du conteneur DI | [`services.php`](services.php.doc.md) |
| Comprendre la configuration OAuth2 | [`services/middlewares.php`](services/middlewares.php.doc.md) |
| Ajouter un nouveau service au DI | [`services/services.php`](services/services.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `services.php` : `DBManager::class` référencé sans import explicite — attendu globalement dans l'environnement PHP SuiteCRM.
- Appel depuis un `entryPoint.php` probablement dans `Api/` non documenté — INCONNU.
