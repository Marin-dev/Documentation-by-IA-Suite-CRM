# 📁 UpgradeWizard

**Chemin :** `modules/UpgradeWizard/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module orchestre le **processus de mise à jour (upgrade) de SuiteCRM**. Il gère le cycle complet : upload du package, vérifications pré-vol (preflight), traitement (commit), fusion des vues personnalisées, suppression du cache et finalisation. Il supporte aussi le mode **silent upgrade** (sans interface) via des scripts dédiés. Un service de vérification d'expiration de mot de passe (`PasswordExpirationService`) y est également inclus.

## ⚙️ Responsabilité technique
Architecture multi-fichiers avec séparation claire des étapes : `upload.php`, `preflight.php`, `commit.php`, `end.php`. Le sous-dossier `SugarMerge/` contient la logique de fusion des vues (Edit, Detail, List, Search, QuickCreate, Subpanel) lors de l'upgrade — chaque classe de merge hérite de `SugarMerge`. Des scripts JSON (`preflightJson.php`, `commitJson.php`, `systemCheckJson.php`) supportent les appels AJAX. `uw_utils.php` fournit les utilitaires de gestion de versions et chemins. `uw_ajax.php` gère les requêtes AJAX. `silentUpgrade.php` et ses variantes DCE permettent l'upgrade sans interface.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `SugarMerge/` | Fusion des vues personnalisées (Edit, Detail, List, Search, QuickCreate, Subpanel) lors de l'upgrade | — |
| `language/` | Libellés i18n (en_us) | — |
| `tpls/` | Template Smarty pour la fusion des layouts | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SugarMerge/SugarMerge.php` | Orchestrateur de la fusion des vues personnalisées pour un module donné | — |
| `uw_utils.php` | Utilitaires de gestion de version, chemins et helpers upgrade | — |
| `silentUpgrade.php` | Mode upgrade sans interface (CLI/cron) | — |
| `commit.php` | Étape de commit : application effective de l'upgrade | — |
| `preflight.php` | Vérifications pré-upgrade (compatibilité, espace disque, etc.) | — |
| `PasswordExpirationService.php` | Service de vérification d'expiration des mots de passe (lié au post-upgrade) | — |
| `UpgradeRemoval.php` | Suppression des artefacts post-upgrade | — |
| `UploadFileCheck.php` | Vérification du fichier d'upgrade uploadé | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard |
| `index.php` | Point d'entrée standard |
| `start.php` / `end.php` | Scripts d'initialisation/finalisation standards |
| `cancel.php` | Annulation standard |
| `layouts.php` / `deleteCache.php` | Utilitaires d'upgrade secondaires |
| `upgradeMetaHelper.php` / `upgradeTimeCounter.php` | Helpers techniques |
| `uw_emptyFunctions.php` / `uw_files.php` | Fonctions vides/liste de fichiers |
| `upgradeWizard.js` / `processing.gif` | Assets front-end |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `include/dir_inc.php` ; `ModuleBuilder/parsers/views/History.php` ; le package d'upgrade uploadé via `upload/`.
- **Expose :** Interface d'upgrade accessible via le menu Admin ; mode silent upgrade utilisable en CLI.
- **Flux typique :** Admin uploade le package → `preflight.php` vérifie la compatibilité → `commit.php` applique l'upgrade et appelle `SugarMerge` pour fusionner les vues → `deleteCache.php` vide le cache → `end.php` finalise.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la fusion des vues lors d'un upgrade | `SugarMerge/SugarMerge.php` |
| Lancer un upgrade sans interface | `silentUpgrade.php` |
| Comprendre les utilitaires de gestion de version | `uw_utils.php` |
| Diagnostiquer un échec preflight | `preflight.php` + `preflightJson.php` |
| Comprendre la fusion des vues Edit/Detail | `SugarMerge/EditViewMerge.php` + `DetailViewMerge.php` |

---

## ⚠️ Zones INCONNU
- Le contenu exact des vérifications dans `preflight.php` (liste des checks) nécessite lecture complète.
- La relation entre `silentUpgrade_dce_step1.php` et la variante DCE n'est pas documentée.
