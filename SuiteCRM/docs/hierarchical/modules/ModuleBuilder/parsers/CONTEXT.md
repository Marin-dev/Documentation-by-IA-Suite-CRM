# 📁 parsers

**Chemin :** `modules/ModuleBuilder/parsers/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les parseurs pour la modification des layouts, champs, relations et listes déroulantes dans Studio et Module Builder. Architecture parser/implementation séparant logique et accès aux fichiers.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `relationships/` | Parseurs de relations (1:N, N:N, etc.) | [→ CONTEXT](relationships/CONTEXT.md) |
| `views/` | Parseurs de vues/layouts | [→ CONTEXT](views/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `constants.php` | Constantes du Module Builder | [→ fiche](constants.doc.md) |
| `ParserFactory.php` | Factory des parseurs | [→ fiche](ParserFactory.doc.md) |
| `ModuleBuilderParser.php` | Parseur de base du Module Builder | [→ fiche](ModuleBuilderParser.doc.md) |
| `StandardField.php` | Gestion des champs standards | [→ fiche](StandardField.doc.md) |
| `parser.dropdown.php` | Parseur des listes déroulantes | [→ fiche](parser.dropdown.doc.md) |
| `parser.label.php` | Parseur des libellés | [→ fiche](parser.label.doc.md) |
| `parser.modifylayoutview.php` | Parseur de modification de layout | [→ fiche](parser.modifylayoutview.doc.md) |
| `parser.modifylistview.php` | Parseur de modification de vue liste | [→ fiche](parser.modifylistview.doc.md) |
| `parser.modifysubpanel.php` | Parseur de modification de sous-panneau | [→ fiche](parser.modifysubpanel.doc.md) |
| `parser.searchfields.php` | Parseur des champs de recherche | [→ fiche](parser.searchfields.doc.md) |

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
