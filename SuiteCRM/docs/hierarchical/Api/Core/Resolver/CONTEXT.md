# 📁 Resolver

**Chemin :** `Api/Core/Resolver/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient l'utilitaire de résolution et chargement des fichiers de configuration PHP de l'API. Il prend en charge la préfixation des chemins relatifs avec `BASE_DIR`, la vérification d'existence/lisibilité et la fusion des tableaux retournés.

## ⚙️ Responsabilité technique
Classe statique `ConfigResolver` avec deux méthodes : `loadFiles()` (charge et fusionne des fichiers PHP retournant des tableaux) et `isFileExist()` (garde-fou — lève `RuntimeException` si fichier absent ou illisible). Comportement fail-fast intentionnel.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ConfigResolver.php` | Résout et charge les fichiers de configuration PHP (chemins relatifs → absolus via `BASE_DIR`, vérification, fusion) | [→ fiche](ConfigResolver.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `$GLOBALS['BASE_DIR']` (défini par `include/entryPoint.php`)
- **Expose :** `loadFiles()` appelé par `ContainerLoader` ; `isFileExist()` appelé par `RouteLoader`
- **Flux typique :** `ContainerLoader` → `ConfigResolver::loadFiles(['Api/Core/Config/slim.php'])` → chemin préfixé avec `BASE_DIR` → vérifié → `require` → tableau fusionné retourné.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le chargement des fichiers de configuration | [`ConfigResolver.php`](ConfigResolver.doc.md) |

---

## ⚠️ Zones INCONNU
- Bug potentiel : vérification `is_array($config)` hors du bloc `if (self::isFileExist())` — variable potentiellement non définie.
- Fusion via `array_merge` (pas profonde) — clés dupliquées écrasées par le dernier fichier.
