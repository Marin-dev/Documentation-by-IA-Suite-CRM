# 📁 Relationships

**Chemin :** `modules/Relationships/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module gère la définition et la manipulation des relations entre modules dans SuiteCRM. Il stocke les métadonnées de relation (table `relationships`) décrivant le lien entre un module gauche (`lhs_module`) et un module droit (`rhs_module`) avec leurs clés et types de jointure. Il est utilisé par Studio/ModuleBuilder pour créer des relations personnalisées.

## ⚙️ Responsabilité technique
La classe `Relationship` étend `SugarBean` et mappe la table `relationships`. `RelationshipHandler` étend `Relationship` et orchestre les opérations de relation (base_bean, rel1, rel2) avec références directes aux vardefs. La vue `view.editfields.php` et le template `editFields.tpl` permettent l'édition des champs de la relation. `field_arrays.php` définit les tableaux de colonnes DB.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Libellés i18n (en_us) | — |
| `views/` | Vue d'édition des champs de relation | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Relationship.php` | Entité SugarBean mappant la table `relationships` (métadonnées de relation inter-modules) | — |
| `RelationshipHandler.php` | Orchestrateur des opérations de relation (3 modules : base, rel1, rel2) | — |
| `vardefs.php` | Définition des champs de l'entité Relationship | — |
| `field_arrays.php` | Tableaux de colonnes DB utilisés pour les requêtes | — |
| `action_view_map.php` | Mapping action → vue | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `editFields.tpl` | Template Smarty de formulaire d'édition, trivial |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `include/SugarObjects/` et `ModuleBuilder/` pour la création/modification de relations ; `data/SugarBean.php` comme classe parente.
- **Expose :** Métadonnées de relation consommées par les sous-panneaux, les requêtes relationnelles et Studio.
- **Flux typique :** Studio crée une relation → enregistrement dans la table `relationships` via `Relationship::save()` → les modules concernés chargent leurs vardefs en tenant compte de cette entrée.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la structure d'une relation (lhs/rhs) | `Relationship.php` |
| Gérer une opération de relation impliquant 3 modules | `RelationshipHandler.php` |
| Consulter la structure DB de la table relationships | `vardefs.php` |
| Modifier le formulaire d'édition de champs de relation | `views/view.editfields.php` |

---

## ⚠️ Zones INCONNU
- La logique complète de `RelationshipHandler` (méthodes sur rel1/rel2/base) n'est pas entièrement documentée — investigation au-delà des lignes 60+ nécessaire.
