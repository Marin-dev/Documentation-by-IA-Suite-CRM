# 📁 ModuleBuilder

**Chemin :** `modules/ModuleBuilder/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module ModuleBuilder est l'outil de personnalisation avancée de SuiteCRM. Il regroupe Studio (modification des modules déployés) et le Module Builder (création de nouveaux modules packagés). Permet de créer/modifier des champs, layouts, relations, labels et listes déroulantes.

## ⚙️ Responsabilité technique
Architecture parseur/implémentation séparant logique et accès fichiers. Deux sous-systèmes : `MB/` (Module Builder packages) et `Module/` (Studio déployé). Parseurs spécialisés par action (layout, liste, relation, dropdown). Interface AJAX avec arborescence navigable.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `MB/` | Classes du Module Builder (packages non déployés) | [→ CONTEXT](MB/CONTEXT.md) |
| `Module/` | Classes Studio (modules déployés) | [→ CONTEXT](Module/CONTEXT.md) |
| `parsers/` | Parseurs de layouts, relations, champs | [→ CONTEXT](parsers/CONTEXT.md) |
| `views/` | Vues de l'interface Studio/MB | [→ CONTEXT](views/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `controller.php` | Contrôleur principal | [→ fiche](controller.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |
| `action_view_map.php` | Mapping actions → vues | [→ fiche](action_view_map.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `DynamicFields`, `VardefManager`, système de fichiers `custom/`
- **Consommé par :** Interface d'administration (outil de personnalisation)
- **Flux typique :** Admin modifie layout dans Studio → parseur génère fichier dans `custom/Extension/` → `repair/rebuild` applique les changements

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre Studio (modules déployés) | [`Module/StudioModule.php`](Module/CONTEXT.md) |
| Comprendre le Module Builder (packages) | [`MB/ModuleBuilder.php`](MB/CONTEXT.md) |
| Voir les parseurs de layouts | [`parsers/views/`](parsers/views/CONTEXT.md) |
| Voir les parseurs de relations | [`parsers/relationships/`](parsers/relationships/CONTEXT.md) |

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
