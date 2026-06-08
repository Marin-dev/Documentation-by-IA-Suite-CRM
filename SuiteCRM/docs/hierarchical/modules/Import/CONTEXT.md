# 📁 Import

**Chemin :** `modules/Import/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Import fournit un assistant multi-étapes pour l'importation de données externes dans SuiteCRM. Il prend en charge plusieurs formats (CSV, vCard Outlook, Google, Salesforce, etc.) et couvre toutes les étapes du processus : sélection du fichier, mapping des colonnes, vérification des doublons, confirmation et annulation d'import. Il gère également l'import depuis des sources externes via des adaptateurs EAPM.

## ⚙️ Responsabilité technique
`ImportController` (étend `SugarController`) orchestre le workflow en 4 étapes via des vues dédiées (`view.step1` à `view.step4`). La classe `Importer` effectue l'import effectif avec `ImportFieldSanitize` pour la validation, `ImportDuplicateCheck` pour la détection de doublons, et `ImportCacheFiles` pour la gestion des fichiers temporaires. Les `ImportMap*` fournissent des mappings prédéfinis pour différents formats sources. `ImportFileSplitter` gère le découpage des gros fichiers.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `maps/` | Mappings prédéfinis pour formats sources (CSV, Outlook, Google, Salesforce, Tab) | Pas de CONTEXT.md |
| `sources/` | Sources de données importables (fichier, EAPM externe) | Pas de CONTEXT.md |
| `tpls/` | Templates Smarty des étapes de l'assistant d'import | Pas de CONTEXT.md |
| `views/` | Vues MVC de chaque étape (step1 à step4, dupcheck, confirm, undo, error) | Pas de CONTEXT.md |
| `language/` | Fichiers de traduction | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `controller.php` | Contrôleur orchestrant le workflow d'import en étapes | Pas de fiche |
| `Importer.php` | Classe d'import effectif avec sanitisation et gestion des doublons | Pas de fiche |
| `ImportFieldSanitize.php` | Validation et nettoyage des champs importés | Pas de fiche |
| `ImportDuplicateCheck.php` | Détection et gestion des doublons lors de l'import | Pas de fiche |
| `ImportCacheFiles.php` | Gestion des fichiers cache temporaires d'import | Pas de fiche |
| `ImportFileSplitter.php` | Découpage des gros fichiers d'import | Pas de fiche |
| `CsvAutoDetect.php` | Détection automatique du délimiteur et de l'encodage CSV | Pas de fiche |
| `UsersLastImport.php` | Suivi du dernier import par utilisateur | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard du module |
| `Forms.php` | Helpers de formulaires standard |
| `vardefs.php` | Définition des champs standard SugarCRM |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `include/MVC/Controller/SugarController.php`, `BeanFactory` (chargement du bean cible), `ACLController` (vérification des droits d'import), sources EAPM (`ExternalSourceEAPMAdapter`).
- **Expose :** Interface utilisateur d'import multi-étapes accessible via `index.php?module=Import`. Classe `Importer` utilisable programmatiquement.
- **Flux typique :** Utilisateur sélectionne module cible (Step1) → upload fichier et mapping (Step2/Confirm) → import effectif avec gestion doublons (Step3/DupCheck) → résultat et historique (Step4/Last) → possibilité d'annulation (Undo).

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le workflow d'import | [`controller.php`](controller.php) |
| Modifier la logique d'import effectif | [`Importer.php`](Importer.php) |
| Ajouter un format de mapping source | [`maps/ImportMap.php`](maps/ImportMap.php) |
| Modifier la détection de doublons | [`ImportDuplicateCheck.php`](ImportDuplicateCheck.php) |
| Comprendre la validation des champs | [`ImportFieldSanitize.php`](ImportFieldSanitize.php) |

---

## ⚠️ Zones INCONNU
- Mécanisme exact d'annulation d'import (Undo) : logique de rollback non vérifiée.
- Comportement précis du mode `ExtStep1` / `Extdupcheck` / `Extimport` (sources externes EAPM) : INCONNU sans lecture de `ExternalSourceEAPMAdapter`.
