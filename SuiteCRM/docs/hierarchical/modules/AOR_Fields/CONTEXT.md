# 📁 AOR_Fields

**Chemin :** `modules/AOR_Fields/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOR_Fields gère les colonnes (champs) des rapports AOR. Chaque champ définit une colonne de résultat avec son label, sa fonction d'agrégation (COUNT, SUM, AVG), son tri, son groupement et son format d'affichage.

## ⚙️ Responsabilité technique
Bean `AOR_Field` (hérite de `Basic`). `save_lines()` parse le POST et valide les fonctions SQL et directions de tri contre des listes autorisées. Gère le `group_display` (niveaux de groupement hiérarchique). Serialisation du `module_path` en `base64(serialize(...))`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises du module | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOR_Field.php` | Bean champ/colonne d'un rapport | [→ fiche](AOR_Field.doc.md) |
| `fieldLines.php` | Helper d'affichage des lignes de champs dans EditView | [→ fiche](fieldLines.doc.md) |
| `vardefs.php` | Schéma de la table `aor_fields` | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `AOR_Report::save()` (via `save_lines`), `build_report_query_select()`, `build_report_html()`
- **Flux typique :** Sauvegarde rapport → `AOR_Field::save_lines($post, $report)` → création des colonnes → `build_report_query_select()` génère la clause SELECT

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle d'un champ de rapport | [`AOR_Field.php`](AOR_Field.doc.md) |

---

## ⚠️ Zones INCONNU
- `fieldLines.php` : contenu exact non lu
