# 📁 data

**Chemin :** `data/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier constitue la couche ORM (Object-Relational Mapping) de SuiteCRM. Il fournit `SugarBean` (classe de base de tous les objets métier), `BeanFactory` (factory avec cache pour charger/créer les beans), et le système de gestion des relations entre beans (`Link`, `Link2`, et le sous-dossier `Relationships/`). Tout module SuiteCRM (Contacts, Accounts, Leads, etc.) hérite de `SugarBean` et utilise `BeanFactory` pour être chargé.

## ⚙️ Responsabilité technique
Deux patterns principaux : Factory (`BeanFactory` avec cache LRU de 10 entrées) et ORM (`SugarBean` avec CRUD, hooks, ACL, champs dynamiques). Les relations sont gérées via `Link2` (API moderne, délègue à `SugarRelationship`) et `Link` (API legacy). Le sous-dossier `Relationships/` contient la hiérarchie complète des types de relation.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Relationships/` | Hiérarchie des types de relation (M2M, One2M, One2One, Email) + factory | [→ CONTEXT](Relationships/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SugarBean.php` | Classe ORM de base de tous les beans SuiteCRM (CRUD, relations, hooks, ACL) | [→ fiche](SugarBean.doc.md) |
| `BeanFactory.php` | Factory statique avec cache LRU pour créer/charger les beans | [→ fiche](BeanFactory.doc.md) |
| `Link2.php` | Implémentation moderne des liens entre beans (délègue à SugarRelationship) | [→ fiche](Link2.doc.md) |
| `Link.php` | Implémentation legacy des liens entre beans (ancienne API) | [→ fiche](Link.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Link.php` | API legacy — documenté mais déprécié, préférer Link2 |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `modules/DynamicFields/DynamicField.php`, `modules/TableDictionary.php`, `DBManager`, `LogicHook`
- **Expose :** `BeanFactory` et `SugarBean` sont les composants les plus utilisés de tout SuiteCRM — dépendance de quasi tous les modules et de la couche `service/`
- **Flux typique :** appel API `get_entry($module, $id)` → `BeanFactory::getBean($module, $id)` → `SugarBean::retrieve($id)` → SQL via `DBManager` → bean hydraté retourné ; ou `SugarBean::load_relationship('contacts')` → `Link2` → `SugarRelationshipFactory` → `M2MRelationship`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment un bean est chargé | [`BeanFactory.php`](BeanFactory.doc.md) |
| Comprendre la classe de base de tous les modules | [`SugarBean.php`](SugarBean.doc.md) |
| Comprendre les relations entre beans | [`Link2.php`](Link2.doc.md) et [`Relationships/CONTEXT.md`](Relationships/CONTEXT.md) |
| Comprendre les types de relation (M2M, 1:N...) | [`Relationships/SugarRelationship.php`](Relationships/SugarRelationship.doc.md) |

---

## ⚠️ Zones INCONNU
- `SugarBean` : liste exhaustive des méthodes publiques (fichier très volumineux, non lu entièrement)
- `Link` (legacy) : méthodes complètes non lues
- Cache `BeanFactory` : `$touched` — usage exact inconnu
