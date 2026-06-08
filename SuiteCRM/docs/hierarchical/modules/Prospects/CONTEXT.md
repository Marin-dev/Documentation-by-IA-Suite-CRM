# 📁 Prospects

**Chemin :** `modules/Prospects/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Prospects (aussi appelé "Targets") représente des cibles marketing qui ne sont pas encore des leads ou contacts. Ils sont importés en masse dans les listes de prospects (`ProspectLists`) pour les campagnes email. Peuvent être convertis en leads.

## ⚙️ Responsabilité technique
Bean `Prospect` (hérite de `SugarBean`). Supporte l'import en masse. Hook de géolocalisation JJWG. Vues liste, détail et édition.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues liste, détail, édition | [→ CONTEXT](views/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Prospect.php` | Bean principal des prospects/cibles | [→ fiche](Prospect.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `Delete.php` | Suppression | [→ fiche](Delete.doc.md) |
| `Import.php` | Import en masse de prospects | [→ fiche](Import.doc.md) |
| `ProspectFormBase.php` | Logique de base du formulaire | [→ fiche](ProspectFormBase.doc.md) |
| `ProspectsJjwg_MapsLogicHook.php` | Hook de géolocalisation | [→ fiche](ProspectsJjwg_MapsLogicHook.doc.md) |
| `ProspectsListViewSmarty.php` | Rendu Smarty de la vue liste | [→ fiche](ProspectsListViewSmarty.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `BeanFactory`
- **Consommé par :** `ProspectLists` (listes de cibles), module Campaigns
- **Flux typique :** Import en masse → prospects ajoutés aux listes → utilisés dans les campagnes email

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
