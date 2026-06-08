# 📁 modules

**Chemin :** `custom/modules/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Dossier contenant les personnalisations spécifiques aux modules SuiteCRM dans le répertoire `custom/`. Le seul fichier documenté configure la visibilité des modules dans la recherche unifiée (barre de recherche globale). Ce fichier surcharge la configuration par défaut du core.

## ⚙️ Responsabilité technique
Fichiers PHP de configuration de surcharge : placés dans `custom/modules/`, ils ont priorité sur les fichiers équivalents dans `modules/`. Générés par l'interface d'administration SuiteCRM (Studio, Search Settings). Ne pas modifier manuellement.

---

## 📂 Contenu

### Sous-dossiers
_(aucun sous-dossier documenté)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `unified_search_modules_display.php` | Contrôle la visibilité des modules dans la recherche globale | [→ fiche](unified_search_modules_display.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** moteur de recherche unifiée SuiteCRM
- **Expose :** `$unified_search_modules_display` — configuration de visibilité des modules dans la barre de recherche globale
- **Flux typique :** requête de recherche globale → chargement de `custom/modules/unified_search_modules_display.php` (surcharge) → filtre les modules visibles

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Modifier quels modules apparaissent dans la recherche globale | [`unified_search_modules_display.php`](unified_search_modules_display.php.doc.md) |

---

## ⚠️ Zones INCONNU
- Autres personnalisations de modules potentiellement présentes dans des sous-dossiers `custom/modules/{NomModule}/` non documentées
