# 📁 DynamicFields

**Chemin :** `modules/DynamicFields/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module DynamicFields gère le système de champs personnalisés de SuiteCRM. Il permet aux administrateurs de créer, modifier et déployer des champs supplémentaires sur n'importe quel module via Studio. Supporte une trentaine de types de champs (texte, date, enum, devise, HTML, relation, etc.).

## ⚙️ Responsabilité technique
Classe centrale `DynamicField` avec classes template pour chaque type de champ (`TemplateField` et sous-classes). Gestion des vardefs dynamiques, génération SQL et mise à jour des vues. `FieldViewer` pour le rendu. `FieldsMetaData` pour les métadonnées.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `templates/` | Templates champs et vues dynamiques | [→ CONTEXT](templates/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `DynamicField.php` | Classe centrale de gestion des champs dynamiques | [→ fiche](DynamicField.php.doc.md) |
| `FieldCases.php` | Gestion des cas/types de champs | [→ fiche](FieldCases.php.doc.md) |
| `FieldViewer.php` | Rendu des champs dynamiques | [→ fiche](FieldViewer.php.doc.md) |
| `FieldsMetaData.php` | Métadonnées des champs | [→ fiche](FieldsMetaData.php.doc.md) |
| `Save.php` | Sauvegarde d'un champ dynamique | [→ fiche](Save.php.doc.md) |
| `UpgradeFields.php` | Mise à niveau des champs | [→ fiche](UpgradeFields.php.doc.md) |
| `vardefs.php` | Schéma de la table des champs | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `VardefManager`, `SugarBean`, structure `fields_meta_data`
- **Consommé par :** Studio, ModuleBuilder (création de champs personnalisés)
- **Flux typique :** Admin crée champ dans Studio → `DynamicField::save()` → vardef généré → table modifiée via `repairDatabase`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la création d'un champ dynamique | [`DynamicField.php`](DynamicField.php.doc.md) |
| Voir les templates de types de champs | [`templates/Fields/`](templates/Fields/CONTEXT.md) |

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
