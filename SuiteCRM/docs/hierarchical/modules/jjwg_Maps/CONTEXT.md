# 📁 jjwg_Maps

**Chemin :** `modules/jjwg_Maps/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module jjwg_Maps est le sous-système de géolocalisation de SuiteCRM (JJW Geo Maps). Il permet d'afficher les enregistrements CRM (comptes, contacts, leads) sur une carte géographique, de géocoder les adresses et d'effectuer des recherches par rayon géographique.

## ⚙️ Responsabilité technique
Bean `jjwg_Maps` (hérite de `jjwg_Maps_sugar`). Module avec router dédié (`jjwg_Maps_Router.php`) et point d'entrée enregistré (`entry_point_registry.php`). Vues multiples pour l'affichage de carte, les marqueurs et la configuration. Consommé par les hooks JJWG de Accounts, Contacts, Leads, Opportunities.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues carte, marqueurs, config, géocodage | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet carte géolocalisation | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `jjwg_Maps.php` | Bean principal de la carte | [→ fiche](jjwg_Maps.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |
| `jjwg_Maps_Router.php` | Router des requêtes carte | [→ fiche](jjwg_Maps_Router.php.doc.md) |
| `entry_point_registry.php` | Enregistrement du point d'entrée | [→ fiche](entry_point_registry.php.doc.md) |
| `vardefs.php` | Schéma de la table `jjwg_maps` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `jjwg_Markers`, `jjwg_Areas`, `jjwg_Address_Cache`
- **Consommé par :** Hooks JJWG de Accounts (`AccountsJjwg_MapsLogicHook`), Contacts, Leads, Opportunities, Cases, Projects
- **Flux typique :** Save enregistrement → hook JJWG géocode l'adresse → marqueur créé → visible sur la carte

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
