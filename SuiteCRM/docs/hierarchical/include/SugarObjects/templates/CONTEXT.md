# 📁 templates

**Chemin :** `include/SugarObjects/templates/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les templates SugarObject — classes intermédiaires dans la hiérarchie des beans SuiteCRM. Ils spécialisent `SugarBean` par type fonctionnel : `Basic` pour les modules génériques, `Person` pour les personnes physiques. Ces templates sont utilisés comme classe parente dans les modules SuiteCRM.

## ⚙️ Responsabilité technique
Hiérarchie d'héritage : `SugarBean` → `Basic` → `Person` (et autres templates non documentés : Company, Sale, Issue, File). Chaque template ajoute uniquement les propriétés et comportements spécifiques à son type.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `basic/` | Template de base pour les beans sans spécialisation | [→ CONTEXT](basic/CONTEXT.md) |
| `person/` | Template pour les personnes physiques (Contact, Lead) avec champs RGPD | [→ CONTEXT](person/CONTEXT.md) |

### Fichiers documentés
Aucun fichier directement dans `templates/`.

### Fichiers non documentés (volontairement)
| Fichier/Dossier | Raison |
|---|---|
| `company/`, `sale/`, `issue/`, `file/` | Autres templates — hors périmètre de cette vague |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean` (héritage)
- **Expose :** `Basic` et `Person` — hérités par les beans de tous les modules SuiteCRM
- **Flux typique :** Chaque module SuiteCRM (ex: `Contact extends Person`, `Account extends Basic`) hérite d'un de ces templates.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la classe parente des modules génériques | [`basic/Basic.php`](basic/Basic.doc.md) |
| Comprendre les champs communs des personnes (Contact, Lead) | [`person/Person.php`](person/Person.doc.md) |

---

## ⚠️ Zones INCONNU
- Templates `company/`, `sale/`, `issue/`, `file/` non documentés.
