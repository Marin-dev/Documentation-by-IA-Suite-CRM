# 📁 jssource

**Chemin :** `jssource/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier implémente le pipeline de build JavaScript de SuiteCRM. Il fournit la carte de regroupement des fichiers JS (`JSGroupings.php`), le minificateur (`SugarMin.php` + `JShrink`), les utilitaires de concatenation/compression/sauvegarde (`minify_utils.php`), et le script de déclenchement (`minify.php`). Son rôle est d'optimiser les performances front-end en produisant des bundles JS concatenés et minifiés dans le cache.

## ⚙️ Responsabilité technique
Pipeline en trois étapes : (1) `JSGroupings.php` définit les groupes source→destination, (2) `minify_utils.php` fournit les fonctions de concatenation (`ConcatenateFiles`) et compression (`CompressFiles` via `SugarMin`), (3) `minify.php` orchestre le tout en CLI ou HTTP. `SugarMin` délègue à la bibliothèque Composer `JShrink\Minifier`.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `JSGroupings.php` | Carte source→destination des bundles JS (12 groupes : jQuery, YUI, SugarFields...) | [→ fiche](JSGroupings.doc.md) |
| `SugarMin.php` | Adaptateur sur JShrink\Minifier pour la minification JS | [→ fiche](SugarMin.doc.md) |
| `minify.php` | Point d'entrée CLI+HTTP du pipeline de build JS | [→ fiche](minify.doc.md) |
| `minify_utils.php` | Fonctions : ConcatenateFiles, CompressFiles, reverseScripts, BackUpAndCompress | [→ fiche](minify_utils.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `src_files/` | Répertoire des sources JS non minifiées — non documenté (fichiers statiques) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `JShrink\Minifier` (Composer), `include/utils/sugar_file_utils.php`, `custom/application/Ext/JSGroupings/jsgroups.ext.php` (extensions)
- **Expose :** bundles JS concatenés dans `cache/` — consommés par les templates de vues SuiteCRM
- **Flux typique :** admin lance rebuild JS → `minify.php` → `BackUpAndCompressScriptFiles()` (backup + minification) + `ConcatenateFiles()` (assemblage bundles) → fichiers JS optimisés en cache

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir quels fichiers JS sont regroupés ensemble | [`JSGroupings.php`](JSGroupings.doc.md) |
| Comprendre comment un fichier JS est minifié | [`SugarMin.php`](SugarMin.doc.md) et [`minify_utils.php`](minify_utils.doc.md) |
| Lancer ou comprendre le pipeline de build JS | [`minify.php`](minify.doc.md) |
| Ajouter un groupe JS personnalisé | [`JSGroupings.php`](JSGroupings.doc.md) via `custom/application/Ext/JSGroupings/jsgroups.ext.php` |

---

## ⚠️ Zones INCONNU
- Point d'entrée admin HTTP exact pour déclencher la reconstruction JS : INCONNU
- Paramètre `$compression` de `SugarMin::minify()` : accepté mais non transmis à JShrink — compression fixe
- Contenu de `src_files/` : sources JS non minifiées, non documentées
