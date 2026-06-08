# 📁 Relationships

**Chemin :** `data/Relationships/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier implémente le système de gestion des relations entre modules SuiteCRM. Il fournit la hiérarchie complète des types de relations (M2M, One2Many, One2One, EmailAddress), la factory singleton de création des objets de relation, et la classe abstraite de base définissant le contrat commun. C'est la couche ORM des relations, utilisée par `Link2` et `SugarBean`.

## ⚙️ Responsabilité technique
Architecture en héritage : `SugarRelationship` (abstract, contrat + constantes) → `M2MRelationship` (table de jointure) → `One2MRelationship` (clé étrangère en table) → `One2MBeanRelationship` (clé étrangère directe dans le bean) → `One2OneBeanRelationship`. Parallèlement, `One2OneRelationship` hérite de `One2MRelationship` pour le cas 1:1 table-based, et `EmailAddressRelationship` hérite de `M2MRelationship` pour le cas spécialisé email. `SugarRelationshipFactory` est un singleton qui instancie le bon type selon les métadonnées de `TableDictionary`.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SugarRelationship.php` | Classe abstraite de base : contrat + constantes REL_LHS/RHS/MANY_MANY/ONE_MANY/ONE_ONE | [→ fiche](SugarRelationship.doc.md) |
| `RelationshipFactory.php` | Factory singleton : instancie le bon type de relation selon TableDictionary | [→ fiche](RelationshipFactory.doc.md) |
| `M2MRelationship.php` | Relation many-to-many via table de jointure | [→ fiche](M2MRelationship.doc.md) |
| `One2MRelationship.php` | Relation one-to-many via clé étrangère en table | [→ fiche](One2MRelationship.doc.md) |
| `One2MBeanRelationship.php` | Relation one-to-many via clé étrangère directe dans le bean | [→ fiche](One2MBeanRelationship.doc.md) |
| `One2OneBeanRelationship.php` | Relation one-to-one via clé étrangère directe dans le bean | [→ fiche](One2OneBeanRelationship.doc.md) |
| `One2OneRelationship.php` | Relation one-to-one via table de liaison | [→ fiche](One2OneRelationship.doc.md) |
| `EmailAddressRelationship.php` | Relation M2M spécialisée pour les adresses email (email_addr_bean_rel) | [→ fiche](EmailAddressRelationship.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `modules/TableDictionary.php` (métadonnées de relations), `data/BeanFactory.php`
- **Expose :** `SugarRelationshipFactory` utilisé par `data/Link2.php` ; `SugarRelationship` et ses sous-classes utilisés par `SugarBean`
- **Flux typique :** `SugarBean::load_relationship('contacts')` → `Link2` → `SugarRelationshipFactory::getRelationship()` → instancie `M2MRelationship` (ou autre type) → `add()` / `getBeans()` / `remove()`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le contrat de base des relations | [`SugarRelationship.php`](SugarRelationship.doc.md) |
| Savoir comment une relation est instanciée | [`RelationshipFactory.php`](RelationshipFactory.doc.md) |
| Comprendre les relations many-to-many (accounts_contacts, etc.) | [`M2MRelationship.php`](M2MRelationship.doc.md) |
| Comprendre la relation spéciale email | [`EmailAddressRelationship.php`](EmailAddressRelationship.doc.md) |

---

## ⚠️ Zones INCONNU
- Méthodes complètes de chaque classe de relation : non lues (fichiers non lus en entier)
- Comportement exact de `add()`, `remove()`, `getBeans()` dans chaque sous-classe : INCONNU
