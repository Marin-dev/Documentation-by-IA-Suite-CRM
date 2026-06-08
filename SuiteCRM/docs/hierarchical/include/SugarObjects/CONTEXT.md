# 📁 SugarObjects

**Chemin :** `include/SugarObjects/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les composants fondamentaux du framework SuiteCRM : la configuration globale, le registre partagé, le gestionnaire de vardefs (schéma de données), le gestionnaire de session, le gestionnaire de langue, et la hiérarchie des templates de beans. Ce sont des utilitaires bas niveau utilisés par l'ensemble de l'application.

## ⚙️ Responsabilité technique
Ensemble de classes statiques/singletons (`SugarConfig`, `SugarRegistry`, `VardefManager`, `LanguageManager`) et de classes d'héritage pour les beans (`templates/`). `VardefManager` est particulièrement central : il alimente le schéma de tous les modules via un système de cache deux niveaux.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `templates/` | Hiérarchie de templates SugarBean (Basic, Person, etc.) | [→ CONTEXT](templates/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SugarConfig.php` | Singleton d'accès unifié à `$GLOBALS['sugar_config']` avec cache | [→ fiche](SugarConfig.doc.md) |
| `SugarRegistry.php` | Registre global key-value par namespace pour le partage d'objets | [→ fiche](SugarRegistry.doc.md) |
| `VardefManager.php` | Gestionnaire des vardefs — chargement, cache et fusion du schéma de données | [→ fiche](VardefManager.doc.md) |
| `SugarSession.php` | Gestionnaire de session PHP pour SuiteCRM | [→ fiche](SugarSession.doc.md) |
| `LanguageManager.php` | Génération et cache des fichiers de langue des modules | [→ fiche](LanguageManager.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `$GLOBALS['sugar_config']`, `$_SESSION`, `DynamicField`, `BeanFactory`, `SugarBean`
- **Expose :** `SugarConfig::get()`, `VardefManager::loadVardef()`, `LanguageManager::createLanguageFile()` — consommés par toute l'application
- **Flux typique :** Au chargement d'un module, `VardefManager::loadVardef()` est appelé → charge le template via `LanguageManager::createLanguageFile()` → le bean utilise `SugarConfig::get()` pour lire la configuration.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Lire la configuration globale SuiteCRM | [`SugarConfig.php`](SugarConfig.doc.md) |
| Comprendre comment les vardefs sont chargés | [`VardefManager.php`](VardefManager.doc.md) |
| Comprendre la hiérarchie des beans modules | [`templates/`](templates/CONTEXT.md) |
| Comprendre le registre global partagé | [`SugarRegistry.php`](SugarRegistry.doc.md) |

---

## ⚠️ Zones INCONNU
- `SugarSession` : implémentation interne INCONNU — fiche incomplète.
- `LanguageManager` : méthodes internes (`loadTemplateLanguage`, `refreshLanguage`) INCONNU.
- `VardefManager::cleanVardefs()` : supprime silencieusement les champs mal formés — à surveiller.
- Templates non documentés : `company/`, `sale/`, `issue/`, `file/`.
