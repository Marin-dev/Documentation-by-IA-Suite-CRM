# 📁 metadata

**Chemin :** `modules/AOBH_BusinessHours/metadata/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient toutes les métadonnées de configuration des vues du module AOBH_BusinessHours : vues liste, détail, édition, recherche, popup, sous-panneaux et dashlet.

## ⚙️ Responsabilité technique
Fichiers PHP déclaratifs au format standard SuiteCRM. Aucune logique métier — configuration pure chargée par le moteur de vues. Les modifications doivent passer par Studio ou `custom/Extension/`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `subpanels/` | Configuration du sous-panneau par défaut | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SearchFields.php` | Champs de recherche basique et avancée | [→ fiche](SearchFields.doc.md) |
| `detailviewdefs.php` | Layout de la vue détail | [→ fiche](detailviewdefs.doc.md) |
| `editviewdefs.php` | Layout du formulaire d'édition | [→ fiche](editviewdefs.doc.md) |
| `listviewdefs.php` | Colonnes de la vue liste | [→ fiche](listviewdefs.doc.md) |
| `dashletviewdefs.php` | Configuration de la vue dashlet | [→ fiche](dashletviewdefs.doc.md) |
| `metafiles.php` | Liste des fichiers metadata à charger | [→ fiche](metafiles.doc.md) |
| `popupdefs.php` | Configuration du popup de sélection | [→ fiche](popupdefs.doc.md) |
| `quickcreatedefs.php` | Layout du formulaire de création rapide | [→ fiche](quickcreatedefs.doc.md) |
| `searchdefs.php` | Définition des filtres de recherche | [→ fiche](searchdefs.doc.md) |
| `subpanels/default.php` | Configuration du sous-panneau par défaut | [→ fiche](subpanels/default.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Framework de vues SuiteCRM
- **Expose :** Configuration des vues et sous-panneaux du module Business Hours
- **Flux typique :** Moteur de vues → charge les fichiers metadata → rendu des vues

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Modifier la vue liste Business Hours | [`listviewdefs.php`](listviewdefs.doc.md) |
| Modifier la vue détail/édition | [`detailviewdefs.php`](detailviewdefs.doc.md) / [`editviewdefs.php`](editviewdefs.doc.md) |
| Configurer la recherche | [`searchdefs.php`](searchdefs.doc.md) |

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
