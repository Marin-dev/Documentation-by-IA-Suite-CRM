# 📁 TemplateSectionLine

**Chemin :** `modules/TemplateSectionLine/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module représente une **ligne de section de template** utilisée dans les modules de génération de documents (PDF, devis, contrats). Chaque `TemplateSectionLine` stocke une ligne de contenu (avec miniature `thumbnail`) appartenant à une section de template. Il sert de brique élémentaire pour la construction de templates documentaires structurés.

## ⚙️ Responsabilité technique
La classe `TemplateSectionLine` étend `TemplateSectionLine_sugar` (pattern sugar/custom). La classe `_sugar` est la base générée. La table cible est `templatesectionline`. Le module dispose d'un CRUD complet (list, detail, edit, search, popup, quickcreate) défini dans `metadata/`. Pas de contrôleur custom ni de vue PHP dédiée.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Libellés i18n (en_us) | — |
| `metadata/` | Définitions des vues (list, detail, edit, search, subpanel) | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `TemplateSectionLine.php` | Entité principale (classe vide pour customisation) | — |
| `TemplateSectionLine_sugar.php` | Classe générée de base — ne pas modifier directement | — |
| `vardefs.php` | Définition des champs (dont `thumbnail`, `line_num`, `type`) | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `metadata/dashletviewdefs.php` | Définition dashlet standard |
| `metadata/metafiles.php` | Métafichiers standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Modules de template (AOS_PDF_Templates, AOS_Quotes, etc.) qui utilisent les lignes de section comme sous-entités.
- **Expose :** Entité `TemplateSectionLine` accessible via sous-panneau depuis les templates parents.
- **Flux typique :** Création d'un template document → ajout de sections → chaque section contient des `TemplateSectionLine` → rendu du document en PDF.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre les champs d'une ligne de section | `vardefs.php` |
| Modifier le comportement de sauvegarde | `TemplateSectionLine.php` (classe vide à compléter) |
| Adapter la vue de création | `metadata/editviewdefs.php` |

---

## ⚠️ Zones INCONNU
- La liste complète des champs définis dans `vardefs.php` (au-delà de `thumbnail`) nécessite lecture complète du fichier.
- Le module parent qui consomme `TemplateSectionLine` n'est pas confirmé depuis ce seul module.
